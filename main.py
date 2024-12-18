import os
import google.generativeai as genai

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=api_key)

# Load the Generative AI model
model = genai.GenerativeModel("gemini-1.5-flash")

print("Chatbot is running. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    try:
        response = model.generate_content(user_input)
        print(f"Bot: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
