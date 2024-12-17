import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    (r'(hi|hello|hey)', ['Hello! How can I assist you today?', 'Hi there!', 'Hey! How can I help you?']),
    (r'how are you?', ['I am doing well, thank you!', 'I am just a bot, but I am good!', 'I’m doing great, thanks for asking!']),
    (r'what is your name?', ['I am BotChat, your friendly assistant.', 'You can call me BotChat.']),
    (r'(.*) your name?', ['My name is BotChat.']),
    (r'what do you do?', ['I am here to chat and answer questions!', 'I can chat, answer your questions, and assist you in many ways.']),
    (r'(.*) help (.*)', ['I am here to help! What do you need assistance with?', 'Sure! How can I assist you today?']),
    (r'what is your purpose?', ['My purpose is to chat with you and assist with any questions you might have.', 'I am designed to assist with various tasks and have conversations.']),
    (r'who created you?', ['I was created by a developer to help with simple tasks and answer questions.', 'I was made by a developer, but I like to think I have a mind of my own!']),
    (r'(.*) are you (.*)', ['I am an AI chatbot created to chat with you and provide useful information.', 'I am BotChat, a friendly assistant bot.']),
    (r'(.*) like (.*)', ['I don’t have personal preferences, but I do like chatting with you!', 'I enjoy talking with people and helping out!']),
    (r'(.*) (thank you|thanks)', ['You’re welcome!', 'Happy to help!']),
    (r'goodbye|bye', ['Goodbye! Have a great day!', 'Bye! It was nice chatting with you.']),
    (r'(.*)', ['Sorry, I did not understand that. Could you rephrase?', 'I’m not sure what you mean. Can you clarify?'])
]

def start_chat():
    print("Hi! I'm BotChat. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    start_chat()
