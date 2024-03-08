#TASK_01
def chatbot_response(user_input):
    # Convert user input to lowercase for easier comparison
    user_input = user_input.lower()

    # Define some predefined rules and responses
    rules = {
        "hi": "Hello! How can I help you today?",
        "how are you": "I'm Fine, What about you?",
        "i am fine": "Great to hear that",
        "who are you": "I'm a virtual chatbot!",
        "are you a robot": "I am a chatbot, which is a type of artificial intelligence program.",
        "who created you": "I was created by Sai Charitha.",
        "what is your name": "I'm Madagascar created by Master CHARITHA.",
        "where are you from": "I exist in the virtual world of the internet!",
        "do you have siblings": "I'm an only child, so to speak, no siblings for me!",
        "how old are you": "I'm just a program, so I don't have an age.",
        "what can you do": "I can answer your questions and have simple conversations with you!",
        "what's your favorite color": "I don't have the ability to see colors, so I don't have a favorite!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what time is it": "I don't have a watch, but you can check the time on your device!",
        "what is the weather like today": "I'm afraid I can't check the weather for you, but you can use a weather app!",
        "bye": "Goodbye! Have a great day!",
       "default": "I'm not sure how to respond to that."
    }

    # Check if user input matches any predefined rules
    if user_input in rules:
        # If user input matches a rule, return the corresponding response
        return rules[user_input]
    else:
        # If user input does not match any rule, return the default response
        return rules["default"]

# Simple conversation loop
print("Welcome! Ask me anything or say 'bye' to exit.")
while True:
    # Get user input
    user_input = input("User: ")
    
    # Get chatbot response based on user input
    response = chatbot_response(user_input)
    
    # Print chatbot response
    print("ChatBot:", response)

    # Check if user wants to end the conversation
    if user_input.lower() == "bye":
        # If user says "bye", break out of the loop
        break