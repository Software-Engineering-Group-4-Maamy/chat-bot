import nltk
import nltk.chat
from nltk.chat.util import Chat, reflections
from language_pairs import pairs


def Botler():
    print("Hi, I'm Botler want to have a conversation with you!\nPlease speak to me in lowercase English. Type quit if you wish to end this conversation. ")
    chat = Chat(pairs, reflections)
    chat.converse()

def main():
    Botler()


if __name__ == "__main__":
    main()