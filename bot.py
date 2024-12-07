import spacy
import random

# Load SpaCy English language model
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hi there!", "Hello!", "Hey! How can I assist you today?"]
    },
    "name_query": {
        "patterns": ["what is your name", "who are you", "your name"],
        "responses": ["I am Chatbot, your virtual assistant.", "My name is Chatbot."]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "take care"],
        "responses": ["Goodbye!", "Take care! Have a great day!", "See you soon!"]
    },
    "education": {
        "patterns": ["tell me about education", "what is education", "education information"],
        "responses": ["Education is the process of facilitating learning, or the acquisition of knowledge, skills, and values."]
    },
    "healthcare": {
        "patterns": ["tell me about healthcare", "healthcare information", "what is healthcare"],
        "responses": ["Healthcare involves the maintenance or improvement of health via diagnosis, treatment, and prevention of disease."]
    },
    "customer_service": {
        "patterns": ["customer service", "help with product", "support"],
        "responses": ["How can I assist you with our products or services?", "Please let me know your query regarding our services."]
    },
    "jokes": {
        "patterns": ["tell me a joke", "make me laugh", "funny"],
        "responses": [
            "Why don't skeletons fight each other? They don't have the guts!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call fake spaghetti? An impasta!"
        ]
    },
    "weather": {
        "patterns": ["what's the weather like", "tell me the weather", "weather forecast", "how's the weather"],
        "responses": [
            "The weather is sunny with a slight chance of rain today.",
            "It looks like it's going to rain. Don't forget your umbrella!",
            "It's cloudy with a chance of showers. Stay dry!"
        ]
    },
    "sports": {
        "patterns": ["what's the score", "tell me the latest match result", "sports news"],
        "responses": [
            "The latest football match ended 3-1 in favor of Manchester United.",
            "The NBA Finals are ongoing. The score is tied at 2-2.",
            "Did you hear about the tennis match? Federer won in straight sets!"
        ]
    },
    "technology": {
        "patterns": ["tell me about the latest tech", "new technology", "what's new in tech", "tech news"],
        "responses": [
            "Artificial intelligence is making significant progress in healthcare and automation.",
            "The latest tech gadget released this year is the new iPhone, featuring cutting-edge camera technology.",
            "Quantum computing is the future, with companies like IBM and Google working on powerful quantum processors."
        ]
    },
    "movies": {
        "patterns": ["what's a good movie", "tell me about the latest movies", "movie recommendations", "new movies"],
        "responses": [
            "If you enjoy action, 'Mission Impossible 7' is a must-watch.",
            "For a good drama, check out 'The Shawshank Redemption.' It's a classic!",
            "The latest sci-fi movie, 'Dune', is a visual masterpiece. Highly recommended!"
        ]
    },
    "music": {
        "patterns": ["tell me about music", "music recommendations", "what's the latest song", "new music"],
        "responses": [
            "The latest album by Taylor Swift is topping the charts. Have you listened to it yet?",
            "If you like pop, you might enjoy 'Blinding Lights' by The Weeknd.",
            "A great new song to check out is 'Levitating' by Dua Lipa. It's really catchy!"
        ]
    },
    "news": {
        "patterns": ["what's the latest news", "tell me the news", "current events", "news updates"],
        "responses": [
            "The latest news: There is a significant breakthrough in renewable energy technologies.",
            "Breaking news: The stock market saw a sharp increase in tech stocks today.",
            "Today's top story: The government is introducing new policies for healthcare reforms."
        ]
    },
    "facts": {
        "patterns": ["tell me a fact", "random fact", "interesting fact"],
        "responses": [
            "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!",
            "Here’s a fun fact: An octopus has three hearts!",
            "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the metal!"
        ]
    }
}

# Preprocess user input and identify intent
def recognize_intent(user_input):
    doc = nlp(user_input.lower())
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in user_input.lower():
                return intent
    return None

# Generate a response based on the recognized intent
def generate_response(intent):
    if intent in intents:
        return random.choice(intents[intent]["responses"])
    return "I'm sorry, I didn't understand that. Could you please rephrase?"

# Chat function
def chat():
    print("Chatbot: Hello! I am Chatbot. How can I assist you today? (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Recognize intent and generate response
        intent = recognize_intent(user_input)
        response = generate_response(intent)
        print(f"Chatbot: {response}")

# Start the chatbot
chat()
