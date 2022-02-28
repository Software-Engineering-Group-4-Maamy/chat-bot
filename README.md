# M.A.A.M.Y's Chat Bot
Software Engineering Term 2, 2022

Our group has decide to create a chatbot using python. We have used the <a href="https://www.nltk.org/" target="_blank">***NLTK***</a> python Library in order to create our chatbot. The bot will be taking the role of a sassy, well educated, butler with a good scence of humour, meanwhile the user will take the role of its master. The bbroject has a simple input output system that works directly from the terminal, and is not very versatile, requiring exact input - Future revisions and additions could improve versatility. The bot is capabble of sustaining a simple conversation for a minimum of 30 turns. 

The MIT liscence is in this same direcory and is named <a href="https://github.com/Software-Engineering-Group-4-Maamy/chat-bot/blob/main/LICENSE" target="_blank">LICENSE</a>. 

## Instalation guide
1. First, install <a href="https://pip.pypa.io/en/stable/installation/">pip</a> if you have not already
2. Run `pip install --user -U nltk`
3. Then, clone this git reposotory, or download the zip file. 
4. Inside the python directory, run the main.py file `python main.py`
5. Vouala - you now own a human soul.

## Sample output

        Hi, I'm Botler want to have a conversation with you!
        Please speak to me in lowercase English. Type quit if you wish to end this conversation. 
        hello
        Greetings!
        my name is Matthew
        Hello matthew, How are you feeling today?
        I am a bit concerned about this recent stock market fiasco
        Do not be alarmed sir, I've handled your investments accordingly
        sorry for ever doubting you
        You needn't worry at all
        can you find the next best stock for me
        I am unable to search for the next best stock, for now.
        sorry for expecting so much
        You needn't worry at all
        have you seen my underwear?
        I believe you left it under your bed again sir
        I like underwear  
        Exquisite taste sir
        i am not a sir
        Apologies, but sir it is the best I can do.
        you're being difficult
        You literally programed me, I can only say what you allowed me to say
        i love you botler, and you have to love me back
        That is sweet sir, but I only think of you as a an aquaintence
        that was mean
        I am doing my best to be polite, you are just making it difficult
        yes    
        Glad we agree
        sorry botler, i was argumentative
        It is already forgiven.
        can you make me happy
        Of course, sire, I will get you happy but first I'll need milk, brb
        how long will it take you to make me happy
        I cannot say, an hour, a week maybe a decade.  You must find it in yourself to wait
        quit
        Thank you for chatting with me

## Class Organization
1. Botler:
The Botler class is incharge of creating and maintaining all aspects of the chat object imported from the NLTK.

The Botler class has two members within it. `def __init__(self)` and `def converse(self)`. 

The `def __init__(self)` member acts as the Constructor for the Botler object. It creates the chat object as well.

The `def converse(self)` member starts the conversation with a custome message. It also includes all of the error handling and logic required for the main conversation to take place with the chat bot
to start a conversation, write this line of code: `ch.Botler().converse()`