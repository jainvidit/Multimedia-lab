import Tkinter as Tk

from Runlength.Compression import Run_length_compression_algorithm as RLA
from .. import Run_Length

def run_length_compress():
    def print_content():
        rl_output.delete("1.0",Tk.END)
        rl_output.insert("1.0",RLA.compress(rl_input.get("1.0",Tk.END)))

    def Go_Back():
        compression_window.destroy()
        Run_Length.run_length_menu()

    compression_window = Tk.Tk()
    compression_window.wm_title("Compression : ")
    Tk.Label(compression_window,text="Enter input").grid( row = 0 )


    rl_input=Tk.Text(compression_window,height=5,width=50)#,text="Enter Input")#,textvariable = input_content)
    rl_input.grid(row=1,column=0,padx=10)
    rl_input.insert("1.0","Enter text here")

    input_button=Tk.Button(compression_window,text = "Click to Compress",command=print_content).grid(row=2)

    Tk.Label(compression_window,text="Compressed String is : ").grid( row = 4)
    rl_output=Tk.Text(compression_window,height=5,width=50)
    rl_output.grid(row=5)


    exit_button=Tk.Button(compression_window,text = "Back",command=Go_Back).grid(row=6)

    compression_window.mainloop()
    compression_window.lift()


