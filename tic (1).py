
board = [" " for _ in range(9)]  


def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")
    print("\n")


def check_win():
    
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            return board[combination[0]]
    return None

def check_draw():
    return " " not in board


def play_game():
    current_player = "X"  
    while True:
        print_board()
        print(f"Player {current_player}'s turn")
        
        
        try:
            move = int(input(f"Enter the position (1-9) for {current_player}: ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        
        board[move] = current_player
        
        
        winner = check_win()
        if winner:
            print_board()
            print(f"Player {winner} wins!")
            break
     
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        
       
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
