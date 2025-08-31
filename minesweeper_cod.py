import random

Board size and mine count

ROWS = 8 COLS = 8 MINES = 10

Initialize board

board = [[" "] * COLS for _ in range(ROWS)] visible = [[False] * COLS for _ in range(ROWS)]

Place mines

mines = set() while len(mines) < MINES: r = random.randint(0, ROWS - 1) c = random.randint(0, COLS - 1) mines.add((r, c))

Calculate numbers

for r in range(ROWS): for c in range(COLS): if (r, c) in mines: board[r][c] = "*" else: count = 0 for dr in [-1, 0, 1]: for dc in [-1, 0, 1]: if (r + dr, c + dc) in mines: count += 1 board[r][c] = str(count)

Print function

def print_board(): print("   " + " ".join(str(c) for c in range(COLS))) for r in range(ROWS): row_display = [] for c in range(COLS): if visible[r][c]: row_display.append(board[r][c]) else: row_display.append("#") print(f"{r:2} " + " ".join(row_display))

Reveal function

def reveal(r, c): if r < 0 or r >= ROWS or c < 0 or c >= COLS: return if visible[r][c]: return visible[r][c] = True if board[r][c] == "0": for dr in [-1, 0, 1]: for dc in [-1, 0, 1]: if dr != 0 or dc != 0: reveal(r + dr, c + dc)

Game loop

while True: print_board() try: r, c = map(int, input("Enter row and col (e.g. 3 4): ").split()) except: print("Invalid input!") continue

if (r, c) in mines:
    print("BOOM! You hit a mine.")
        break

        reveal(r, c)

        # Check win
        safe_revealed = sum(visible[r][c] for r in range(ROWS) for c in range(COLS) if (r, c) not in mines)
        if safe_revealed == ROWS * COLS - MINES:
            print_board()
                print("Congratulations! You cleared the board!")
                    break

                    