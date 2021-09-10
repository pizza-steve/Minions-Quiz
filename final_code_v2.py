from tkinter import *
from random import shuffle # for randomising the order of the questions

# variables
question_number = 0
score = 0

# list of questions with defined answers
def question_1():
    global title
    global answers
    global answer_results
    title="how tall is the \naverage minion"
    answers=["50cm","10cm","105cm","99cm"] # correct is 105
    answer_results=["incorrect","incorrect","correct","incorrect"]

def question_2():
    global title
    global answers
    global answer_results
    title="what language do \nthe minions speak"
    answers=["minionese","minnish","minionish","spanish"] # correct is minionese
    answer_results=["correct","incorrect","incorrect","incorrect"]

def question_3():
    global title
    global answers
    global answer_results
    title="who is the \nsmallest minion"
    answers=["kevin","bob","stuart","phil"] # correct is bob
    answer_results=["incorrect","correct","incorrect","incorrect"]

def question_4():
    global title
    global answers
    global answer_results
    title="how many \nminion hairstyles \nare there"
    answers=["5","2","10","8"] # correct is 5
    answer_results=["correct","incorrect","incorrect","incorrect"]

def question_5():
    global title
    global answers
    global answer_results
    title="how many \nfingers do \nminions have"
    answers=["4","5","1","3"] # correct is 3
    answer_results=["incorrect","incorrect","incorrect","correct"]

def question_6():
    global title
    global answers
    global answer_results
    title="how many \nminions are there"
    answers=["4","1000","578","899"] # correct is 899
    answer_results=["incorrect","incorrect","incorrect","correct"]

def question_7():
    global title
    global answers
    global answer_results
    title="who made the \nminions"
    answers=["disney","illumination","pixar","treyarch"] # correct is illumination
    answer_results=["incorrect","correct","incorrect","incorrect"]

def question_8():
    global title
    global answers
    global answer_results
    title="which is not \na minion's name"
    answers=["tony","lance","norbert","leon"] # correct is leon
    answer_results=["incorrect","incorrect","incorrect","correct"]

def question_9():
    global title
    global answers
    global answer_results
    title="what year did \nminions come \nout"
    answers=["2010","2012","2015","2018"] # correct is 2015
    answer_results=["incorrect","incorrect","correct","incorrect"]

def question_10():
    global title
    global answers
    global answer_results
    title="who voices the \nminions"
    answers=["pierre coffin","steve carell","adam sandler","michael reeves"] # correct is pierre coffin
    answer_results=["correct","incorrect","incorrect","incorrect"]

def question_11():
    global title
    global answers
    global answer_results
    title="what colour are \nthe evil minions"
    answers=["pink","purple","yellow","red"] # correct is purple
    answer_results=["incorrect","correct","incorrect","incorrect"]

def question_12():
    global title
    global answers
    global answer_results
    title="how much is \ndespicable me \nworth"
    answers=["3.7 billion","300 million","1.6 trillion","23 billion"] # correct is 3.7 billion
    answer_results=["correct","incorrect","incorrect","incorrect"]

def question_13():
    global title
    global answers
    global answer_results
    title="what colour \nare bob's eyes"
    answers=["blue","green and brown","red","blue and red"] # correct is green and brown
    answer_results=["incorrect","correct","incorrect","incorrect"]

def question_14():
    global title
    global answers
    global answer_results
    title="what colour are \nthe minions"
    answers=["yellow","orange","blue","purple"] # correct is yellow
    answer_results=["correct","incorrect","incorrect","incorrect"]

def question_15():
    global title
    global answers
    global answer_results
    title="what gender \nare the minions"
    answers=["mix","female","male","agender"] # correct is male
    answer_results=["incorrect","incorrect","correct","incorrect"]

def question_16():
    global title
    global answers
    global answer_results
    title="what do \nminions love"
    answers=["money","bananas","gru","crystal"] # correct is bananas
    answer_results=["incorrect","correct","incorrect","incorrect"]

def question_17():
    global title
    global answers
    global answer_results
    title="what music \ndoes staurt play \nfor the queen"
    answers=["national anthem","sex pistols","van halen","the beatles"] # correct is van halen
    answer_results=["incorrect","incorrect","correct","incorrect"]

def question_18():
    global title
    global answers
    global answer_results
    title="where does \nminions take \nplace"
    answers=["england","kansas","minnesota","space"] # correct is england
    answer_results=["correct","incorrect","incorrect","incorrect"]

