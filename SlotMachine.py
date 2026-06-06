from random import choice

def spin_items():
    items = ['🍎️','🌎️','🎄️','👙️','☢️','🇧🇩️']
    output = []
    for _ in range(3):
        output.append(choice(items))
    return output

def finances(balance):
    
    play = True
    while play:
        print(f'your balance is {balance}')
        bet_amount = float(input("enter your bet amount: "))
        if 0<bet_amount<= balance:
            output = spin_items()
            print(output)
            play = False
        else:
            print("invalid bet, bet cant be negative or bigger than your balance ")

    if output[0] == output[1] == output[2]:
        print("CONGRATULATIONS NGA!!!!!")
        balance += bet_amount*10
        print(f"Your current balance is {balance}")
    elif output[0] == output[1]: #1st 2nd
        balance += bet_amount*2
        print(f"Your current balance is {balance}")
    elif output[0] == output[2]: #1st 3rd
        balance += bet_amount*2
        print(f"Your current balance is {balance}")
    elif output[1] == output[2]: #2nd 3rd
        balance += bet_amount*2
        print(f"Your current balance is {balance}")
        
    else:
        balance -= bet_amount
        print("phuuuu! u lost XD")
        print(f"Your current balance is {balance}")

    return balance



#just for user choices , play / quit
def main():     
    balance = 100
    print("welcome to slot machine!!")
    while True:
        if balance == 0:
            print("money over, come back later with your wife's money ")
            break
        play = input("press 'y' to play: ").lower()
        if play == "y":
            balance = finances(balance)
        else:
            print("Visit again!")
            break


if __name__ == "__main__":
    main()
