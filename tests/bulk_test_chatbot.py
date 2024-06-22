import unittest
import sys
import os
from unittest.mock import patch

# Add src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from chatbot import customer_support_chatbot

def bulk_run():
    test_cases = [
        "I'm having trouble logging in to my account.",
        "What are your hours of operation?",
        "How can I reset my password?",
        "Where can I track my order?",
        "What is your return policy?"
    ]

    expected_responses = [
        "Sure, I can help you with that.",
        "Our customer support is available 24/7.",
        "You can reset your password by clicking on the 'Forgot Password' link on the login page.",
        "You can track your order in the 'My Orders' section of your account dashboard.",
        "You can return any item within 30 days of purchase for a full refund."
    ]

    for i, query in enumerate(test_cases):
        with patch('chatbot.client.chat.completions.create') as mock_create:
            mock_response = {
                'choices': [
                    {
                        'message': {
                            'role': 'assistant',
                            'content': expected_responses[i]
                        }
                    }
                ]
            }
            mock_create.return_value = mock_response
            response = customer_support_chatbot(query)
            assert expected_responses[i] in response['choices'][0]['message']['content']
            print(f"Test case {i+1} passed")

if __name__ == "__main__":
    bulk_run()
