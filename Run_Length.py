
import Tkinter as Tk
import Run_length_compression as RLC

def run_length_menu():
    def go_to_compression():
        Rl.destroy()
        RLC.RL_compress()
    def go_to_decompression():
        Rl.destroy()

    Rl = Tk.Tk()
    Rl.wm_title("Run Length Menu")
    Tk.Label(Rl,text="Select option : ").grid(row=0,column=0,columnspan=3,padx=100,pady=10)
    compression_button = Tk.Button(Rl,text="Run length Compression",command=go_to_compression)
    compression_button.grid(row = 2 ,columnspan=3, padx=10,pady=10)

    decompression_button = Tk.Button(Rl,text="Run length Decompression",command=go_to_decompression)
    decompression_button.grid(row = 3 ,columnspan=3, padx=10,pady=10)

    Rl.mainloop()