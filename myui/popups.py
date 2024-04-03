import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("hi good morning")
window.geometry("450x450")
lable = tk.Label(text="Hi",font=("consolas",16))
lable.pack(pady=20)

def clicked():
    messagebox.showinfo("hi","you clicked me ")
button = tk.Button(window,text="god",command=clicked)
button.pack()
window.mainloop()