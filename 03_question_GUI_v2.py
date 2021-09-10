from tkinter import *
from random import shuffle # for randomising the order of the questions

# list of questions
def question_1():
    global title
    global answers
    global answer_results
    title="how tall is the \naverage minion"
    answers=["50cm","10cm","105cm","99cm"] # correct is 105
    answer_results=[incorrect,incorrect,correct,incorrect]

def question_2():
    global title
    global answers
    global answer_results
    title="what language do \nthe minions speak"
    answers=["minionese","minnish","minionish","spanish"] # correct is minionese
    answer_results=[correct,incorrect,incorrect,incorrect]

def question_3():
    global title
    global answers
    global answer_results
    title="who is the \nsmallest minion"
    answers=["kevin","bob","stuart","phil"] # correct is bob
    answer_results=[incorrect,correct,incorrect,incorrect]

def question_4():
    global title
    global answers
    global answer_results
    title="how many minion \nhairstyles are there"
    answers=["5","2","10","8"] # correct is 5
    answer_results=[correct,incorrect,incorrect,incorrect]

def question_5():
    global title
    global answers
    global answer_results
    title="how many fingers \ndo minions have"
    answers=["4","5","1","3"] # correct is 3
    answer_results=[incorrect,incorrect,incorrect,correct]

def question_6():
    global title
    global answers
    global answer_results
    title="how many minions \nare there"
    answers=["4","1000","578","899"] # correct is 899
    answer_results=[incorrect,incorrect,incorrect,correct]

def question_7():
    global title
    global answers
    global answer_results
    title="who made the \nminions"
    answers=["disney","illumination","pixar","treyarch"] # correct is illumination
    answer_results=[incorrect,correct,incorrect,incorrect]

def question_8():
    global title
    global answers
    global answer_results
    title="which is not \na minion's name"
    answers=["tony","lance","norbert","leon"] # correct is leon
    answer_results=[incorrect,incorrect,incorrect,correct]

def question_9():
    global title
    global answers
    global answer_results
    title="what year did \nminions come out"
    answers=["2010","2012","2015","2018"] # correct is 2015
    answer_results=[incorrect,incorrect,correct,incorrect]

def question_10():
    global title
    global answers
    global answer_results
    title="who voices the \nminions"
    answers=["pierre coffin","steve carell","adam sandler","michael reeves"] # correct is pierre coffin
    answer_results=[correct,incorrect,incorrect,incorrect]

def question_11():
    global title
    global answers
    global answer_results
    title="what colour are \nthe evil minions"
    answers=["pink","purple","yellow","red"] # correct is purple
    answer_results=[incorrect,correct,incorrect,incorrect]

def question_12():
    global title
    global answers
    global answer_results
    title="how much is \ndespicable me \nworth"
    answers=["3.7 billion","300 million","1.6 trillion","23 billion"] # correct is 3.7 billion
    answer_results=[correct,incorrect,incorrect,incorrect]

def question_13():
    global title
    global answers
    global answer_results
    title="what colour are \nbob's eyes"
    answers=["blue","green and brown","red","blue and red"] # correct is green and brown
    answer_results=[incorrect,correct,incorrect,correct]

def question_14():
    global title
    global answers
    global answer_results
    title="what colour are \nthe minions"
    answers=["yellow","orange","blue","purple"] # correct is yellow
    answer_results=[correct,incorrect,incorrect,incorrect]

def question_15():
    global title
    global answers
    global answer_results
    title="what gender are \nthe minions"
    answers=["mix","female","male","agender"] # correct is male
    answer_results=[incorrect,incorrect,correct,incorrect]

def question_16():
    global title
    global answers
    global answer_results
    title="what do minions \nlove"
    answers=["money","bananas","gru","crystal"] # correct is bananas
    answer_results=[incorrect,correct,incorrect,incorrect]

def question_17():
    global title
    global answers
    global answer_results
    title="what music does \nstaurt play for \nthe queen"
    answers=["national anthem","sex pistols","van halen","the beatles"] # correct is van halen
    answer_results=[incorrect,incorrect,correct,incorrect]

def question_18():
    global title
    global answers
    global answer_results
    title="where does minions \ntake place"
    answers=["england","kansas","minnesota","space"] # correct is england
    answer_results=[correct,incorrect,incorrect,incorrect]

def question_19():
    global title
    global answers
    global answer_results
    title="how old are \nthe minions"
    answers=["100 million years","6 million years","100 years","60 million years"] # correct is 60 mil
    answer_results=[incorrect,incorrect,incorrect,correct]

def question_20():
    global title
    global answers
    global answer_results
    title="who do minions \nserve"
    answers=["evil","good","christ","gru"] # correct is evil
    answer_results=[correct,incorrect,incorrect,incorrect]

# list of questions
questions = [question_1,question_2, question_3, question_4, question_5, question_6, question_7, question_8,
             question_9, question_10, question_11, question_12, question_13, question_14, question_15,
             question_16, question_17, question_18, question_19, question_20]

# give different outputs if the questions is incorrect
def incorrect():
    print("incorrect")

def correct():
    print("correct")


def question_randomiser():
    # randomise the order  of the list
    shuffle(questions)

class Questions:
    def __init__(self):

        # Formatting variables
        background_color = "yellow"

        # Question Main Screen GUI
        self.question_frame = Frame(width=300, height=300,
                              bg=background_color, pady=10)
        self.question_frame.grid()

        # Question Title
        self.question_title = Label(self.question_frame,
                                            text=title,
                                            font=("Arial", "30", "bold"),
                                            bg=background_color,
                                            pady=10, padx=10)
        self.question_title.grid(row=0,sticky='N')

        # Answer Buttons
        self.answer_button_1 = Button(self.question_frame, text=answers[0],
                                      font=("Arial", "20"),
                                      bg="blue",
                                      width=15, command=(answer_results[0]))
        self.answer_button_1.grid(row=1)

        self.answer_button_2 = Button(self.question_frame, text=answers[1],
                                      font=("Arial", "20"),
                                      bg="blue",
                                      width=15, command=(answer_results[1]))
        self.answer_button_2.grid(row=2)

        self.answer_button_3 = Button(self.question_frame, text=answers[2],
                                      font=("Arial", "20"),
                                      bg="blue",
                                      width=15, command=answer_results[2])
        self.answer_button_3.grid(row=3)

        self.answer_button_4 = Button(self.question_frame, text=answers[3],
                                      font=("Arial", "20"),
                                      bg="blue",
                                      width=15, command=answer_results[3])
        self.answer_button_4.grid(row=4)

# main routine
question_randomiser()
questions[0]()

if __name__ == "__main__":
    root = Tk()
    root.title("question")
    something = Questions()
    root.mainloop()
