# AI FAQ Assistant 🤖

The **AI FAQ Assistant** is a web application that allows users to ask natural language questions and get intelligent, real-time answers. It uses **Streamlit** for the user interface, **AWS Bedrock (Claude 3.5 Sonnet)** for natural language processing, and can be extended to include multi-agent workflows using platforms like **CrewAI**.

---

## Features

- **Ask Questions**: Enter a question and receive a detailed answer powered by AI.
- **Streamlit UI**: Clean, user-friendly interface for interacting with the assistant.
- **Claude 3.5 Sonnet**: Uses Anthropic's advanced language model via AWS Bedrock for accurate and intelligent responses.
- **Customizable Workflow**: Extendable to support multi-agent workflows, enabling collaboration between different AI systems.

---

## File Structure

- **`app.py`**  
  The main file for the Streamlit front-end. Displays the input field, handles user queries, and shows the answers.  

- **`backend.py`**  
  Backend logic to interact with AWS Bedrock and retrieve responses from Claude 3.5 Sonnet.  

- **`test_backend.py`**  
  A test script to validate the backend's integration with Claude 3.5 Sonnet. Useful for debugging and testing.  

---

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- An AWS account with access to Bedrock
- API access to Anthropic's Claude 3.5 Sonnet via AWS Bedrock

### Setup Instructions

#### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-faq-assistant.git
cd ai-faq-assistant

2. Set up a Virtual Environment
Create a virtual environment and activate it:

python3 -m venv env
source env/bin/activate


3. Install Dependencies
Install the necessary dependencies:
pip install -r requirements.txt

4. Configure AWS CLI
Configure your AWS CLI credentials:
aws configure

You’ll need to provide:
AWS Access Key
AWS Secret Key
Preferred Region

How to Run the Application
1. Run the Streamlit App

Start the Streamlit application:
streamlit run app.py

2. Open the App in Your Browser
Once the app is running, Streamlit will provide a local URL (e.g., http://localhost:8501). Open this URL in your browser to interact with the assistant.

Testing the Backend
To test the backend functionality separately, run the test_backend.py script:

python test_backend.py

This script will send a test query to Claude 3.5 Sonnet and print the response in the terminal.
