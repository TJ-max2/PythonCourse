import tkinter as tk
from tkinter import messagebox
from typing import List, Tuple


#main class that handles the game logic and GUI
class ConnectFourGUI:
    def __init__(self, master):
        #initialize main window
        self.master = master
        self.master.title("Connect Four")

        #game variables
        self.players = ['Red', 'Yellow']
        self.current_player = 0
        self.board = [['' for _ in range(7)] for _ in range(6)]
        
        #buttons for columns
        self.buttons = []
        for col in range(7):
            button = tk.Button(master, text=f'{col+1}', command=lambda c=col: self.make_move(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)
        
        #game board canvas
        self.canvas = tk.Canvas(master, width=700, height=600, bg='blue')
        self.canvas.grid(row=1, columnspan=7)

        #displays the players turn
        self.turn_label = tk.Label(master, text=f"{self.players[self.current_player]}'s turn", font=('Arial', 16))
        self.turn_label.grid(row=2, columnspan=7)

        #initial empty board
        self.draw_board()
    

    #initializes empty board
    def draw_board(self):
        for row in range(6):
            for col in range(7):
                x1, y1 = col * 100 + 10, row * 100 + 10
                x2, y2 = x1 + 80, y1 + 80
                self.canvas.create_oval(x1, y1, x2, y2, fill='white', outline='black')
    
    #handles players moves when column button clicked
    def make_move(self, col: int):
        for row in range(5, -1, -1): #start from the bottom of the column
            if self.board[row][col] == '':
                #places piece
                self.board[row][col] = self.players[self.current_player]
                self.draw_piece(row, col)

                #check for win or draw
                if self.check_win(row, col):
                    messagebox.showinfo("Game Over", f"{self.players[self.current_player]} wins!")
                    self.reset_game()
                elif self.is_board_full():
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.reset_game()
                else:
                    #switch to other player
                    self.current_player = 1 - self.current_player
                    self.update_turn_label()
                return
        messagebox.showwarning("Invalid Move", "This column is full!")
    

    #colored cirlce drawn to rep player's move
    def draw_piece(self, row: int, col: int):
        x = col * 100 + 50
        y = row * 100 + 50
        color = self.players[self.current_player].lower()
        self.canvas.create_oval(x-40, y-40, x+40, y+40, fill=color, outline='black')
    

    #checks for win condition after each move
    def check_win(self, row: int, col: int) -> bool:
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)] #checks horizontal, vertical, and diagonal
        for dr, dc in directions:
            if self.count_consecutive(row, col, dr, dc) + self.count_consecutive(row, col, -dr, -dc) - 1 >= 4:
                return True
        return False
    
    #counts the consecutive pieces of the same color
    def count_consecutive(self, row: int, col: int, dr: int, dc: int) -> int:
        player = self.board[row][col]
        count = 0
        while 0 <= row < 6 and 0 <= col < 7 and self.board[row][col] == player:
            count += 1
            row += dr
            col += dc
        return count
    
    #checks if board is full
    def is_board_full(self) -> bool:
        return all(self.board[0][col] != '' for col in range(7))
    
    #resets game 
    def reset_game(self):
        self.board = [['' for _ in range(7)] for _ in range(6)]
        self.current_player = 0
        self.canvas.delete("all")
        self.draw_board()
        self.update_turn_label()

    #updates player's turn
    def update_turn_label(self):
        self.turn_label.config(text=f"{self.players[self.current_player]}'s turn")

#main window and start of game
def main():
    root = tk.Tk()
    game = ConnectFourGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()