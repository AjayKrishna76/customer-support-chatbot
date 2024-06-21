import unittest
from src.chatbot import get_response

class TestChatbot(unittest.TestCase):

    def test_get_response(self):
        response = get_response("What are your hours of operation?")
        self.assertIn("24/7", response)

    def test_get_response_reset_password(self):
        response = get_response("How can I reset my password?")
        self.assertIn("reset your password", response)

if __name__ == "__main__":
    unittest.main()
