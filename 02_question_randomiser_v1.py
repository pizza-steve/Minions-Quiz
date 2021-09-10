from random import shuffle # for shuffling the list of questions

# list of questions with answers
def question_1():
    global title
    global answers
    title="how tall is the average minion"
    answers=["50cm","10cm","105cm","99cm"] # correct is 105
    print("question 1")

def question_2():
    global title
    global answers
    title="what language do the minions speak"
    answers=["minionese","minnish","minionish","spanish"] # correct is minionese
    print("question 2")

def question_3():
    global title
    global answers
    title="who is the smallest minion"
    answers=["kevin","bob","stuart","phil"] # correct is bob
    print("question 3")

def question_4():
    global title
    global answers
    title="how many minion hairstyles are there"
    answers=["5","2","10","8"] # correct is 5
    print("question 4")

def question_5():
    global title
    global answers
    title="how many fingers do minions have"
    answers=["4","5","1","3"] # correct is 3
    print("question 5")

def question_6():
    global title
    global answers
    title="how many minions are there"
    answers=["4","1000","578","899"] # correct is 899
    print("question 6")

def question_7():
    global title
    global answers
    title="who made the minions"
    answers=["disney","illumination","pixar","treyarch"] # correct is illumination
    print("question 7")

def question_8():
    global title
    global answers
    title="which is not a minion's name"
    answers=["tony","lance","norbert","leon"] # correct is leon
    print("question 8")

def question_9():
    global title
    global answers
    title="what year did minions come out"
    answers=["2010","2012","2015","2018"] # correct is 2015
    print("question 9")

def question_10():
    global title
    global answers
    title="who voices the minions"
    answers=["pierre coffin","steve carell","adam sandler","michael reeves"] # correct is pierre coffin
    print("question 10")

def question_11():
    global title
    global answers
    title="what colour are the evil minions"
    answers=["pink","purple","yellow","red"] # correct is purple
    print("question 11")

def question_12():
    global title
    global answers
    title="how much is the despicable me franchise worth"
    answers=["3.7 billion","300 million","1.6 trillion","23 billion"] # correct is 3.7 billion
    print("question 12")

def question_13():
    global title
    global answers
    title="what colour are bob's eyes"
    answers=["blue","green and brown","red","blue and red"] # correct is green and brown
    print("question 13")

def question_14():
    global title
    global answers
    title="what colour are the minions"
    answers=["yellow","orange","blue","purple"] # correct is yellow
    print("question 14")

def question_15():
    global title
    global answers
    title="what gender are the minions"
    answers=["mix","female","male","agender"] # correct is male
    print("question 15")

def question_16():
    global title
    global answers
    title="what do minions love"
    answers=["money","bananas","gru","crystal"] # correct is bananas
    print("question 16")

def question_17():
    global title
    global answers
    title="what music does staurt play for the queen"
    answers=["god save the queen","sex pistols","van halen","the beatles"] # correct is van halen
    print("question 17")

def question_18():
    global title
    global answers
    title="where does minions take place"
    answers=["england","kansas","minnesota","space"] # correct is england
    print("question 18")

def question_19():
    global title
    global answers
    title="how old are the minions"
    answers=["100 million years","6 million years","100 years","60 million years"] # correct is 60 mil
    print("question 19")

def question_20():
    global title
    global answers
    title="who do minions serve"
    answers=["evil","good","christians","gru"] # correct is evil
    print("question 20")

# questions in a list
questions = [question_1,question_2, question_3, question_4, question_5, question_6, question_7, question_8,
             question_9, question_10, question_11, question_12, question_13, question_14, question_15,
             question_16, question_17, question_18, question_19, question_20]

def question_randomiser():
    # randomise the order of the list
    shuffle(questions)

# main routine
question_randomiser()

# for testing purposes
questions[0]()
print(title)
for x in answers:
    print(x)

