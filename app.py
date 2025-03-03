import random
import tkinter as tk
from tkinter import ttk
from chords import root_options, type_options, form_options

class RandomChordGenerator:
    def __init__(self, master):
        # Initialize the main application window
        self.master = master  # Reference to the main window
        master.title("Random Chord Generator")  # Set the window title
        master.geometry("600x300")  # Set the window size

        # Import predefined lists of root notes, chord types, and chord forms
        self.root_options = root_options
        self.type_options = type_options
        self.form_options = form_options

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
