import json
import ollama

client = ollama.Client()

def get_recommendations(user_data_input):
    # Parse input if it's a JSON string, otherwise use it directly as a dict
    if isinstance(user_data_input, str):
        user_data = json.loads(user_data_input)
    else:
        user_data = user_data_input

    # Extracting variables based on the updated HTML form fields
    user_profile = dict(
        target_city = user_data.get("city", "Unknown"),
        money = user_data.get("budget", "Flexible"),
        days = user_data.get("days", "a few"),
        interests = user_data.get("interests", "general sightseeing")
    )
    
    prompt = f"""
    Return ONLY JSON.
    
    The user is traveling for {user_profile['days']} days and is using {user_profile['target_city']} as their baseline inspiration.
    Their total budget is {user_profile['money']}.
    They are highly interested in: {user_profile['interests']}.

    Suggest 4 less crowded alternative cities that offer a similar vibe to {user_profile['target_city']} but align well with their specific interests and budget.
    The alternative cities should NOT be capitals or in the top 5 most visited in that country. They should be less known but still offer a rich experience in terms of culture, art, history, and local cuisine.

    Format(FOLLOW STRICTLY):
    [
      {{
        "city": "...",
        "country": "...",
        "description": "...",
        "dailyBudget": "...",
        "similaritiesToYourDesires": "...",
        "latitude": "...",
        "longitude": "..."
      }}
    ]
    """
    
    print("Prompt sent to LLM:\n", prompt)

    response = client.generate(
        model="phi3",
        prompt=prompt,
        format="json"
    )

    text = response['response']

    try:
        return json.loads(text)
    except Exception as e:
        return {"error": "Invalid JSON from LLM", "raw": text}
    
if __name__ == "__main__":
    # Updated test data to mirror the HTML form inputs
    data = {
        "city": "Paris",
        "budget": 1500,
        "days": 9,
        "interests": "art, history, local cuisine, and architecture"
    }
    
    # Passing the dictionary directly (the function now handles both dicts and JSON strings safely)
    results = get_recommendations(data)
    print(json.dumps(results, indent=2))