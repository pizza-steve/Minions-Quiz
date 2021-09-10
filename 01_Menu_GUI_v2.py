from tkinter import *


class Quiz:
    def __init__(self):
        # formatting variables
        background_color = "yellow"

        # quiz main screen GUI
        self.quiz_frame = Frame(width=300, height=400, bg=background_color)
        self.quiz_frame.grid()

        # minions quiz heading
        self.minion_label = Label(text="Minions Quiz",
                                            font=("Arial", "30", "bold"),
                                            bg=background_color,
                                            padx=10,pady=10,)
        self.minion_label.grid(row=0,sticky='N')

        # play button
        self.play_button_frame = Frame(self.quiz_frame)
        self.play_button_frame.grid(row=3, pady=10)

        self.play_button = Button(self.play_button_frame,
                                  text="Play", font="Arial 10 bold",
                                  bg="Khaki1", padx=10, pady=10)
        self.play_button.grid(row=0)

        Button(text="Play").grid(row=2)

    def play(self):
        # temporary code to be replace by question randomiser/question GUI
        print("quiz will now start")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Minion Quiz Menu")
    something = Quiz()
    root.mainloop()
