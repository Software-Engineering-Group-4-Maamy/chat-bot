import unittest;
"""
Unit tests for the chatbot.py module.
"""
from chatbot import *;
from nltk.chat.util import Chat;
from autocorrect import Speller
from nltk.sentiment import SentimentIntensityAnalyzer

class TestChatBot(unittest.TestCase):

    def test_generate_token(self):
        result = generate_token("Hello, how are you?");
        print(result);
        """Check return type is a string"""
        self.assertIsInstance(result, str);

    def test_Botler_init_attributes(self):
        """Check the attributes of the Botler class"""
        botler = Botler();
        self.assertIsInstance(botler.chat, Chat);
        self.assertEqual(botler.name, "Botler");
        self.assertIsInstance(botler.sentiment_analyzer, SentimentIntensityAnalyzer);
        self.assertIsInstance(botler.speller, Speller);

    def test_Botler(self):
        response = Botler().generate_response("Hello, how are you?");
        print("Response: " + response);
        """Check return type is a string"""
        self.assertIsInstance(response, str);

    
if __name__ == '__main__':
    unittest.main()