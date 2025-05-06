# This file is intentionally left blank.
import random
import os

class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_cells = [(r, c) for r in range(4) for c in range(4) if self.board[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.board[r][c] = 2 if random.random() < 0.9 else 4

    def slide_and_merge(self, row):
        new_row = [num for num in row if num != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                self.score += new_row[i]
                new_row[i + 1] = 0
        new_row = [num for num in new_row if num != 0]
        return new_row + [0] * (4 - len(new_row))

    def move(self, direction):
        if direction == 'w':  # Up
            self.board = [list(row) for row in zip(*self.board)]
            self.board = [self.slide_and_merge(row) for row in self.board]
            self.board = [list(row) for row in zip(*self.board)]
        elif direction == 's':  # Down
            self.board = [list(row) for row in zip(*self.board)]
            self.board = [self.slide_and_merge(row[::-1])[::-1] for row in self.board]
            self.board = [list(row) for row in zip(*self.board)]
        elif direction == 'a':  # Left
            self.board = [self.slide_and_merge(row) for row in self.board]
        elif direction == 'd':  # Right
            self.board = [self.slide_and_merge(row[::-1])[::-1] for row in self.board]
        else:
            return False
        self.add_new_tile()
        return True

    def is_game_over(self):
        for row in self.board:
            if 0 in row:
                return False
        for r in range(4):
            for c in range(4):
                if c < 3 and self.board[r][c] == self.board[r][c + 1]:
                    return False
                if r < 3 and self.board[r][c] == self.board[r + 1][c]:
                    return False
        return True

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Score: {self.score}")
        for row in self.board:
            print("+----" * 4 + "+")
            print("".join(f"|{num:^4}" if num != 0 else "|    " for num in row) + "|")
        print("+----" * 4 + "+")

def main():
    game = Game2048()
    while not game.is_game_over():
        game.display_board()
        move = input("Enter move (w/a/s/d): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            game.move(move)
        else:
            print("Invalid move. Use 'w', 'a', 's', or 'd'.")
    game.display_board()
    print("Game Over!")

if __name__ == "__main__":
    main()