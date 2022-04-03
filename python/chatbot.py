from autocorrect import Speller
from nltk.chat.util import Chat, reflections
from nltk.tokenize import wordpunct_tokenize
from stopwords import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from language_pairs import pairs
from nltk.corpus import wordnet
from googletrans import Translator
import wikipediaapi


def generate_token(msg):
    """Tokenize response and remove all stop words to simplify the statement"""
    text_tokens = wordpunct_tokenize(msg)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords]
    print("Generated tokens: ", " ".join(tokens_without_sw))
    return " ".join(tokens_without_sw)


def Detect_Synonym(msg):
    text_tokens = msg.split()  ## tokenizes based on spaces, does not make `'` a separate token
    pair_tokens = []
    for elem in pairs:
        pair_tokens.append(elem[0].split())

    new_input = []
    for elem in pair_tokens:
        if len(elem) is not len(
                text_tokens):  ## checks token length of user input, and makes sure it matches expected pair (EP)input
            continue

        new_input = []
        for i in range(len(text_tokens)):  ## loops through each work/token in EP input
            if elem[i] == text_tokens[i]:
                new_input.append(elem[i])  ## if the the two words match, add to
            else:
                for syn in wordnet.synsets(elem[i]):  ## if they do not match, loop thru EP input word synonyms,
                    found = False

                    for l in syn.lemmas():
                        if l.name() == text_tokens[i]:  ## if the proposed synonym matches the user input
                            new_input.append(elem[i])  ## add the synonym to te new_input, then break out of two loops
                            found = True
                            break
                    if found:
                        break

    return " ".join(new_input)  ## Makes the new_input list a string unput


class Botler:
    """This is the bolter class it is in charge of maintaining the conversation"""

    def __init__(self):
        """Creates chat object from NLTK"""
        self.chat = Chat(pairs, reflections)
        self.name = "Botler"
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.speller = Speller()
        self.translator = Translator()
        self.wiki = wikipediaapi.Wikipedia('en')

    def _search_wikipedia(self, msg: str):
        """Search wikipedia for a given page, returns summary if it exists, and link, else it returns an error"""
        page = self.wiki.page(msg)

        if not page.exists():
            return "I couldn't find a page about that in wikipedia, sorry sir"

        return f'Here is the page for {page.title} on wikipedia:\n{page.summary[0:100]}...\n\nIf you are curious sir, you can read more ' \
               f'here: {page.fullurl} '

    def _translate_input(self, msg: str):
        """Returns a translation of the given text into the english language"""
        return self.translator.translate(msg, dest="en").text

    def generate_response(self, msg: str):
        """Generates a response for the given text input"""

        # Check if we are asking for a translation
        if self.speller(msg.split()[0]) == "translate":
            return self._translate_input(" ".join(msg.split()[1:]))

        # Correct any spelling mistakes
        clean_input = self.speller(msg)

        # Search wikipedia for the page
        if "search wikipedia for" in clean_input:
            new_input = clean_input.replace("search wikipedia for", "")
            tokens_without_sw = generate_token(new_input)
            return self._search_wikipedia(tokens_without_sw)

        # Generate a response from the chatbot
        response = self.chat.respond(clean_input)

        # If response is still none, tokenize words and try again
        if not response:
            tokens_without_sw = generate_token(clean_input)
            response = self.chat.respond(tokens_without_sw)

        if not response:
            response = self.chat.respond(Detect_Synonym(clean_input))

        # Getting sia_value to hold the dictionary from polarity_scores
        sia_value = self.sentiment_analyzer.polarity_scores(clean_input)

        if response:
            return response
        elif sia_value['compound'] <= -0.5:
            return "I'm sorry you feel that way, but I am\nunable to fix this for you.\nPlease ask something different."
        elif sia_value['compound'] >= 0.5:
            return ("I'm happy to hear that sir,\nalthough I don't quite know what to do with "
                    "that\ninformation.\nWould you mind asking something else?")
        else:
            return "I didn't quite hear that sir,\nwould you mind repeating that?"
