from autocorrect import Speller
from nltk.chat.util import Chat, reflections
from nltk.tokenize import wordpunct_tokenize
from stopwords import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from language_pairs import pairs
from nltk.corpus import wordnet


def generate_token(msg):
    """Tokenize response and remove all stop words to simplify the statement"""
    text_tokens = wordpunct_tokenize(msg)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords]
    return " ".join(tokens_without_sw)

def Detect_Synonym(msg):
    text_tokens = msg.split()
    pair_tokens = []
    for elem in pairs:
        pair_tokens.append(elem[0].split())

    new_input = []
    for elem in pair_tokens:
        if len(elem) is not len(text_tokens): ## checks token length of user input, and makes sure it matches expected pair (EP)input
            continue
        
        new_input = []
        for i in range(len(text_tokens)):              ##loops through each work/token in EP input 
            if elem[i] == text_tokens[i]:                         
                new_input.append(elem[i])
            else:
                for syn in wordnet.synsets(elem[i]):
                    found = False

                    for l in syn.lemmas():
                        if l.name() == text_tokens[i]:
                            new_input.append(elem[i])
                            found = True
                            break
                    if found:
                        break

    return " ".join(new_input)


class Botler:
    """This is the bolter class it is in charge of maintaining the conversation"""

    def __init__(self):
        """Creates chat object from NLTK"""
        self.chat = Chat(pairs, reflections)
        self.name = "Botler"
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.speller = Speller()

    def generate_response(self, msg):
        # Correct any spelling mistakes
        clean_input = self.speller(msg)

        # Generate a response from the chatbot
        response = self.chat.respond(clean_input)

        # If response is still none, tokenize words and try again
        if not response:
            tokens_without_sw = generate_token(clean_input)
            response = self.chat.respond(tokens_without_sw)
        
        #if not response:
        if not response:
            response = self.chat.respond(Detect_Synonym(clean_input))



        # Print polarity score of message
        print(clean_input, self.sentiment_analyzer.polarity_scores(clean_input), sep=": ")

        return response if response else "Sorry sir, I didn't understand"



    # Very basically I want to take an INPUT and create an array of inputs that is the length of each words synonyms multiplied together.
        ## For example, have you seen my underwear -> have you witnessed my underware, have you witnessed my undergarmnets and so on.
        ## how to parse out each 'possible sysnonym' word, I am not sure. I could do all of the