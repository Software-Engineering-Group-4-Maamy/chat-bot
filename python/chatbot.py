import autocorrect
import nltk
import nltk.chat
from autocorrect import Speller
from nltk.chat.util import Chat, reflections
from nltk.sentiment import SentimentIntensityAnalyzer

from language_pairs import pairs


class Botler:
    """This is the bolter class it is in charge of maintaining the conversation"""

    def __init__(self):
        """Creates chat object from NLTK"""
        self.chat = Chat(pairs, reflections)
        


    def converse(self):
        """Starts the conversation with a custom message.  Includes a few error handling if the user inputs anything
        incorrectly"""

        print("Hi, I'm Botler want to have a conversation with you!\nPlease speak to me in lowercase English. Type "
              "quit if you wish to end this conversation. ")
        
        #starting SIA from NLTK package.No usage implemented yet.
        sia = SentimentIntensityAnalyzer()
        
        #speller() parses user input for errors and corrects.
        spell = Speller()
        user_input = input()
        cleaned_input = spell(user_input).lower()


        while cleaned_input != "quit":
            #if for notfying user their input has been corrected
            if(str(user_input).lower() != str(cleaned_input)):
                print("Spelling mistakes were detected in your text, you said:\n " + str(user_input) + "\nAnd it was corrected to: \n" + str(cleaned_input) )
            
            response = self.chat.respond(cleaned_input)
            
            #if/else for handling no pre-programmed response
            if(str(response) != "None"):
                print(sia.polarity_scores(cleaned_input))
                print(response)    
            else:
                print(sia.polarity_scores(cleaned_input))
                print("Sorry sir, I didn't understand")

            #setting new inputs for loop
            user_input = input()
            cleaned_input = spell(user_input).lower()

        print("Thank you for chatting with me")
