import autocorrect
import nltk
import nltk.chat
from autocorrect import Speller
from nltk.chat.util import Chat, reflections
from nltk.tokenize import wordpunct_tokenize
from stopwords import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
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
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.speller = Speller()
       
    def converse(self):
        """THIS IS NOW DEPRECATED
        Starts the conversation with a custom message. Includes a few error handling if the user inputs anything
        incorrectly"""

        print("Hi, I'm Botler want to have a conversation with you!\nPlease speak to me in lowercase English. Type "
              "quit if you wish to end this conversation. ")
        
        # starting SIA from NLTK package.No usage implemented yet.
        sia = SentimentIntensityAnalyzer()
        
        # speller() parses user input for errors and corrects.
        spell = Speller()
        user_input = input()
        cleaned_input = spell(user_input).lower()

        while cleaned_input != "quit":
            # if for notifying user their input has been corrected
            if str(user_input).lower() != str(cleaned_input):
                print("Spelling mistakes were detected in your text, you said:\n " + str(user_input) + "\nAnd it was corrected to: \n" + str(cleaned_input) )
            
            response = self.chat.respond(cleaned_input)
            
            # if/else for handling no pre-programmed response
            if str(response) != "None":
                print(sia.polarity_scores(cleaned_input))
                print(response)    
            else:
                print(sia.polarity_scores(cleaned_input))
                print("Sorry sir, I didn't understand")

            # setting new inputs for loop
            user_input = input()
            cleaned_input = spell(user_input).lower()

        print("Thank you for chatting with me")

    def generate_response(self, msg):
        # Correct any spelling mistakes
        clean_input = self.speller(msg)

        # Generate a response from the chatbot
        response = self.chat.respond(clean_input)
        
        # If response is still none, tekenize words and try again
        if response is None:
            tokens_without_sw = generate_token(clean_input)
            response = self.chat.respond(tokens_without_sw)

        # Print polarity score of message
        print(clean_input, self.sentiment_analyzer.polarity_scores(clean_input), sep=": ")

        return response if response else "Sorry sir, I didn't understand"
