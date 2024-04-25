import tkinter as tk
import random

window = tk.Tk()
window.geometry("300x300")
window.title("FIRST WINDOW")
label = tk.Label(window, text="First Label", font=("Ariel", 20), bg="green")
label.pack()


def random_generator():
  r = random.randint(1, 1000)
  label = tk.Label(window, text=r, font=("Arial", 20), bg="blue")
  label.pack()


button = tk.Button(window,
                   text="click",
                   font=("Arial", 20),
                   command=random_generator)
button.pack()
window.mainloop()
