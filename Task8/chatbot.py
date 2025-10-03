# Simple Rule-Based Chatbot using if-else

print("🤖 Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("🤖 Chatbot: Hello! How can I help you today?")

    elif "name" in user_input:
        print("🤖 Chatbot: I am a Python chatbot created using if-else rules.")

    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm just a bot, but I'm doing great! Thanks for asking 😊")

    elif "bye" in user_input or "exit" in user_input:
        print("🤖 Chatbot: Goodbye! Have a nice day 👋")
        break

    elif "help" in user_input:
        print("🤖 Chatbot: Sure! You can ask me about my name, how I am, or just say hi!")

    else:
        print("🤖 Chatbot: Sorry, I don’t understand that. Can you rephrase?")