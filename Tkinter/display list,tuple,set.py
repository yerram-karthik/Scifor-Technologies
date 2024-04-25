import tkinter as tk


def display_data():
  selected_type = data_type_var.get()
  if selected_type == "List":
    result_label.config(text=f"Selected List: {my_list}")
  elif selected_type == "Set":
    result_label.config(text=f"Selected Set: {my_set}")
  elif selected_type == "Tuple":
    result_label.config(text=f"Selected Tuple: {my_tuple}")


window = tk.Tk()
window.geometry("400x400")
window.title("Data Types Example")

data_type_var = tk.StringVar()
data_type_var.set("List")

my_list = [1, 2, 3, 4, 5]
my_set = {5, 6, 7, 8, 9}
my_tuple = (10, 11, 12, 13, 14)

list_radio = tk.Radiobutton(window,
                            text="List",
                            variable=data_type_var,
                            value="List")
set_radio = tk.Radiobutton(window,
                           text="Set",
                           variable=data_type_var,
                           value="Set")
tuple_radio = tk.Radiobutton(window,
                             text="Tuple",
                             variable=data_type_var,
                             value="Tuple")

result_label = tk.Label(window, text="", font=("Arial", 16))

submit_button = tk.Button(window,
                          text="Submit",
                          bg="green",
                          command=display_data)

list_radio.pack(anchor=tk.W)
set_radio.pack(anchor=tk.W)
tuple_radio.pack(anchor=tk.W)
submit_button.pack()
result_label.pack()

window.mainloop()
