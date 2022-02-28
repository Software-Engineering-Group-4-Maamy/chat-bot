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

        B:Hi, I'm Botler want to have a conversation with you!
        B:Please speak to me in lowercase English. Type quit if you wish to end this conversation. 
        U:hello
        B:Greetings!
        U:my name is Matthew
        B:Hello matthew, How are you feeling today?
        U:I am a bit concerned about this recent stock market fiasco
        B:Do not be alarmed sir, I've handled your investments accordingly
        U:sorry for ever doubting you
        B:You needn't worry at all
        U:can you find the next best stock for me
        B:I am unable to search for the next best stock, for now.
        U:sorry for expecting so much
        B:You needn't worry at all
        U:have you seen my underwear?
        B:I believe you left it under your bed again sir
        U:I like underwear  
        B:Exquisite taste sir
        U:i am not a sir
        B:Apologies, but sir it is the best I can do.
        U:you're being difficult
        B:You literally programed me, I can only say what you allowed me to say
        U:i love you botler, and you have to love me back
        B:That is sweet sir, but I only think of you as a an aquaintence
        U:that was mean
        B:I am doing my best to be polite, you are just making it difficult
        U:yes    
        B:Glad we agree
        U:sorry botler, i was argumentative
        B:It is already forgiven.
        U:can you make me happy
        B:Of course, sire, I will get you happy but first I'll need milk, brb
        U:how long will it take you to make me happy
        B:I cannot say, an hour, a week maybe a decade.  You must find it in yourself to wait
        U:quit
        B:Thank you for chatting with me
### Errors in output
        U:that was MEAN
        B:Sorry sir, I didn't understand
Botler responds this way because Botler does not understand capital letters. The user must put all inputs as lowercase english

        U:what's your favotite movie
        B:Sorry sir, I didn't understand
Botler responds this way because Botler cannot recognize a phraze that is not exactly the same as what it uses as examples.
## Class Organization
1. Botler:
The Botler class is incharge of creating and maintaining all aspects of the chat object imported from the NLTK.

The Botler class has two members within it. `def __init__(self)` and `def converse(self)`. 

The `def __init__(self)` member acts as the Constructor for the Botler object. It creates the chat object as well.

The `def converse(self)` member starts the conversation with a custome message. It also includes all of the error handling and logic required for the main conversation to take place with the chat bot
to start a conversation, write this line of code: `ch.Botler().converse()`
