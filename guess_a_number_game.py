from colorama import Fore, Style
from random import randint

print("Do you want to play a guessing game?")

while True:
    computer_number = randint(1, 100)

    while True:
        guesses_input = input(Style.RESET_ALL + "In how many moves you will guess the number: ")
        if not guesses_input.isdigit():
            print(Fore.RED + "Invalid input. Please try again!")
            continue
        else:
            guess_number = int(guesses_input)
            break

    guess_counter = 0

    while guess_number > guess_counter:
        user_input = input(Style.RESET_ALL + "Guess the number (1:100): ")

        if not user_input.isdigit():
            print(Fore.RED + "Invalid input. Please try again!")
            continue
        else:
            player_number = int(user_input)
            guess_counter += 1
            moves_left = guess_number - guess_counter

        if player_number == computer_number:
            print(Fore.GREEN + "You guessed it!")
            break
        elif player_number > computer_number:
            print(f"Your guess is too high!", end=' ')
            if moves_left > 1:
                print(f"You have {moves_left} guesses left.")
            elif moves_left == 1:
                print(f"You have {moves_left} guess left.")
            continue
        else:
            print(f"Your guess is too low!", end=' ')
            if moves_left > 1:
                print(f"You have {moves_left} guesses left.")
            elif moves_left == 1:
                print(f"You have {moves_left} guess left.")
            continue
    else:
        print("\nSorry, you ran out of guesses!")

    exit_game = False

    while True:
        restart = input(Style.RESET_ALL + "\nType [yes] to Play again or [no] to quit: ")

        if restart == 'yes':
            break
        elif restart == 'no':
            print("\x1B[3mThank you for playing!")
            exit_game = True
            break
        else:
            print("Invalid input. Please try again...")
            continue

    if exit_game:
        break
