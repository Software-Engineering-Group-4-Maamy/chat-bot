import nltk
import nltk.chat
from nltk.chat.util import Chat, reflections
#import language_pairs

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you feeling today?", ]
    ],
    [
        r"what is your name ?",
        ["My name is Butler, how may I be of service?", ]
    ],
    [
        r"how are you ?",
        ["I'm doing well my friend!\nHow are you?", ]
    ],
    [
        r"sorry (.*)",
        ["It is already forgiven.", "You needn't worry at all", ]
    ],
    [
         r"Can you find (.*) for me ?",
         ["I am unable to search for %1, for now.", "I will commence a search for %1 when I am able to do so.", ]
    ],
    [
        r"hi|hey|hello",
        ["Salutations!", "Greetings!", ]
    ],
    [
        r"quit",
        ["Farewell, have a fantastic day ", "Until we speak again."]
    ]
   ]
  



def Butler():
    print("Hi, I'm Butler want to have a conversation with you!\nPlease speak to me in lowercase English. Type quit if you wish to end this conversation. ")
    chat = Chat(pairs, reflections)
    chat.converse()

def main():
    Butler()


if __name__ == "__main__":
    main()