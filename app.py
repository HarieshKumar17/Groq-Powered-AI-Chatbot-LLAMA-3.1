import os
import gradio as gr
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_chat_completion(message, history):
    # Append the user message to history
    history.append((message, ""))  # Add an empty bot response placeholder
    
    # Generate the bot's response using Groq API
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": message}],
        model="llama3-8b-8192"
    )
    bot_response = chat_completion.choices[0].message.content
    
    # Update the last entry in history with the bot's response
    history[-1] = (message, bot_response)
    
    return history

# Define the Gradio interface
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(
        label="Your Message", 
        placeholder="Type here...", 
        lines=2
    )
    
    # Setup submission action
    user_input.submit(get_chat_completion, [user_input, chatbot], chatbot)

    # Optional: Add a button to explicitly send messages
    submit_button = gr.Button("Send")
    submit_button.click(get_chat_completion, [user_input, chatbot], chatbot)

# Launch the app
if __name__ == "__main__":
    demo.launch()
