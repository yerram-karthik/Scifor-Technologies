import tkinter as tk
from tkinter import StringVar

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    address = address_text.get("1.0", "end-1c")  
    email = email_entry.get()
    contact_no = contact_entry.get()
    country = country_entry.get()
    state = state_entry.get()

    diseases = []
    if cold_var.get():
        diseases.append("Cold")
    if cough_var.get():
        diseases.append("Cough")
    if fever_var.get():
        diseases.append("Fever")
    if headache_var.get():
        diseases.append("Headache")

    
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Address:", address)
    print("Email:", email)
    print("Contact No:", contact_no)
    print("Country:", country)
    print("State:", state)
    print("Selected Diseases:", diseases)


root = tk.Tk()
root.title("COVID Vaccine Registration Form")
root.geometry("500x600")

padding_y = 5
padding_x = 10

tk.Label(root, text="Name of the visitor:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age of the visitor:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Gender:").pack()
gender_var = StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Label(root, text="Address:").pack()
address_text = tk.Text(root, height=5, width=30)
address_text.pack()

tk.Label(root, text="Email Id:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Contact No:").pack()
contact_entry = tk.Entry(root)
contact_entry.pack()

tk.Label(root, text="Country:").pack()
country_entry = tk.Entry(root)
country_entry.pack()

tk.Label(root, text="State:").pack()
state_entry = tk.Entry(root)
state_entry.pack()

tk.Label(root, text="SELECT If you are having any following disease:").pack()

cold_var = tk.BooleanVar()
tk.Checkbutton(root, text="Cold", variable=cold_var).pack()

cough_var = tk.BooleanVar()
tk.Checkbutton(root, text="Cough", variable=cough_var).pack()

fever_var = tk.BooleanVar()
tk.Checkbutton(root, text="Fever", variable=fever_var).pack()

headache_var = tk.BooleanVar()
tk.Checkbutton(root, text="Headache", variable=headache_var).pack()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()