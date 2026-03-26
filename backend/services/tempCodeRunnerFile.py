import json
import ollama

client =ollama.Client()
def get_recommendations(user_data_json):
    try: 
        user_data = json.loads(user_data_json)
    except (json.JSONDecodeError, TypeError):
       return {"error": "Invalid input: Expected a JSON string"}

    user_profile = dict(
        target_city = user_data.get("city", "Unknown"),
        money = user_data.get("budget", "Flexible"),
        start = user_data.get("start_date", "TBD"),
        end = user_data.get("end_date", "TBD"),
        wishes = ", ".join(user_data.get("list of desires", []))
    )
    
    
    prompt = f"""
    Return ONLY JSON.
    
    The user is traveling to {user_profile['target_city']}.
    His budget is {user_profile['money']}.
    He will be there from {user_profile['start']} to {user_profile['end']}.
    He is interested in {user_profile['wishes']}.

    Suggest 5 less crowded alternative cities.

    Format:
    [
      {{
        "city": "...",
        "country": "...",
        "description": "..."
        "daily budget": "..."
        "similarities to your desires": "..."
      }}
    ]
    """

    response = client.generate(
        model="phi3",
        prompt=prompt,
        format = "json"
    )

    text = response['response']

    try:
        return json.loads(response['response'])
    except Exception as e:
        return {"error": "Invalid JSON from LLM", "raw": text}
    
if __name__ == "__main__":
    data = {
        "city": "Paris",
        "budget": "1500 USD",
        "start_date": "2024-07-01",
        "end_date": "2024-07-10",
        "list of desires": ["art", "history", "cuisine"]
        }
    
    json_input = json.dumps(data)
    results = get_recommendations(json_input)
    print(json.dumps(results, indent=2))