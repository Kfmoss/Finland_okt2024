import random

# Predefined responses
greetings = ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you today?"]
farewells = ["Goodbye!", "See you later!", "Take care!", "Bye!"]
feeling_responses = {
    "happy": ["I'm glad to hear that!", "That's great!", "Keep up the good mood!"],
    "sad": ["I'm sorry to hear that. Things will get better!", "It's okay to feel sad sometimes.", "Do you want to talk about it?"],
}
topics_responses = {
    "python": ["Python is a versatile programming language.", "Do you want to learn more about Python?"],
    "weather": ["The weather is different everywhere! Do you like sunny or rainy days?", "Do you want to know the weather forecast?"],
}

# Function to get chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Greeting
    if "hi" in user_input or "hello" in user_input or "hey" in user_input:
        return random.choice(greetings)
    
    # Farewell
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(farewells)
    
    # Feelings (simple sentiment detection)
    elif "happy" in user_input:
        return random.choice(feeling_responses["happy"])
    elif "sad" in user_input:
        return random.choice(feeling_responses["sad"])
    
    # Topics
    elif "python" in user_input:
        return random.choice(topics_responses["python"])
    elif "weather" in user_input:
        return random.choice(topics_responses["weather"])
    
    # Default response if no keywords match
    else:
        return "I'm not sure how to respond to that. Can you ask me something else?"

# Main chatbot loop
def start_chatbot():
    print("Chatbot: Hi! I'm your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if "bye" in user_input.lower():
            print("Chatbot: " + random.choice(farewells))
            break
        
        # Get response from chatbot
        response = chatbot_response(user_input)
        print("Chatbot: " + response)

# Run the chatbot
start_chatbot()
