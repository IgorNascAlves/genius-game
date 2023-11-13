import tkinter as tk
import random
import time

colors = {
    'red': 0,
    'blue': 90,
    'green': 180,
    'yellow': 270,
}


# Initialize the game
class SimonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Genius Game")
        self.sequence = []
        self.player_sequence = []
        self.level = 1
        self.create_widgets()
        self.show_color()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=300, height=300, background="black")
        self.canvas.pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        self.sequence = []
        self.player_sequence = []
        self.level = 1
        self.play_sequence()

    def play_sequence(self):
        self.root.after(1000)  # Delay for better visualization

        for color in self.sequence:
            self.show_color(color)

        color = random.choice(list(colors.keys()))
        self.sequence.append(color)
        self.show_color(color)
        time.sleep(1)

        print(self.sequence)

        self.show_color()

        self.get_player_input()

    def show_color(self, color_selected=None):
   
        # Define the width of the border
        border_width = 10

        for color in ['red', 'blue', 'green', 'yellow']:
            if color == color_selected:
                self.canvas.create_arc(50 + border_width, 50 + border_width, 250 - border_width, 250 - border_width,
                                       start=colors[color], extent=90, fill=color, outline='white', width=border_width)
            else:
                self.canvas.create_arc(50 + border_width, 50 + border_width, 250 - border_width, 250 - border_width,
                                       start=colors[color], extent=90, fill=color, width=border_width)

        self.root.update()
        time.sleep(0.5)

    def get_player_input(self):
        self.player_sequence = []
        self.canvas.bind("<Button-1>", self.check_color)

    def check_color(self, event):
        x, y = event.x, event.y
        color = self.canvas.itemcget(self.canvas.find_closest(x, y), "fill")
        self.show_color(color)
        self.player_sequence.append(color)
        self.show_color(color)

        if len(self.sequence) == len(self.player_sequence):
            if self.sequence == self.player_sequence:
                print('Correct')
                self.level += 1
                self.canvas.unbind("<Button-1>")
                self.play_sequence()
            else:
                self.canvas.create_text(150, 150, text="Game Over", fill="red", font=("Helvetica", 20))
        
        print(self.sequence)
        print(self.player_sequence)

# Create the main window
root = tk.Tk()
simon_game = SimonGame(root)
root.mainloop()
