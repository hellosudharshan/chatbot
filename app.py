import streamlit as st
from openai import OpenAI

# 1. Configuration
OPENAI_MODEL = "gpt-3.5-turbo"
API_KEY_KEY = "openai_api_key" # Key for st.session_state

def run_chat_app():
    """
    Contains the core logic for the ChatGPT-like application.
    This function only runs if the API key is successfully set.
    """
    # Initialize the OpenAI client using the key from session state
    try:
        client = OpenAI(api_key=st.session_state[API_KEY_KEY])
    except Exception as e:
        # Fallback if somehow the key is invalid here, though unlikely
        st.error("Error initializing OpenAI client. Please re-enter your API key.")
        del st.session_state[API_KEY_KEY]
        st.experimental_rerun()
        return

    st.title("My ChatGPT Clone 💬")
    
    # Initialize chat history if not present
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input and generate response
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and stream assistant response
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

def api_key_submitted():
    """Callback function to store the API key."""
    # The value of the widget with key="api_input" is stored in st.session_state
    st.session_state[API_KEY_KEY] = st.session_state["api_input"]
    st.session_state["api_input"] = "" # Clear the input field after submission

def main():
    """Main application logic with conditional key check."""
    
    # --- Check for API Key ---
    if API_KEY_KEY not in st.session_state:
        st.title("Welcome to the LLM Chat App! 👋")
        st.markdown(
            """
            This application requires your OpenAI API Key to function.
            Your key is **not** stored anywhere and is used only for this session.
            """
        )
        
        # Use st.form to batch the input and button click into one rerun
        with st.form("api_key_form"):
            api_key = st.text_input(
                "Enter your OpenAI API Key", 
                type="password",
                key="api_input",  # Key to retrieve value in callback
                placeholder="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            )
            st.form_submit_button(
                "Start Chatting",
                on_click=api_key_submitted # Call the function to save key
            )
            
        st.caption("You can get your key from the OpenAI website.")
        
    else:
        # --- API Key is present, run the chat app ---
        run_chat_app()
        
        # Option to clear the key
        if st.sidebar.button("Clear API Key"):
            del st.session_state[API_KEY_KEY]
            st.experimental_rerun()

# Run the application
if __name__ == "__main__":
    main()
