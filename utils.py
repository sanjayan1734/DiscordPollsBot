import random

#answers for magic 8-ball
eightball = [
    "It is certain",                         #positve answers
    "Without a doubt",
    "You may rely on it",
    "Yes definitely",
    "It is decidedly so",
    "As I see it, yes",
    "Most likely",
    "Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy try again",                  #nutral answers
    "Better not tell you now",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don’t count on it",                     #negative answers
    "Outlook not so good",
    "My sources say no",
    "Very doubtful",
    "My reply is no"
    ]

#this function chooses a random answer for the 'eightball' list
def eightball_answer():
    answer = random.choice(eightball)
    
    return answer

def check_commandlength(message):
    count = 0
    for word in message:
        count+=1
    if count>1:
        return 1
    else:
        return 0

#checks if the message from the user contains the phrase 'choices' and returns its position
#parameters - list(list of the words of the message/command split using ' ')
def poll_option(message):
    count = 0
    for word  in message :
        count = count + 1
        if word == '-':
            return count

    return count

#id's of different colour reactions 'colour square'
#got the id's from emojipedia
poll_reactions = [
    '🟦',            #blue
    '🟥',            #red
    '🟨',            #yellow
    '🟩',            #green
    '🟪',            #purple
    '🟧',            #orange
    '🟫',            #brown
    '⬛',            #black
    '⬜'             #white
]


