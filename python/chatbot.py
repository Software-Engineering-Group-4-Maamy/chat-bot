from nltk.chat.util import Chat, reflections
from nltk.tokenize import wordpunct_tokenize
from stopwords import stopwords
from language_pairs import pairs


def generate_token(msg):
    """Tokenize response and remove all stop words to simplify the statement"""
    text_tokens = wordpunct_tokenize(msg)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords]
    print(tokens_without_sw)
    return " ".join(tokens_without_sw)

class Botler:
    """This is the bolter class it is in charge of maintaining the conversation"""

    def __init__(self):
        """Creates chat object from NLTK"""
        self.chat = Chat(pairs, reflections)
        self.name = "Botler"

    def converse(self):
        """THIS IS NOW DEPRECATED
        Starts the conversation with a custom message. Includes a few error handling if the user inputs anything
        incorrectly"""

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

    def generate_response(self, msg):
        """Generates a response for a specific message"""
        response = self.chat.respond(msg)

        if response is None:
            tokens_without_sw = generate_token(msg)
            response = self.chat.respond(tokens_without_sw)

        return response if response else "Sorry sir, I didn't understand"
