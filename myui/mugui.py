import tkinter as tk

window = tk.Tk()
window.title("hi good morning")
window.geometry("450x450")
lable = tk.Label(text="Hi",font=("consolas",16))
lable.pack(pady=20)
button = tk.Button(text="god")
button.pack()
window.mainloop()