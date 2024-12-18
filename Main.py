import openai
API_KEY_OPENAI=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
# Set your API key
openai.api_key = 'API_KEY_OPENAI'

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("Chatbot is running. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
