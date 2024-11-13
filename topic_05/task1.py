import random

def getUserSign():
    while True:
        sign = input("Choose sign (rock, scissor, paper): ").lower()
        if sign in ['rock', 'scissor', 'paper']:
            return sign
        else:
            print("Unknown sign, please try again.")

def getComputerSign():
    return random.choice(['rock', 'scissor', 'paper'])

def determineWinner(user_sign, computer_sign):
    if user_sign == computer_sign:
        return "No winners"
    elif (user_sign == 'rock' and computer_sign == 'scissor') or \
         (user_sign == 'scissor' and computer_sign == 'paper') or \
         (user_sign == 'paper' and computer_sign == 'rock'):
        return "You won"
    else:
        return "Computer won"

def gameProcedure():
    user_sign = getUserSign()
    computer_sign = getComputerSign()
    result = determineWinner(user_sign, computer_sign)
    print(f"Your choice: {user_sign}")
    print(f"Computer's choice: {computer_sign}")
    print(result)
gameProcedure()
