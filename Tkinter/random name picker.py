import tkinter as tk
import random

class RandomNamePickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Name Picker")
        self.students = ["karthik","nikhil","leela","vedanta","vignesh"]  # List of students

        self.random_name_var = tk.StringVar()
        self.completed_names = []

        self.create_widgets()

    def create_widgets(self):
        # Frame for the main content
        main_frame = tk.Frame(self.master, bg="#f0f0f0")
        main_frame.pack(pady=20)

        # Frame to display the random name and pick button
        random_frame = tk.Frame(main_frame, bg="#f0f0f0")
        random_frame.pack(side=tk.LEFT, padx=10)

        # Label to display the randomly generated name
        self.random_name_label = tk.Label(random_frame, textvariable=self.random_name_var, font=("Helvetica", 18), bg="#f0f0f0")
        self.random_name_label.pack(pady=10)

        # Button to pick a random name
        self.pick_random_button = tk.Button(random_frame, text="Pick Random Name", command=self.pick_random_name)
        self.pick_random_button.pack()

        # Frame to display completed names
        completed_frame = tk.Frame(main_frame, bg="#f0f0f0")
        completed_frame.pack(side=tk.LEFT, padx=10)

        completed_label = tk.Label(completed_frame, text="Completed Names:", font=("Helvetica", 14), bg="#f0f0f0")
        completed_label.pack()

        self.completed_names_text = tk.Text(completed_frame, height=10, width=20, font=("Helvetica", 12))
        self.completed_names_text.pack()

    def pick_random_name(self):
        if self.students:
            # Pick a random name from the list
            random_name = random.choice(self.students)
            self.random_name_var.set(random_name)

            # Remove the name from the list of students
            self.students.remove(random_name)

            # Add the name to the completed names section
            self.completed_names.append(random_name)
            self.update_completed_names_display()
        else:
            self.random_name_var.set("No more names left!")

    def update_completed_names_display(self):
        # Clear the text widget
        self.completed_names_text.delete(1.0, tk.END)

        # Update the text widget with completed names
        for name in self.completed_names:
            self.completed_names_text.insert(tk.END, name + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = RandomNamePickerApp(root)
    root.mainloop()
