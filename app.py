import streamlit as st
from openai import OpenAI, RateLimitError
# Import the missing function from the tenacity library
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# 1. Configuration
OPENAI_MODEL = "gpt-3.5-turbo"
API_KEY_KEY = "openai_api_key"  # Key for st.session_state

# 2. Retrying Function Logic
# This decorator is crucial for handling the RateLimitError
@retry(
    wait=wait_exponential(min=1, max=60),  # Wait between 1s and 60s, increasing exponentially
    stop=stop_after_attempt(6),            # Stop after 6 attempts
    retry=retry_if_exception_type(RateLimitError), # Only retry on rate limit errors
    before_sleep=lambda retry_state: st.warning(
        f"Rate limit hit. Retrying in {int(retry_state.next_action.sleep)} seconds... (Attempt {retry_state.attempt_number}/6)"
    )
)
def create_chat_completion_with_retry(client, **kwargs):
    """Function to call OpenAI with built-in retry for RateLimitError."""
    # This is where the actual API call happens
    return client.chat.completions.create(**kwargs)

# 3. Main Chat App Function
def run_chat_app():
    """
    Contains the core logic for the ChatGPT-like application, now including
    resilient API calls with retry logic.
    """
    # Initialize the OpenAI client using the key from session state
    try:
        client = OpenAI(api_key=st.session_state[API_KEY_KEY])
    except Exception:
        st.error("Error initializing OpenAI client. Please re-enter your API key.")
        del st.session_state[API_KEY_KEY]
        st.experimental_rerun()
        return

    st.title("My Resilient LLM Chat App 💬")
    st.caption("Now with built-in retry logic for Rate Limit Errors!")

    # Initialize chat history if not present
    if "messages" not in st.session_state:
        # Start with a friendly system message (optional)
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! Ask me anything, and don't worry about rate limits—I'm designed to retry if I get overloaded."}
        ]

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input and generate response
    if prompt := st.chat_input("What's on your mind?"):
        # 1. Add and display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 2. Generate and stream assistant response with retry logic
        with st.chat_message("assistant"):
            try:
                # Call the retrying function instead of the client directly
                stream = create_chat_completion_with_retry(
                    client,
                    model=OPENAI_MODEL,
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                response = st.write_stream(stream)

            except RateLimitError:
                # This block runs only if ALL 6 retries failed
                st.error("I'm currently overloaded or out of quota. All retries failed. Please try again in a minute.")
                return # Stop processing this message

            # 3. Add assistant response to chat history ONLY if the call was successful
            st.session_state.messages.append({"role": "assistant", "content": response})

# 4. API Key Handling Functions
def api_key_submitted():
    """Callback function to store the API key."""
    # The value of the widget with key="api_input" is stored in st.session_state
    st.session_state[API_KEY_KEY] = st.session_state["api_input"]
    st.session_state["api_input"] = "" # Clear the input field after submission

def main():
    """Main application logic with conditional key check."""

    # --- Check for API Key ---
    if API_KEY_KEY not in st.session_state:
        st.title("Welcome to the Resilient Chat App! 👋")
        st.markdown(
            """
            This application requires your OpenAI API Key to function.
            Your key is **not** stored anywhere and is used only for this session.
            """
        )

        # Use st.form to batch the input and button click into one rerun
        with st.form("api_key_form"):
            st.text_input(
                "Enter your OpenAI API Key",
                type="password",
                key="api_input", # Key to retrieve value in callback
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

        # Option to clear the key in the sidebar
        with st.sidebar:
            st.title("Settings")
            if st.button("Clear API Key and Restart"):
                del st.session_state[API_KEY_KEY]
                st.experimental_rerun()

# Run the application
if __name__ == "__main__":
    main()
