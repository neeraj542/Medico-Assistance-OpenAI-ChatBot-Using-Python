import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "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" #api 
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with a Medical Assistant. I can provide information on medical topics and answer health-related questions. Please remember that I'm not a substitute for professional medical advice. If you have a medical emergency, please call emergency services immediately.
"""

@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Medical Assistant Chatbot logic
#     message_history: List of user messages
#     state: A dictionary to store any stateful information

#     Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
#     """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state

# @textbase.chatbot("medical-assistant-chatbot")
# def on_message(message_history: List[Message], state: dict = None):
#     """Medical Assistant Chatbot logic
#     message_history: List of user messages
#     state: A dictionary to store any stateful information

#     Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
#     """

#     if state is None or "counter" not in state:
#         state = {"counter": 0}
#     else:
#         state["counter"] += 1

#     # Get the latest user message
#     latest_message = message_history[-1].content.lower()

#     # Process user input and get bot response
#     if latest_message.strip() != "":
#         # TODO: Call the backend API or chatbot logic here to get the bot's response
#         # For now, we use a placeholder response for demonstration purposes
#         bot_response = "I'm here to provide medical information and support. However, please remember that I'm not a substitute for professional medical advice. If you have specific health concerns, it's best to consult a healthcare professional."

#     else:
#         # If the user sends an empty message (e.g., just hitting Enter), respond with a prompt
#         bot_response = "I'm here to assist you with medical information and health-related questions. Please feel free to ask anything related to your health."

#     # Display the bot's response
#     bot_response = f"Medical Assistant: {bot_response}"
    
#     return bot_response, state
