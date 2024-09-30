import random

def guess_the_number():
    

    while True:
        number = random.randint(1, 100)
        attempts = 0

        print("Welcome to Guess the Number! I'm thinking of a number between 1 and 100.")

        while True:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
                if guess < 1 or guess > 100:
                    print("Please enter a number within the range of 1 to 100.")
                    continue

                attempts += 1

                if guess == number:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
                elif guess < number:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")
            except ValueError:
                print("That's not a valid number. Please enter an integer.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

guess_the_number()
