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

    return {
        "cities": [
            {
            "city": "Lisbon",
            "country": "Portugal",
            "description": "A charming city with a rich history, stunning architecture, and delicious cuisine.",
            "dailyBudget": "$120-$150",
            "similaritiesToYourDesires": "Offers art museums such as the Mosteiro dos Jerónimos; numerous historical sites like Belém Tower. Local seafood is a must-try, reflecting its Portuguese culinary tradition.",
            "latitude": 38.720145,
            "longitude": -9.136101
            },
            {
            "city": "Siena",
            "country": "Italy",
            "description": "A picturesque Tuscan hill town with medieval streets and Renaissance art.",
            "dailyBudget": "$80-$120",
            "similaritiesToYourDesires": "Home to the Siena Cathedral, a stunning example of Italian Gothic architecture. Offers local truffles in dishes which is unique cuisine experience.",
            "latitude": 43.356891,
            "longitude": 11.327008
            },
            {
            "city": "Copenhagen",
            "country": "Denmark",
            "description": "Known for its architecture and design museums like the Louisiana Museum of Modern Art.",
            "dailyBudget": "$100-$130",
            "similaritiesToYourDesires": "The city offers a rich culinary tradition with dishes such as smorrebord. The Freemasons' Church and Rosenborg Castle are historical sites to explore."
            },
            {
            "city": "Bucharest",
            "country": "Romania",
            "description": "The capital of Romania, known for the historicity reflected in its architecture.",
            "dailyBudget": "$70-$100",
            "similaritiesToYourDesires": "Offers art museums like Muzeul de Arta din Bucurest and Palatul Parlamentului. Culinary delights can be enjoyed at places such as Babesca Biserica.",
            "latitude": 44.431287,
            "longitude": 23.059862
            }
        ]
    }

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