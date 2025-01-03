import streamlit as st
from backend import get_claude_answer

# Set up the Streamlit page with a title and custom styling
st.set_page_config(page_title="AI FAQ Assistant", page_icon="🤖", layout="centered")

# Custom CSS to improve the UI
st.markdown("""
    <style>
        .stTextInput > div > div > input {
            font-size: 18px;
            height: 40px;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            height: 45px;
            width: 120px;
            border-radius: 5px;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .stWrite {
            font-size: 16px;
            line-height: 1.8;
            margin-top: 20px;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
        }
        .subheader {
            font-size: 20px;
            color: #555;
        }
        .answer-box {
            padding: 20px;
            background-color: #f0f8ff;  /* Light blue background */
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            color: #333;
            font-size: 16px;
            line-height: 1.6;
            max-width: 700px;
            word-wrap: break-word;
        }
    </style>
""", unsafe_allow_html=True)

# Set the app title with larger font
st.markdown("<div class='title'>AI FAQ Assistant</div>", unsafe_allow_html=True)

# Add a subheader for the input area
st.markdown("<div class='subheader'>Ask any question and get an answer powered by AI 🤖</div>", unsafe_allow_html=True)

# Create a text input widget for the question with a placeholder
question = st.text_input("What would you like to know?", placeholder="Enter your question here...")

# Add a search button with custom styling
if st.button("Search"):
    if question:
        # Show loading indicator
        with st.spinner('Fetching answer...'):
            # Fetch the answer from Claude 3.5 Sonnet
            answer = get_claude_answer(question)
        
        # Display the response in a styled box
        st.markdown(f"<div class='answer-box'><b>Answer:</b><br>{answer}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a question to search.")