def question_19():
    global title
    global answers
    global answer_results
    title="how old are \nthe minions"
    answers=["100 million years","6 million years","100 years","60 million years"] # correct is 60 mil
    answer_results=["incorrect","incorrect","incorrect","correct"]

def question_20():
    global title
    global answers
    global answer_results
    title="who do minions \nserve"
    answers=["evil","good","christ","gru"] # correct is evil
    answer_results=["correct","incorrect","incorrect","incorrect"]

# all the questions in an actual list
questions = [question_1,question_2, question_3, question_4, question_5, question_6, question_7, question_8,
             question_9, question_10, question_11, question_12, question_13, question_14, question_15,
             question_16, question_17, question_18, question_19, question_20]


class Quiz:
    def __init__(self):

        # Quiz Main Screen GUI
        self.quiz_frame = Frame(width=300, height=300,
                                bg="yellow", pady = 10)
        self.quiz_frame.grid()

        # minions quiz heading
        self.minion_label = Label(self.quiz_frame,
                                          text="Minions Quiz",
                                          font=("Arial", "30", "bold"),
                                          bg="yellow",
                                          padx=10, pady=30)
        self.minion_label.grid(row=0,sticky='N')

        # play button
        self.play_button = Button(self.quiz_frame, text="Play",
                                  font=("Arial", "20"),
                                  bg="Blue",
                                  padx=90, pady=10, command=self.play)
        self.play_button.grid(row=1)

    def play(self):
        global questions_tk
        root.destroy() # to close the menu window when the quiz starts
        questions_tk = Tk()
        questions_tk.title("Questions")
        Questions()
        questions_tk.mainloop()



class Questions:
    def __init__(self):

        # function to update the GUI to display the next question up to 10 questions
        def next_question():
            global question_number
            if question_number < 9:
                question_number += 1
                questions[question_number]()
                self.question_title.configure(text=title)
                self.answer_button_1.configure(text=answers[0])
                self.answer_button_2.configure(text=answers[1])
                self.answer_button_3.configure(text=answers[2])
                self.answer_button_4.configure(text=answers[3])
                self.answer_button_1["state"]=NORMAL
                self.answer_button_2["state"]=NORMAL
                self.answer_button_3["state"]=NORMAL
                self.answer_button_4["state"]=NORMAL
                self.answer_button_1.configure(bg="blue")
                self.answer_button_2.configure(bg="blue")
                self.answer_button_3.configure(bg="blue")
                self.answer_button_4.configure(bg="blue")
                self.next_question_button.grid_forget()
            # stop updating questions after 10th questions
            elif question_number >= 9:
                global score_tk
                # Start score code
                questions_tk.destroy()
                score_tk = Tk()
                score_tk.title("Score")
                Score()
                score_tk.mainloop()
        # functions for each button when clicked
        def button_1():
            if answer_results[0]=="correct":
                global score
                score+=1
            show_colours()

        def button_2():
            if answer_results[1]=="correct":
                global score
                score+=1
            show_colours()

        def button_3():
            if answer_results[2]=="correct":
                global score
                score+=1
            show_colours()

        def button_4():
            if answer_results[3]=="correct":
                global score
                score+=1
            show_colours()

        # function to reveal which questions were right and wrong by revealing the colours
        def show_colours():
            if answer_results[0]=="correct":
                self.answer_button_1.configure(bg="green1")
            elif answer_results[0]=="incorrect":
                self.answer_button_1.configure(bg="red")

            if answer_results[1]=="correct":
                self.answer_button_2.configure(bg="green1")
            elif answer_results[1]=="incorrect":
                self.answer_button_2.configure(bg="red")

            if answer_results[2]=="correct":
                self.answer_button_3.configure(bg="green1")
            elif answer_results[2]=="incorrect":
                self.answer_button_3.configure(bg="red")

            if answer_results[3]=="correct":
                self.answer_button_4.configure(bg="green1")
            elif answer_results[3]=="incorrect":
                self.answer_button_4.configure(bg="red")

            # Disable the answer buttons for now
            self.answer_button_1["state"]=DISABLED
            self.answer_button_2["state"]=DISABLED
            self.answer_button_3["state"]=DISABLED
            self.answer_button_4["state"]=DISABLED

            # Reveal the next question button
            self.next_question_button.grid()

        # Question Main Screen GUI
        self.question_frame = Frame(width=300, height=300,
                              bg="yellow", pady=10)
        self.question_frame.grid()

        # Question Title
        self.question_title = Label(self.question_frame,
                                            text=title,
                                            font=("Arial", "30", "bold"),
                                            bg="yellow",
                                            pady=10, padx=10)
        self.question_title.grid(row=0,sticky='N')

        # Answer Buttons
        self.answer_button_1 = Button(self.question_frame, text=answers[0],
                                      font=("Arial", "20"),
                                      bg="blue",
                                      width=15, command=button_1, disabledforeground="black")
        self.answer_button_1.grid(row=1)

        self.answer_button_2 = Button(self.question_frame, text=answers[1],
                                      font=("Arial", "20"),
                                      bg="blue",
                                      width=15, command=button_2, disabledforeground="black")
        self.answer_button_2.grid(row=2)

        self.answer_button_3 = Button(self.question_frame, text=answers[2],
                                      font=("Arial", "20"),
                                      bg="blue",
                                      width=15, command=button_3, disabledforeground="black")
        self.answer_button_3.grid(row=3)

        self.answer_button_4 = Button(self.question_frame, text=answers[3],
                                      font=("Arial", "20"),
                                      bg="blue",
                                      width=15, command=button_4, disabledforeground="black")
        self.answer_button_4.grid(row=4)

        # Button to go to the next question
        self.next_question_button = Button(self.question_frame, text="next question",
                                            font=("Arial","15"),
                                            bg="yellow", command=next_question)
        self.next_question_button.grid(row=5)

        # The button begins hidden until used again later
        self.next_question_button.grid_forget()

