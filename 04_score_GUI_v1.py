from tkinter import *

# Example score value for testing
score = 7

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
                                        width=15, command=export)
        self.open_export_button.grid(row=3)

        # button to end the code
        self.exit_button = Button(self.score_frame,
                                        text="exit",
                                        font=("Arial", "20"),
                                        bg="blue",
                                        width=15, command=root.destroy)
        self.exit_button.grid(row=4)

# functions for the export button that will be working in the final code
def export():
    print("export results")
    root.destroy()




# main routine
root = Tk()
root.title("Score")
Score()
root.mainloop()
