import unittest
import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from chatbot import customer_support_chatbot


class TestChatbot(unittest.TestCase):

    @patch('chatbot.client.chat.completions.create')
    def test_customer_support_chatbot(self, mock_create):
        # Mocking the response from OpenAI
        mock_response = {
            'choices': [
                {
                    'message': {
                        'role': 'assistant',
                        'content': "Sure, I can help you with that."
                    }
                }
            ]
        }
        mock_create.return_value = mock_response

        user_message = "I'm having trouble logging in to my account."
        response = customer_support_chatbot(user_message)
        self.assertIn("Sure, I can help you with that.", response['choices'][0]['message']['content'])

    @patch('chatbot.client.chat.completions.create')
    def test_customer_support_chatbot_other_query(self, mock_create):
        # Mocking the response from OpenAI
        mock_response = {
            'choices': [
                {
                    'message': {
                        'role': 'assistant',
                        'content': "Our customer support is available 24/7."
                    }
                }
            ]
        }
        mock_create.return_value = mock_response

        user_message = "What are your hours of operation?"
        response = customer_support_chatbot(user_message)
        self.assertIn("Our customer support is available 24/7.", response['choices'][0]['message']['content'])

if __name__ == "__main__":
    unittest.main()
