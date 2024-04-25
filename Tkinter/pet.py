import tkinter as tk

class ScreenPetApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Screen Pet")

        self.canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.canvas.pack()

        # Draw initial happy face
        self.draw_happy_face()

        # Bind events
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Double-Button-1>", self.on_double_click)

    def draw_happy_face(self):
        self.canvas.delete("all")  # Clear canvas
        # Draw happy face
        self.canvas.create_oval(50, 50, 250, 250, outline="black", fill="yellow")
        self.canvas.create_oval(100, 100, 120, 120, outline="black", fill="black")  # Left eye
        self.canvas.create_oval(180, 100, 200, 120, outline="black", fill="black")  # Right eye
        self.canvas.create_arc(100, 150, 200, 200, start=180, extent=180, outline="black", style="arc", width=10)  # Smile

    def draw_cheeky_face(self):
        self.canvas.delete("all")  # Clear canvas
        # Draw cheeky face
        self.canvas.create_oval(50, 50, 250, 250, outline="black", fill="yellow")
        self.canvas.create_oval(100, 100, 120, 120, outline="black", fill="black")  # Left eye
        self.canvas.create_oval(180, 100, 200, 120, outline="black", fill="black")  # Right eye
        self.canvas.create_line(150, 170, 150, 190, width=10)  # Tongue

    def on_left_click(self, event):
        self.draw_happy_face()

    def on_double_click(self, event):
        self.draw_cheeky_face()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = ScreenPetApp(root)
    root.mainloop()
