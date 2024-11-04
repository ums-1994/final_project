import random

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "anxiety" in user_input:
        return random.choice([
            "It's normal to feel anxious sometimes. Could you tell me more about what's causing it?",
            "I understand. Anxiety can be tough. Do you want to talk about what's on your mind?"
        ])
    elif "depression" in user_input or "sad" in user_input:
        return "I'm sorry to hear that you're feeling this way. What's been bothering you lately?"
    elif "stress" in user_input:
        return "Stress can be difficult to manage. Are there specific situations making you feel this way?"
    elif "mood" in user_input:
        return "How would you describe your mood today on a scale from 1 to 10?"
    elif "help" in user_input:
        return "I'm here to help! Could you share a bit more about what you're going through?"
    else:
        return "I'm not sure how to help with that. Can you tell me more?"

def start_chat():
    print("Welcome to the Mental Health Chatbot. Type 'exit' to end the chat.")
    
    # Ask for the user's name
    name = input("What's your name? ")
    print(f"Chatbot: Nice to meet you, {name}! How can I help you today?")
    
    while True:
        user_input = input(f"{name}: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Take care, {name}! Remember, you're not alone.")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        
        # Add a follow-up question after the initial response
        if "anxiety" in user_input:
            follow_up = input("Chatbot: Have you tried any techniques to manage your anxiety? ")
            print(f"Chatbot: That sounds like a good step. Let me know if you'd like more resources on managing anxiety.")
        elif "depression" in user_input or "sad" in user_input:
            follow_up = input("Chatbot: I'm here for you. Would you like to talk to a friend or family member about this? ")
            print("Chatbot: Connecting with others can sometimes help. Remember, there's support out there.")

start_chat()