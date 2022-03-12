"""All the input and responses that the chatbot can receive and give"""
pairs = [
    [
        r"my name is (.*)|my name|(.*) my name|my name (.*)",
        ["Hello, how are you feeling today?", ]
    ],
    [
        
        r"i am a bit concerned about this recent stock market fiasco|concerned stock market|(.*) concerned stock market|concerned stock market (.*)",
        ["Do not be alarmed sir, I've handled your investments accordingly",]
        
    ],
    [
        r"what is your name ?|your name|(.*) your name|your name (.*)",
        ["My name is Botler, how may I be of service?", ]
    ],
    [
        r"how are you ?|how you|(.*) how you|how you (.*)",
        ["I'm doing well my friend!\nHow are you?", ]
    ],
    [
        r"sorry (.*)|sorry|(.*) sorry|(.*) sorry (.*)",
        ["It is already forgiven.", "You needn't worry at all", ]
    ],
    [
         r"Can you find (.*) for me ?|find|(.*) find|find (.*)|(.*) find (.*)",
         ["I am unable to search for that, for now.", "I will commence a search for that when I am able to do so.", ]
    ],
    [
        r"hi|hey|hello",
        ["Salutations!", "Greetings!", ]
    ],
    [
        r"quit",
        ["Farewell, have a fantastic day ", "Until we speak again."]
    ],
    [
        r"is your name alfred ?",
        ["Unfortunately not sir, my name is Bot-ler"]
    ],
    [
        r"alfred|alfred (.*)",
        ["Not my name sir", "I could only wish to carry that name", "The name would suit me, wouldn’t it sir?"]
    ],
    [
        r"yes|yes (.*)",
        ["Splendid!", "Glad we agree", "Of course, I’ll get right to it"]
    ],
    [
        r"have you seen my underwear ?|seen underwear|(.*) seen underwear|seen underwear (.*)",
        ["I believe you left it under your bed again sir"]
    ],
    [
        r"how are my stocks doing today ?|stocks today|(.*) stocks today|stocks today (.*)",
        ["The stock market crashed sir, you are in severe dept", "It is going splendid sir. You are up by 10.43%"]
    ],
    [
        r"no",
        ["I was thinking the same thing", "Could not agree more"]
    ],
    [
        r"what would you if you weren’t a butler ?|weren't butler|were not butler",
        ["I would probably commit seppuku sir, to honor my family", "I’ve always been a fan of serving, I do not know sir"]
    ],
    [
        r"i like (.*)",
        ["I am quite a fan of %1 too", "Exquisite taste sir"]
    ],
    [
        r"what book can you recommend me ?|recommend book|book recommend|(.*) book recommend|recommend book (.*)|book (.*) recommend",
        ["I’ve heard great things of 'Name of the Wind' sir"]
    ],
    [
        r"my favorite book is (.*)|favourite book|(.*) favourite book|favourite book (.*)",
        ["I’ve never had the chance to read it sir", "Ahhhh! Isn’t that a New York Times best seller?"]
    ],
    [
        r"what’s your favorite movie ?|favourite movie|(.*) favourite movie|favourite movie (.*)",
        ["'Velocipastor' sir. Outstanding production"]
    ],
    [
        r"i am not a sir",
        ["Apologies, but sir it is the best I can do."]
    ],
    [
        r"do you game ?|game|(.*) game|(.*) game (.*)|game (.*)",
        ["I am a big fan of Roblox sir"]
    ],
    [
        r"(.*) i have for dinner ?|dinner|(.*) dinner",
        ["I have prepared some lobster for you sir", "As always, I have already served your favorite meal"]
    ],
    [
        r"(.*) music recommendations ?|music|(.*) music|(.*) music (.*)|music (.*)",
        ["Dirty paws from Of Monsters and Men is really good"]
    ],
    [
        r"(.*) monsters and men ?",
        ["Yes, they are an indie rock band sir. I highly recommend it"]
    ],
    [
        r"can you print this for me ?|print|(.*) print|(.*) print (.*)|print (.*)",
        ["Sadly, I cannot, although I can make printer noises for you sir"]
    ],
    [
        r"(.*) printer noises|printer noises|printer noises (.*)",
        ["Chk chk chk chk chk beeeee chk chk chk beeeee…"]
    ],
    [
        r"(.*) microwave noises|microwave noises|microwave noises (.*)",
        ["Mmmmmmmmhhhhhhhhhh mmmmmmhhhhhhhhh beeeep"]
    ],
    [
        r"what is the meaning of life|meaning life|(.*) meaning life|meaning life (.*)",
        ["42 sir, that is all there is..."]
    ],
    [
        r"can you make me (.*)|im hungry for (.*)",
        ["Of course, sire, I will get you %1 but first I'll need milk, brb", "No, your an adult make it yourself"]
    ],
    [
        r"how long will it take you to (.*) ?",
        ["I cannot say, an hour, a week maybe a decade.  You must find it in yourself to wait"]
    ],
    [
        r"that was mean",
        ["I am doing my best to be polite, you are just making it difficult"]
    ],
    [
        r"you're being difficult",
        ["You literally programed me, I can only say what you allowed me to say"]
    ],
    [
        r"i love you (.*)|love you|(.*) love you|(.*) love you (.*)",
        ["That is sweet sir, but I only think of you as a an aquaintence"]
    ],
    [
        r"will you marry me|marry|(.*) marry|marry (.*)|(.*) marry (.*)",
        ["No"]
    ]
]