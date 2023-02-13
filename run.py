import random
import sys


board = [' ' for x in range(9)]
player_name = input("Enter your name: ").strip()

player_wins = 0
computer_wins = 0
ties = 0

print("\nWelcome to Tic-Tac-Toe, " + player_name + "!\n")
print("The rules of the game are as follows:\n")
print("1. The game is played on a 3x3 grid.")
print("2. You will be 'X' and the computer will be 'O'.")
print("3. To make a move, enter a number from 1 to 9.")
print("4. The numbers correspond to the positions on the grid as follows:\n")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")
print("\n5. The first player to get three of their \nsymbols in a row (horizontally, vertically, \nor diagonally) wins the game.")
print("6. If all the cells on the grid are filled and \nno player has won, the game ends in a draw.")
input("\nPress Enter to start playing: ")


def print_board():
    print("")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("")


def print_scoreboard():
    print("\nScoreboard: ")
    print(player_name + ": " + str(player_wins) + " wins")
    print("Computer: " + str(computer_wins) + " wins")
    print("Ties: " + str(ties) + "\n")

def player_move(icon):
    while True: 
        try:
            choice = input("To leave the game type 'exit' \n\nEnter your move (1-9): ").strip()
            if choice == 'exit':
                print("Thanks for playing Tic-Tac-Toe! Have a great day.")
                sys.exit()
            else:
                choice = int(choice) - 1
                if choice >= 0 and choice <= 8:
                    if board[choice] == ' ':
                        board[choice] = icon
                        break
                    else:
                        print("\nSpace already taken, try again.")
                else:
                    print("\nInvalid choice, try again.")
        except ValueError:
            print("\nInvalid input, try again.")

def is_victory(icon):
    for i in range(3):
        if board[i*3] == icon and board[i*3 + 1] == icon and board[i*3 + 2] == icon:
            return True
        if board[i] == icon and board[i + 3] == icon and board[i + 6] == icon:
            return True
    if board[0] == icon and board[4] == icon and board[8] == icon:
        return True
    if board[2] == icon and board[4] == icon and board[6] == icon:
        return True
    return False

def is_draw():
    for i in range(9):
        if board[i] == ' ':
            return False
    return True

def computer_move(icon):
    while True:
        choice = random.randint(0, 8)
        if board[choice] == ' ':
            board[choice] = icon
            break


while True:
    print_board()
    print_scoreboard()
    player_move('X')
    if is_victory('X'):
        print_board()
        print("X wins! Congratulations " + player_name + "!")
        player_wins += 1
        if player_wins == 5:
            print("\n" + player_name + " has won the game by 5 points! Congratulations!")
            break
        board = [' ' for x in range(9)]
    elif is_draw():
        print_board()
        print("It's a draw")
        ties += 1
        if ties == 5:
            print("\nThe game has ended in a draw by 5 ties.")
            break
        board = [' ' for x in range(9)]
    else:
        computer_move('O')
        if is_victory('O'):
            print_board()
            print("O wins! Better luck next time " + player_name + ".")
            computer_wins += 1
            if computer_wins == 5:
                print("\nThe computer has won the game by 5 points.")
                break
            board = [' ' for x in range(9)]
