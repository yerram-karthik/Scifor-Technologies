import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import winsound
from threading import Thread
from tkinter import messagebox

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Alarm Clock")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Set Alarm Time", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()
        self.second_var = tk.StringVar()

        ttk.Label(frame, text="Hour:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10)
        ttk.Entry(frame, textvariable=self.hour_var, font=("Helvetica", 12)).grid(row=1, column=1, padx=10)

        ttk.Label(frame, text="Minute:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10)
        ttk.Entry(frame, textvariable=self.minute_var, font=("Helvetica", 12)).grid(row=2, column=1, padx=10)

        ttk.Label(frame, text="Second:", font=("Helvetica", 12)).grid(row=3, column=0, padx=10)
        ttk.Entry(frame, textvariable=self.second_var, font=("Helvetica", 12)).grid(row=3, column=1, padx=10)

        set_button = ttk.Button(frame, text="Set Alarm", command=self.set_alarm, style="TButton")
        set_button.grid(row=4, column=0, columnspan=3, pady=10)

    def set_alarm(self):
        try:
            selected_hour = int(self.hour_var.get())
            selected_minute = int(self.minute_var.get())
            selected_second = int(self.second_var.get())

            now = datetime.now()
            alarm_time = datetime(now.year, now.month, now.day, selected_hour, selected_minute, selected_second)

            if alarm_time <= now:
                alarm_time += timedelta(days=1)

            time_difference = alarm_time - now
            seconds_until_alarm = time_difference.total_seconds()

            self.root.after(int(seconds_until_alarm * 1000), self.show_alarm_message)

        except ValueError:
            self.show_error_message("Invalid input. Please enter valid numbers for hours, minutes, and seconds.")

    def show_alarm_message(self):
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        tk.messagebox.showinfo("Alarm", "Time's up! It's time to wake up!")

    def show_error_message(self, message):
        tk.messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    root.style = ttk.Style()
    root.style.configure("TButton", font=("Helvetica", 12))
    alarm_clock = AlarmClock(root)
    root.mainloop()
