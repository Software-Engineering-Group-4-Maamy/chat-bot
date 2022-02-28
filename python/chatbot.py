import nltk
import nltk.chat
from nltk.chat.util import Chat, reflections
from language_pairs import pairs


class Botler:
    def __init__(self):
        self.chat = Chat(pairs, reflections)

    def converse(self):
        print("Hi, I'm Botler want to have a conversation with you!\nPlease speak to me in lowercase English. Type "
              "quit if you wish to end this conversation. ")

        user_input = input()
        while user_input != "quit":
            response = self.chat.respond(user_input)
            if response:
                print(response)
            else:
                print("Sorry sir, I didn't understand")

            user_input = input()

        print("Thank you for chatting with me")