class Score:
    def __init__(self):

        # Score Main Screen GUI
        self.score_frame = Frame(width=300, height=300,
                                bg="yellow", pady = 10)
        self.score_frame.grid()

        # Score headings
        self.score_heading_label = Label(self.score_frame,
                                          text="Your final score \nwas:",
                                          font=("Arial", "30", "bold"),
                                          bg="yellow",
                                          padx=10, pady=5)
        self.score_heading_label.grid(row=0,sticky='S')

        self.score_label = Label(self.score_frame,
                                 text=(score,"/10"),
                                 font=("Arial", "30", "bold"),
                                 bg="yellow",
                                 padx=10)
        self.score_label.grid(row=1)

        # button to launch the export GUI
        self.open_export_button = Button(self.score_frame,
                                        text="export results",
                                        font=("Arial", "20"),
                                        bg="blue",
                                        width=15, command=export_button)
        self.open_export_button.grid(row=3)

        # button to end the code
        self.exit_button = Button(self.score_frame,
                                        text="exit",
                                        font=("Arial", "20"),
                                        bg="blue",
                                        width=15, command=score_tk.destroy)
        self.exit_button.grid(row=4)

# Functions for the export button

def export_button():
    global export_tk
    score_tk.destroy()
    export_tk = Tk()
    export_tk.title("Export results")
    Export()
    export_tk.mainloop()

class Export:
    def __init__(self):

        # Function to export the score to a text file
        def export():
            # to add the .txt extension to the file
            filename = self.export_name.get() + ".txt"
            print("exporting")
            print(filename)
            file = open(filename,"w")
            file.write("your final score on the minions quiz was:\n")
            file.write(str(score))
            file.write("/10\ncongratulations")
            file.close()
            export_tk.destroy()


        # Export Main Screen GUI
        self.export_frame = Frame(width=300, height=300,
                                bg="yellow", pady = 10)
        self.export_frame.grid()

        # export heading
        self.export_label = Label(self.export_frame,
                                          text="Export results",
                                          font=("Arial", "30", "bold"),
                                          bg="yellow",
                                          padx=10, pady=30)
        self.export_label.grid(row=0,sticky='N')

        self.enter_filename_label = Label(self.export_frame,
                                          text="Enter a filename:",
                                          font=("Arial", "15", "bold"),
                                          bg="yellow",
                                          padx=10)
        self.enter_filename_label.grid(row=2,sticky='S')

        # Filename entry box
        self.export_name = Entry(self.export_frame,
                                   font=("Arial", "15"),
                                   bg="white", width=15)
        self.export_name.grid(row=3,sticky='N')

        # Export button
        self.export_button = Button(self.export_frame,
                                    text=("export"),
                                    font=("Arial", "15", "bold"),
                                    bg="blue",
                                    padx=10, pady=5, command=export)
        self.export_button.grid(row=4,sticky='S')


# main routine
shuffle(questions)
questions[question_number]()

root = Tk()
root.title("Main Menu")
Quiz()
root.mainloop()
