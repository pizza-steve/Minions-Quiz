from tkinter import *


class Quiz:
    def __init__(self):
        # formatting variables
        background_color = "yellow"

        # quiz main screen GUI
        self.quiz_frame = Frame(width=300, height=300, bg=background_color)
        self.quiz_frame.grid()

        # minions quiz heading
        self.minion_converter_label = Label(text="Minions Quiz",
                                            font=("Arial", "30", "bold"),
                                            bg=background_color,
                                            padx=10,pady=10,)
        self.minion_converter_label.grid(row=0,sticky='N')


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Minion Quiz Menu")
    something = Quiz()
    root.mainloop()
