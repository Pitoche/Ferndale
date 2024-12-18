import tkinter as tk

class LightControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Light Control System")

        # Light states (initially off)
        self.red_light = False
        self.amber_light = False
        self.green_light = False

        # Create labels to represent the lights
        self.red_label = tk.Label(root, text="Red Light", width=20, height=2, bg="gray")
        self.red_label.grid(row=0, column=0)

        self.amber_label = tk.Label(root, text="Amber Light", width=20, height=2, bg="gray")
        self.amber_label.grid(row=1, column=0)

        self.green_label = tk.Label(root, text="Green Light", width=20, height=2, bg="gray")
        self.green_label.grid(row=2, column=0)

        # Create buttons to control the lights (switches)
        self.red_button = tk.Button(root, text="Toggle Red", command=self.toggle_red)
        self.red_button.grid(row=0, column=1)

        self.amber_button = tk.Button(root, text="Toggle Amber", command=self.toggle_amber)
        self.amber_button.grid(row=1, column=1)

        self.green_button = tk.Button(root, text="Toggle Green", command=self.toggle_green)
        self.green_button.grid(row=2, column=1)

    def toggle_red(self):
        """Toggle the Red Light."""
        self.red_light = not self.red_light
        color = "red" if self.red_light else "gray"
        self.red_label.config(bg=color)

    def toggle_amber(self):
        """Toggle the Amber Light."""
        self.amber_light = not self.amber_light
        color = "yellow" if self.amber_light else "gray"
        self.amber_label.config(bg=color)

    def toggle_green(self):
        """Toggle the Green Light."""
        self.green_light = not self.green_light
        color = "green" if self.green_light else "gray"
        self.green_label.config(bg=color)

# Create the main window
root = tk.Tk()

# Create the light control app
app = LightControlApp(root)

# Start the GUI event loop
root.mainloop()