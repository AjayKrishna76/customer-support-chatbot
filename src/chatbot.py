import os
from openai import OpenAI
from dotenv import load_dotenv

# Replace with your OpenAI API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def customer_support_chatbot(user_message):
  """
  Simulates a basic customer support chatbot conversation using OpenAI completion.

  Args:
      user_message: The user's message to the chatbot.

  Returns:
      The chatbot's response to the user's message.
  """
  # Define conversation history with correct role value
  conversation_history = [
      {"role": "system", "content": "How can I help you today?"},
      {"role": "user", "content": "I had a question..."}
  ]
  conversation_history.append({"role": "user", "content": user_message})

  # Use chat completions endpoint with required arguments
  response = client.chat.completions.create(
      model="gpt-4o",  # Replace with your chosen chat model
      messages=conversation_history,
      max_tokens=100,
      n=1,
      stop=None,
      temperature=0.7
  )
  return response

  # Combine messages content with newlines (optional)
  prompt = "\n".join([message["content"] for message in conversation_history])

# Example usage
user_message = "I'm having trouble logging in to my account."
chatbot_response = customer_support_chatbot(user_message)
print("Customer Support Chatbot:", chatbot_response)
