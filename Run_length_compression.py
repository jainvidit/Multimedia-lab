import Tkinter as Tk

def RL_compress():
    def prin():
        print input_content.get()
    compression_window = Tk.Tk()
    compression_window.geometry("400X400")
    compression_window.wm_title("Compression : ")
    Tk.Label(compression_window,text="Enter input").grid(row = 0 )


    input_content = Tk.StringVar()
    rl_input=Tk.Entry(compression_window,text="Enter aInput",textvariable = input_content,height=50,width= 50)
    rl_input.grid(row=1,column=0)
    rl_input.insert(0,"Enter text here")

    input_button=Tk.Button(compression_window,text = "Click to decompress",command=prin).grid(row=2)

    compression_window.mainloop()
RL_compress()

def analyze(event=None):
    content = entry_contents.get()
    if content == "":
        entry_contents.set("default")

lord = Tk.Tk()

entry_contents = Tk.StringVar()
aEntry = Tk.Entry(lord, textvariable=entry_contents)
aEntry.grid()

aText = Tk.Text(lord, font=("Georgia", "12"))
aText.grid()

aEntry.bind("<FocusOut>", analyze)

lord.mainloop()
