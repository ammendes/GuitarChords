import tkinter as tk

class GuitarLayout(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.pack()
        self.canvas_width = 600
        self.canvas_height = 300
        self.string_spacing = self.canvas_height / 5
        self.fret_spacing = self.canvas_width / 6
        self.dot_color = "white"
        self.dot_background = "white"
        self.dot_radius = 10  # Radius of the dot
        self.dots = {}  # Store dot IDs
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="#3f1f00", highlightthickness=0)
        self.canvas.pack()

        # Draw frets
        for i in range(7):
            x = i * self.fret_spacing
            self.canvas.create_line(x, 0, x, self.canvas_height, width=8, fill="gray40")

        # Draw strings
        for i in range(6):
            y = i * self.string_spacing + self.string_spacing / 2
            self.canvas.create_line(0, y, self.canvas_width, y, width=2, fill="black")



        # Bind mouse click event to canvas
        self.canvas.bind("<Button-1>", self.toggle_dot)

    def toggle_dot(self, event):
        # Determine string and fret based on click coordinates
        string = int(event.y / self.string_spacing)
        fret = int(event.x / self.fret_spacing)

        # Validate string and fret
        if 0 <= string < 6 and 0 <= fret < 6:
            dot_id = self.dots.get((string, fret))
            if dot_id:
                # Delete the dot
                self.canvas.delete(dot_id)
                del self.dots[(string, fret)]
            else:
                # Create a dot
                x = fret * self.fret_spacing + self.fret_spacing / 2
                y = string * self.string_spacing + self.string_spacing / 2
                dot = self.canvas.create_oval(x - self.dot_radius, y - self.dot_radius, x + self.dot_radius,
                                                y + self.dot_radius, fill=self.dot_color, outline="")
                self.dots[(string, fret)] = dot

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Guitar Fretboard Layout")
    guitar_layout = GuitarLayout(master=root)
    root.mainloop()
