from email.mime import application
import imp
import unittest
from app import ChatApplication;
from chatbot import Botler;
from tkinter import *;
class TestApp(unittest.TestCase):
    """
    This file contains all the tests for the app.py
    """
    def test_app_instances(self):
        """
        This is the test for the app function
        """
        application = ChatApplication();
        """Running post-initilization tests"""
        # Check type of chat is a Botler
        self.assertIsInstance(application.chat, Botler);
        # Check type of window is a Tk
        self.assertIsInstance(application.window, Tk);
        # Check type of text widget is a Text
        self.assertIsInstance(application.text_widget, Text);
        # Check type of msg_entry is a Entry
        self.assertIsInstance(application.msg_entry, Entry);

    def test_app_title(self):
        """
        This is the test for the title of the window
        """
        application = ChatApplication();
        self.assertEqual(application.window.title(), "Botler the Butler");

    def test_app_insert_message(self):
        """
        This is the test for the insert message function
        """
        application = ChatApplication();
        application._insert_message("Hello", "You");
        self.assertIn("Hello\n\n\n" ,application.text_widget.get(1.0, END));

if __name__ == '__main__':
    unittest.main()