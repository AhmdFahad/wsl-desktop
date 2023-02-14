import tkinter as tk
from wslService import listDistribution

distribution_objects=listDistribution()

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Create the GUI
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the list of items
        item_frame = tk.Frame(self)
        item_frame.pack(side="top", fill="both", expand=False)

        # Create a scrollbar for the frame
        scrollbar = tk.Scrollbar(item_frame)
        scrollbar.pack(side="right", fill="y")

        # Create a listbox to display the items
        self.listbox = tk.Listbox(item_frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)

        # Attach the scrollbar to the listbox
        scrollbar.config(command=self.listbox.yview)

        # Add the items to the listbox
        for distribution in distribution_objects:
            self.listbox.insert("end", f"{distribution.name} ({distribution.state}, {distribution.version})")
        # Create a frame for the button
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom")

        # Create a button with two states
        self.button = tk.Button(button_frame, text="", command=self.change_state)
        self.button.pack(side="left")

    def change_state(self):
        if self.button["text"] == "Stopped":
            self.button.config(text="Running")
        else:
            self.button.config(text="Stopped")

if __name__ == "__main__":
    app = App()
    app.mainloop()