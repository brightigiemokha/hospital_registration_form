from tkinter import*
import tkinker.messagebox
from tkinter import ttk
import time
import datetime
import random


def main():
    root = TK()
    app = Windowl(root)

class Windowl:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management Systems")
        self.master.geometry('135x750+0+0')
        self.frame = Frame (self.master)
        self.frame.pack()

        
self.LabelTitle =Label(self.frame, text ='hospital Management System', font=('arial',50, 'bold'),bd=20,)
self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

self.Loginframe1 = Frame(self.frame,width=1010,height=300, bd=20,relief='ridge')
self.Loginframe1.grid(row=1, column=0)

self.Loginframe2 = Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
self.Loginframe2.grid(row=2, column=0)

self.Loginframe3 = Frame(self.frame,width=1000,height=200,bd=20,relief='ridge')
self.Loginframe3.grid(row=3, column=0,pady=2)