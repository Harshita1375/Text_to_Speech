import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text To Speech")
root.geometry("900x450")
root.resizable(False, False)
root.config(bg="blue")

icn_img = PhotoImage(file=r"C:\Users\Lenovo\Desktop\sp1.png")
root.iconphoto(False, icn_img)

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combo.get()
    speed = speed_combo.get()
    voices = engine.getProperty("voices")

    if gender == "Male":
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)

    if text:
        if speed == "FAST":
            engine.setProperty("rate", 250)
        elif speed == "NORMAL":
            engine.setProperty('rate', 150)
        else:
            engine.setProperty("rate", 60)

        engine.say(text)
        engine.runAndWait()


def download():
    print("Download functionality to be implemented.")

top_frame = Frame(root, bg="cyan", width=900, height=80)
top_frame.place(x=0, y=0)

Label(top_frame, text="Text To Speech", font="arial 28 bold",bg="white", fg="black").place(x=300, y=20)

text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=5, y=150, width=440, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="yellow", fg="white").place(x=520, y=160, width=80, height=20)
Label(root, text="SPEED", font="arial 15 bold", bg="yellow", fg="white").place(x=730, y=160, width=80, height=20)

gender_combo = Combobox(root, values=["Male", "Female"], font="arial 14", state="r", width=10)
gender_combo.place(x=520, y=200)
gender_combo.set("Male")

speed_combo = Combobox(root, values=["FAST", "NORMAL", "SLOW"], font="arial 14", state="r", width=10)
speed_combo.place(x=730, y=200)
speed_combo.set("NORMAL")


btn = Button(root, text="Speak", compound=LEFT, width=130, bg="red", font="arial 14 bold", command=speaknow)
btn.place(x=600, y=270, width=200, height=60)

root.mainloop()
