import random

def get_guess():
    while True:
        try:
            guess = int(input("Enter a guess between 0 and 50: "))
            if 0 <= guess <= 50:
                return guess
            else:
                print("Please enter a number between 0 and 50.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    target = random.randint(0, 50)
    attempts = 3

    for _ in range(attempts):
        guess = get_guess()
        if guess == target:
            print("Correct! You've guessed the number.")
            break
        else:
            print("Incorrect. Try again.")
    else:
        print(f"Sorry, you've used all your attempts. The correct number was {target}.")

if __name__ == "__main__":
    main()
