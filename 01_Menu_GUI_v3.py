from tkinter import *

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
        # temporary code to be replaced by the questions GUI
        print("question randomiser/question gui")
        root.destroy() # to close the menu window when the quiz starts


# main routine
root = Tk()
root.title("Main Menu")
Quiz()
root.mainloop()
