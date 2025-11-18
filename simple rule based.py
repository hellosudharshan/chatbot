import streamlit as st
import random
import re

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            'greeting': [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! Nice to meet you!"
            ],
            'farewell': [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! Come back anytime!"
            ],
            'thanks': [
                "You're welcome!",
                "Happy to help!",
                "Anytime!"
            ],
            'default': [
                "That's interesting. Tell me more!",
                "I see. What else would you like to know?",
                "Could you elaborate on that?",
                "I'm here to help! What can I tell you?"
            ]
        }
        
        self.patterns = {
            'greeting': r'hello|hi|hey|good morning|good afternoon',
            'farewell': r'bye|goodbye|see you|later',
            'thanks': r'thanks|thank you|appreciate'
        }
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        
        for intent, pattern in self.patterns.items():
            if re.search(pattern, user_input):
                return random.choice(self.responses[intent])
        
        return random.choice(self.responses['default'])

# Streamlit app
st.title("🤖 Simple Rule-Based Chatbot")
st.write("Chat with a basic rule-based AI")

# Initialize chatbot and session state
bot = SimpleChatbot()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "user":
        st.write(f"**You:** {message}")
    else:
        st.write(f"**Bot:** {message}")

# Chat input
user_message = st.text_input("Type your message:", key="user_msg")

if st.button("Send") and user_message:
    # Add user message to history
    st.session_state.chat_history.append(("user", user_message))
    
    # Get bot response
    bot_response = bot.get_response(user_message)
    st.session_state.chat_history.append(("bot", bot_response))
    
    st.rerun()
