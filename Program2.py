#Info Button Joseph Rydberg 11/11/2024
import tkinter


def gui():
    def show():
        info = tkinter.Label(window, text="Name: Joseph Rydberg, Address: 10682 38th circle NE")
        info.pack()

    window = tkinter.Tk()
    window.title("Information")

    button1 = tkinter.Button(window, text = "Display Information", command = show)
    button2 = tkinter.Button(window, text = "Close", command = window.destroy)
    button1.pack()
    button2.pack()

    window.mainloop()

gui()