
import Tkinter as Tk
import Run_length_compression as RLC
import main

def run_length_menu():
    def go_to_compression():
        Run_length_window.destroy()
        RLC.run_length_compress()
    def go_to_decompression():
        Run_length_window.destroy()
    def Go_Home():
        Run_length_window.destroy()
        main.main_menu()

    Run_length_window = Tk.Tk()
    Run_length_window.wm_title("Run Length Menu")
    Tk.Label(Run_length_window,text="Select option : ").grid(row=0,columnspan=3)
    compression_button = Tk.Button(Run_length_window,text="Run length Compression",command=go_to_compression)
    compression_button.grid(row = 2 ,columnspan=3, padx=10,pady=10)

    decompression_button = Tk.Button(Run_length_window,text="Run length Decompression",command=go_to_decompression)
    decompression_button.grid(row = 3 ,columnspan=3, padx=10,pady=10)

    home_button=Tk.Button(Run_length_window,text = "Home",command=Go_Home)
    home_button.grid(row = 6 ,columnspan=4, padx=10,pady=10)

    Run_length_window.mainloop()
    Run_length_window.lift()