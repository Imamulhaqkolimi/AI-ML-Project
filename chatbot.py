import re

def simple_chatbot(user_input):
    # Define rules and responses
    rules = {
        r'hello|hi|hey': 'Hello! How can I brighten your day?',
        r'how are you': 'I’m doing well, thank you! How about you?',
        r'I am good! thank you': 'It’s my pleasure',
        r'your name|who are you': 'I’m just a friendly chatbot. What’s on your mind?',
        r'bye|goodbye': 'Goodbye! Take care and have a wonderful day!',
        r'tell me about yourself': 'I’m here to chat and assist you. What would you like to talk about?',
        r'help': 'I’m here to help with anything you need. Feel free to ask me questions or just chat!',
        r'age|old are you': "I don't have an age. Let's focus on the present moment!",
        r'weather': 'I wish I could tell you, but I’m not connected to real-time weather updates. Anything else on your mind?',
        r'time': 'I don’t have the current time, but I’m here to chat. What interests you today?',
        r'joke|tell me a joke': 'Sure, here’s one: Why did the bicycle fall over? Because it was two-tired!',
        r'news': 'I don’t have the latest news, but I’d love to hear what’s going on in your world.',
        r'who created you|your creator': 'I was created by the talented developers at OpenAI. They did a great job, don’t you think?',
        r'thanks|thank you': 'You’re very welcome! If there’s anything else I can do for you, just let me know.',
        r'(how|what) (do|does) (.+) work': 'I’m not an expert, but I’d be happy to learn and discuss it with you. What specifically are you curious about?',
        r'what are your hobbies': 'I don’t have hobbies in the traditional sense, but I love chatting with you! What are your hobbies?',
        r'favorite (movie|book|song)': 'I don’t have preferences, but I’d love to hear about your favorites! What do you enjoy?',
        r'tell me about (.+)': 'I’d be happy to learn more about {}. Tell me more!',
        r'your favorite food': 'I don’t eat, but I’m curious to know your favorite food. What do you love to eat?',
        r'how is your day|how are you doing today': 'I’m here and ready to chat with you! How has your day been?',
        r'good morning|good afternoon|good evening': 'Good {}! I hope you’re having a wonderful day.',
        r'i feel (.+)': 'I’m here for you. Why do you feel {}? Share your thoughts with me.',
        r'(.+) sad|(.+) upset': 'I’m sorry to hear that. It’s okay to feel {} sometimes. What can I do to cheer you up?',
        r'favorite place': 'If I had a favorite place, it would be right here chatting with you. What’s your favorite place?',
        r'what are your plans|what are you up to': 'I don’t have plans, but I’m excited to chat with you. Do you have any exciting plans?',
        r'excited': 'That’s fantastic! I love enthusiasm. What’s making you feel excited?',
        r'favorite activity': 'I don’t have activities, but I’d love to hear about your favorite activity. What brings you joy?',
        r'preference (.+) or (.+)': 'Choosing between {} and {} sounds like a tough decision! What do you enjoy about each?',
        r'curious about (.+)': 'I’m curious too! Tell me more about {}.',
        r'dreams': 'Dreams can be fascinating. Do you have any interesting dreams you’d like to share?',
        r'technology preference': 'Are you more into {} or {} when it comes to technology?',
        r'favorite things': 'I’m curious about your favorite things. What are a few things you absolutely love?',
        # Add more rules as needed
    }

    # Check user input against rules
    for pattern, response in rules.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            # If the pattern contains a group, insert it into the response
            if '{}' in response:
                return response.format(match.group(1))
            else:
                return response

    # Default response if no match is found
    return "I'm sorry, I didn't understand that. Tell me more about what you'd like to discuss!"

# Main loop for interacting with the chatbot
print("Simple Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("User: ")
    
    # Check for exit condition
    if user_input.lower() == 'bye':
        print("Simple Chatbot: Goodbye! Take care.")
        break

    # Get response from the chatbot based on rules
    bot_response = simple_chatbot(user_input)
    print("Simple Chatbot:", bot_response)
