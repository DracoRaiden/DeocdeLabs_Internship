
def main():
    """Entry point for the simple chatbot program.

    Prints a short welcome message. The interactive loop runs at
    module level below so `main()` only serves as a clear starting
    point when the script is executed directly.
    """
    print("Welcome to the Simple Chatbot!")

# A mapping of exact user inputs to the chatbot's canned responses.
# Keys are expected to be lowercase and trimmed (the input is
# normalized before lookup). The 'default' key contains the
# fallback response used when the user's input isn't found.
responses = {
    'hello': "Hello! How can I assist you today?",
    'hi': "Hello! How can I assist you today?",
    'how are you?': "I'm just a program, but I'm here to help you!",
    'what is your name?': "I am a simple chatbot created to assist you.",
    'what can you do?': "I can answer basic questions and have simple conversations. Try asking me something!",
    'bye' : "Goodbye! Have a great day!",
    'default': "I'm sorry, I don't understand that. Can you please rephrase?"
}


# Interactive loop: repeatedly prompt the user until they choose to exit.
while True:
    # Read raw input from the user. The prompt reminds how to quit.
    raw_input = input("Enter a question or type Exit to quit: ")

    # Normalize the input for reliable matching: remove surrounding
    # whitespace and convert to lowercase so lookups are case-insensitive.
    refined_input = raw_input.strip().lower()

    # Check for exit conditions. Accept either 'exit' or 'bye'.
    if refined_input == "exit" or refined_input == "bye":
        print("Exiting the Program. Goodbye!")
        break

    # Look up the response in the `responses` dictionary. If the
    # normalized input isn't found, fall back to the 'default' reply.
    response = responses.get(refined_input, responses['default'])

    # Display the bot's reply prefixed with 'Bot:' so it's clear
    # which lines are user input and which are chatbot responses.
    print(f"Bot: {response}")

if __name__ == "__main__":
    # When run as a script, call the `main()` function to show the
    # welcome message before entering the interactive loop above.
    main()