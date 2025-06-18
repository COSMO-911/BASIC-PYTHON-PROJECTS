import random

# Initial balance
balance = 10000

print("🎲 Welcome to the Guess & Win Game!")
print("You have ₹10,000. Guess a number between 1 to 5 and double your bet if correct!\n")

while True:
    if balance <= 0:
        print("\nYou have run out of money! Game Over.")
        restart = input("You lost all your money. Wanna restart the game? (y/n): ").lower()
        if restart == 'y':
            balance = 10000
            print("\nGame restarted with ₹10,000!")
            continue
        else:
            break

    print(f"Current Balance: ₹{balance}")

    try:
        bet = int(input("Enter bet amount: ₹"))
        if bet <= 0 or bet > balance:
            print("Invalid bet amount! Try again.\n")
            continue

        guess = int(input("Guess a number between 1 and 5: "))
        if guess < 1 or guess > 5:
            print("Invalid guess! Must be between 1 and 5.\n")
            continue

        winning_number = random.randint(1, 5)
        print(f"Computer chose: {winning_number}")

        if guess == winning_number:
            balance += bet
            print("🎉 You guessed right! You won ₹", bet)
        else:
            balance -= bet
            print("❌ Wrong guess! You lost ₹", bet)

        print("-" * 30)

        if balance <= 0:
            print("\nYou have run out of money! Game Over.")
            restart = input("You lost all your money. Wanna restart the game? (y/n): ").lower()
            if restart == 'y':
                balance = 10000
                print("\nGame restarted with ₹10,000!")
                continue
            else:
                break

        # Ask to continue
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("99% of the gamblers quit before winning big, come on give it a shot")
            play_again = input("Try again (get free ₹1000 special bonus)..wanna play again(y/n): ").lower()
            if play_again == 'y':
                balance += 1000
            else:
                break

    except ValueError:
        print("Please enter a valid number!\n")

print(f"\nGame Over! Final Balance: ₹{balance}")

