import random

print("Welcome to the Guess the Secret Number Game!")

wins = 0  # total number of player wins

while True:
    secret_number = random.randint(1, 20)
    guess_count = 0

    # Choose difficulty
    difficulty = input("Choose difficulty (easy/hard): ").lower()
    if difficulty == "easy":
        guess_limit = 5
    else:
        guess_limit = 3

    print("\nTry to guess the secret number!")
    print("It's between 1 and 20.")
    print(f"You have {guess_limit} attempts.\n")

    while guess_count < guess_limit:
        try:
            guess = int(input("Guess the secret number: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        guess_count += 1
        guesses_left = guess_limit - guess_count

        if guess == secret_number:
            print(f"\n🎉 You guessed it in {guess_count} {'guess' if guess_count == 1 else 'guesses'}!")
            print(f"{secret_number} was the secret number. Well done!\n")
            wins += 1
            break
        elif guess < secret_number:
            print(f"Too low. ({guesses_left} guesses left)\n")
        else:
            print(f"Too high. ({guesses_left} guesses left)\n")

    else:
        print("😞 You ran out of guesses.")
        print(f"The secret number was {secret_number}\n")

    print(f"🏆 Total wins: {wins}\n")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Goodbye 👋")
        print(f"Final wins: {wins}")
        break

    print("\n" + "-" * 40 + "\n")  # separator between games
