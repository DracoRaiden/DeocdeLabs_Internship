
def main():
    print("Welcome to the Simple Chatbot!")

responses = {
    'hello': "Hello! How can I assist you today?",
    'hi': "Hello! How can I assist you today?",
    'how are you?': "I'm just a program, but I'm here to help you!",
    'what is your name?': "I am a simple chatbot created to assist you.",
    'what can you do?': "I can answer basic questions and have simple conversations. Try asking me something!",
    'bye' : "Goodbye! Have a great day!",
    'default': "I'm sorry, I don't understand that. Can you please rephrase?"
}


while True:
    raw_input = input("Enter a question or type Exit to quit: ")
    refined_input = raw_input.strip().lower()
    if refined_input == "exit" or refined_input == "bye":
        print("Exiting the Program. Goodbye!")
        break
    response = responses.get(refined_input, responses['default'])
    print(f"Bot: {response}")

if __name__ == "__main__":
    main()