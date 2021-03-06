import Tkinter as Tk

from Runlength.Compression import Run_length_compression as RLC
#import Main_Menu


def run_length_menu():
    flag_run_length_menu= True
    while flag_run_length_menu:
        global flag_run_length_menu
        flag_run_length_menu = True
        def go_to_compression():
            Run_length_window.destroy()
            RLC.run_length_compress()
        def go_to_decompression():
            Run_length_window.destroy()
        def go_home():
            Run_length_window.destroy()
            global flag_run_length_menu
            flag_run_length_menu = False
 #       Main_Menu.main_menu()

        Run_length_window = Tk.Tk()
        Run_length_window.wm_title("Run Length Menu")
        Tk.Label(Run_length_window,text="Select option : ").grid(row=0,columnspan=3)
        compression_button = Tk.Button(Run_length_window,text="Run length Compression",command=go_to_compression)
        compression_button.grid(row = 2 ,columnspan=3, padx=10,pady=10)

        decompression_button = Tk.Button(Run_length_window,text="Run length Decompression",command=go_to_decompression)
        decompression_button.grid(row = 3 ,columnspan=3, padx=10,pady=10)

        home_button=Tk.Button(Run_length_window,text = "Home",command=go_home)
        home_button.grid(row = 6 ,columnspan=4, padx=10,pady=10)

        Run_length_window.mainloop()
       # Run_length_window.lift()