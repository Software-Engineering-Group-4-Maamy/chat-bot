import nltk
import nltk.chat
from nltk.chat.util import Chat, reflections
from pairs import language_pairs


def Butler():
    print("Hi, I'm Butler want to have a conversation with you!\nPlease speak to me in lowercase English. Type quit if you wish to end this conversation. ")
    chat = Chat(pairs, reflections)
    chat.converse()

def main():
    Butler()


if __name__ == "__main__":
    main()