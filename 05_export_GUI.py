from tkinter import *

# example  score for testing
score=5

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
root = Tk()
root.title("Export Results")
Export()
root.mainloop()
