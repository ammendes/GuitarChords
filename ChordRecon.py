import random
import tkinter as tk
from tkinter import ttk

class RandomChordGenerator:
    def __init__(self, master):
        # Initialize the main application window
        self.master = master
        master.title("Random Chord Generator")
        master.geometry("300x150")  # Adjusted size for simpler layout

        # Predefined lists of possible values
        self.root_options = ["Ab", "A", "A#", "Bb", "B", "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "Fb", "F", "F#", "Gb", "G", "G#"]
        self.type_options = ["Major", "Minor", "7", "Min7", "Maj7", "5"]
        self.form_options = ["C", "A", "G", "E", "D"]

        # Create and place the "Generate Chord" button
        ttk.Button(master, text="Generate Chord", command=self.generate_chord).pack(pady=20)

        # Create and place the label to display the result
        self.result_label = ttk.Label(master, text="", wraplength=280)
        self.result_label.pack(pady=10)

    def generate_chord(self):
        # Randomly select one item from each list
        random_root = random.choice(self.root_options)
        random_type = random.choice(self.type_options)
        random_form = random.choice(self.form_options)

        # Format and display the result
        result = f"{random_root} {random_type} ({random_form} form)"
        self.result_label.config(text=result)

# Main execution block
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    # Initialize the application
    app = RandomChordGenerator(root)
    # Start the Tkinter event loop
    root.mainloop()
