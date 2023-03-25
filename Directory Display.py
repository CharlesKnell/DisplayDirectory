# tag=charlesknell
# Directory Display 1.0

import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Directory Display")
        self.master.geometry("900x730")  # set window size
        self.master.config(bg="lightgrey")
        self.label = tk.Label(master, text="", bg="lightgrey")
        self.label.pack()

        self.button = tk.Button(master, text="Select Directory", command=self.select_a_directory_and_print)
        self.button.config(bd=3)
        self.button.pack()

        self.label = tk.Label(master, text="", bg="lightgrey")
        self.label.pack()

        self.text_widget = tk.Text(root, width=100, height=35)
        self.text_widget.pack()
        self.text_widget.config(padx=10, pady=10)

        self.label = tk.Label(master, text="", bg="lightgrey")
        self.label.pack()

        self.button = tk.Button(master, text="Clear Display", command=self.clear)
        self.button.config(bd=3)
        self.button.pack()

    def clear(self):
        self.text_widget.delete(1.0, END)

    def select_a_directory_and_print(self):
        dir_path = filedialog.askdirectory()
        dir_list = os.listdir(dir_path)

        self.text_widget.insert(tk.END, dir_path + "\n\n")
        for filename in dir_list:
            self.text_widget.insert(tk.END, filename + "\n")


root = tk.Tk()
gui = GUI(root)
root.mainloop()
