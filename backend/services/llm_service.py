import json

def get_recommendations(city, preferences):
    text = {"message": "Hello world"}

    try:
        return json.loads(text)
    except:
        return {"error": "Invalid JSON from LLM", "raw": text}
    
if __name__ == "__main__":
    get_recommendations("New York", ["museums", "parks"])