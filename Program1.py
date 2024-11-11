#First GUI Joseph Rydberg 11/11/2024
import tkinter


def open_gui():
    window = tkinter.Tk()
    window.title("GUI")

    label = tkinter.Label(window, text = "A ship in the harbor is safe but that is not what ships are for.")
    label.pack()
    window.mainloop()

open_gui()