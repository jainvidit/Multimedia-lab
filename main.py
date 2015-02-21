
import Tkinter as Tk
import Run_Length as RL
import tkMessageBox


def main_menu():
    def go_to_problem_1():
        Index.destroy()
        RL.run_length_menu()
    Index = Tk.Tk()
    Index.wm_title("Main Menu")
    Tk.Label(Index,text="Select program to run : ").grid(row=0,column=0,columnspan=3,padx=100,pady=10)

    Prog1_button = Tk.Button(Index,text="Run length Coding",command=go_to_problem_1)
    Prog1_button.grid(row = 2 ,columnspan=3, padx=10,pady=10)

    Index.mainloop()
    Index.lift()

#Start_Screen=0



