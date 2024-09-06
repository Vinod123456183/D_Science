import random

def is_win(player, opponent):
    return  (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")    
    if user not in ['r', 'p', 's']:
        return "Invalid choice. Please choose 'r' for rock, 'p' for paper, or 's' for scissors."
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s a tie!'
    elif is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost!'
print(play())

# computer = random.choice(['1' , '2' , 55])
# print(computer)
