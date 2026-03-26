from google import genai

KEY = "AIzaSyAYA7JNLpiEoNRUEuSRJL7z6HslMv4-4A4" 

client = genai.Client(api_key=KEY)

try:
    user_input = input("Enter your prompt: ")
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_input
    )
    print(response.text)
except Exception as e:
    print(f"Error occurred: {e}")