# Groq-Powered AI Chatbot LLAMA 3.1

## Project Overview

An intelligent chatbot application built using Groq's LLM API and Gradio interface, providing a user-friendly conversational AI experience. The system leverages Groq's Llama3-8b-8192 model to generate contextual and engaging responses.

## Key Features

- **Real-time AI Responses**: Powered by Groq's Llama3-8b-8192 model
- **Interactive Chat Interface**: Built with Gradio for seamless user experience
- **Chat History Management**: Maintains conversation context
- **User-friendly Design**: Clean and intuitive interface
- **Responsive Interface**: Works across different devices
- **Easy Deployment**: Quick setup on various platforms

## Technical Stack

- **Backend**: Python
- **AI Model**: Groq's Llama3-8b-8192
- **Frontend Framework**: Gradio
- **API Integration**: Groq Python Client
- **Environment Management**: Python dotenv

## System Architecture

### Components

**Groq Client Integration**

```python
client = Groq(api_key=os.getenv("YOUR_GROQ_API_KEY"))

```

**Chat Completion Function**

```python
def get_chat_completion(message, history):
    history.append((message, ""))
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": message}],
        model="llama3-8b-8192"
    )
    bot_response = chat_completion.choices[0].message.content
    history[-1] = (message, bot_response)
    return history

```

**Gradio Interface**

```python
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(
        label="Your Message",
        placeholder="Type here...",
        lines=2
    )
    submit_button = gr.Button("Send")

```

## 

### Installation and Setup

**Prerequisites**

```bash
pip install -r requirements.txt
```

**Requirements.txt**

```
streamlit
python-dotenv
groq
werkzeug
requests
python-docx 
reportlab
openpyxl
```
    

## Usage Guide

### Starting a Conversation

1. Launch the application
2. Type your message in the text box
3. Click "Send" or press Enter
4. View the AI's response in the chat window

## Technical Details

### API Integration

The application uses Groq's API for generating responses:

```python
chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": message}],
    model="llama3-8b-8192"
)

```

### Chat History Management

- Maintains conversation flow
- Updates history with each interaction
- Preserves context for better responses

### 

### Running the Chatbot

Run the Streamlit application with the following command:

```
streamlit run app.py
```

## Contributing

Contributions are welcome! Please read our contributing guidelines and code of conduct before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
