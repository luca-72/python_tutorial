secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess a number from 1 - 10: "))
    guess_count += 1
    if guess == secret_number:
        print("YOU WON!!!!")
        break
else:
    print("That is the wrong guess. You have no more guesses.")