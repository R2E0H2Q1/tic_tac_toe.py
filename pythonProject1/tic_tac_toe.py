#Tic Tac oe is played on a 3x3 grid.
"""
As a first step we need to create the board game.
"""
def create_grid():
    return [' ' for _ in range(9)] # This will create a list of 9 spaces.


"""
Then we need to create a  function to display the board.
 """
def display_grid(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

"""
Now we need to make sure that the player doesn't choose an empty place.
"""

def in_player(board):
    while True:
        try:
            move = int(input("Choose a position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid position. Choose a number between 1 and 9.")
            elif board[move] != ' ':
                print("This position is already taken. Try again.")
            else:
                return move
        except ValueError:
            print("Please enter a number.")

""" 
We use a while loop so the program keeps running until the user enters a valid input. 
Changing the board with the moves the player select.
"""

def update_board(board, position, marker):
    board[position] = marker

"""
After the grid is updated, a winner check must be done to see who wins.
"""

def who_won(board, marker):
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal
        [2, 4, 6],  # Diagonal
    ]
    return any(board[x] == board[y] == board[z] == marker for x, y, z in win_conditions)

""" 
    We also need to check if there is a tie. If none succeds, and no more empty spaces remain, is a tie. 
"""

def draw_check(board):
    return ' ' not in board

"""
Now we combine everything into the main game logic.
"""

def start_playing():
    board = create_grid()
    current_player = 'X'

    while True:
        display_grid(board)
        print(f"Player {current_player}'s turn.")

        move = in_player(board)
        update_board(board, move, current_player)

        if who_won(board, current_player):
            display_grid(board)
            print(f"Player {current_player} wins!")
            break

        if draw_check(board):
            display_grid(board)
            print("It's a draw!")
            break

            # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


start_playing()