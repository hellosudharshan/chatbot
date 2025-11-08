import streamlit as st
# Import the Google GenAI SDK and the specific error for rate limits
from google import genai
from google.generativeai.errors import ResourceExhaustedError
# Import tenacity components
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# 1. Configuration
# We switch to a Gemini model
GEMINI_MODEL = "gemini-2.5-flash"
API_KEY_KEY = "gemini_api_key"  # Key for st.session_state

# 2. Retrying Function Logic
@retry(
    wait=wait_exponential(min=1, max=60),  # Wait between 1s and 60s, increasing exponentially
    stop=stop_after_attempt(6),            # Stop after 6 attempts
    # Change the exception type to catch the Gemini rate limit error
    retry=retry_if_exception_type(ResourceExhaustedError),
    before_sleep=lambda retry_state: st.warning(
        f"Resource Exhausted (Rate Limit). Retrying in {int(retry_state.next_action.sleep)} seconds... (Attempt {retry_state.attempt_number}/6)"
    )
)
def create_chat_completion_with_retry(client, **kwargs):
    """Function to call Gemini API with built-in retry for ResourceExhaustedError."""
    # Extract the required arguments for the Gemini SDK call
    messages = kwargs.pop('messages')
    model = kwargs.pop('model')
    
    # Use generate_content_stream for streaming equivalent
    return client.models.generate_content_stream(
        model=model,
        contents=messages
    )

# 3. Message Format Conversion Helper
def convert_to_gemini_format(st_messages):
    """
    Converts Streamlit session state messages (role, content) into the 
    Gemini SDK's expected structure (role, parts).
    """
    gemini_messages = []
    for msg in st_messages:
        # The Gemini SDK uses 'model' for the assistant role
        role = "model" if msg["role"] == "assistant" else "user"
        
        # All content must be inside a 'parts' list
        gemini_messages.append({
            "role": role,
            "parts": [{"text": msg["content"]}]
        })
    return gemini_messages

# 4. Main Chat App Function
def run_chat_app():
    """
    Contains the core logic for the Gemini application, including
    resilient API calls with retry logic.
    """
    # Initialize the Gemini client using the key from session state
    try:
        # We pass the API key from session state to the client
        client = genai.Client(api_key=st.session_state[API_KEY_KEY])
    except Exception:
        st.error("Error initializing Gemini client. Please re-enter your API key.")
        del st.session_state[API_KEY_KEY]
        st.experimental_rerun()
        return

    st.title("My Resilient Gemini Chat App 💬")
    st.caption(f"Using Model: **{GEMINI_MODEL}** | Now with built-in retry logic!")

    # Initialize chat history if not present
    if "messages" not in st.session_state:
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

        # 2. Convert history to Gemini format
        gemini_history = convert_to_gemini_format(st.session_state.messages)

        # 3. Generate and stream assistant response with retry logic
        with st.chat_message("assistant"):
            try:
                # Call the retrying function
                stream = create_chat_completion_with_retry(
                    client,
                    model=GEMINI_MODEL,
                    messages=gemini_history,
                )
                
                # st.write_stream handles iterating over the stream object (which returns chunks)
                response = st.write_stream(stream)

            except ResourceExhaustedError:
                # This block runs only if ALL 6 retries failed
                st.error("I'm currently overloaded or out of quota. All retries failed. Please try again in a minute.")
                return # Stop processing this message
            except Exception as e:
                # Catch any other unexpected API error
                st.error(f"An unexpected API error occurred: {e}")
                return

            # 4. Add assistant response to chat history ONLY if the call was successful
            st.session_state.messages.append({"role": "assistant", "content": response})

# 5. API Key Handling Functions
def api_key_submitted():
    """Callback function to store the API key."""
    st.session_state[API_KEY_KEY] = st.session_state["api_input"]
    st.session_state["api_input"] = "" # Clear the input field after submission

def main():
    """Main application logic with conditional key check."""

    # --- Check for API Key ---
    if API_KEY_KEY not in st.session_state:
        st.title("Welcome to the Resilient Gemini Chat App! 👋")
        st.markdown(
            """
            This application uses the **Google Gemini API** (`gemini-2.5-flash`).
            Please enter your API Key to begin. Your key is used only for this session.
            """
        )

        with st.form("api_key_form"):
            st.text_input(
                "Enter your Gemini API Key",
                type="password",
                key="api_input", # Key to retrieve value in callback
                placeholder="AIzaSy...your-key-goes-here"
            )
            st.form_submit_button(
                "Start Chatting",
                on_click=api_key_submitted # Call the function to save key
            )

        st.caption("You can get your key from Google AI Studio.")

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
