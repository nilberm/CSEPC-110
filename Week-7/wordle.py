import random

list_words = ["snare", "tears", "quest", "piano", "cream", "train", "heart", "there", "sweat", "place", "trace", "alone", "smile", "could", "horse", "party", "house"]

play_again = "yes"

while play_again == "yes":
    secret_word = random.choice(list_words)
    range_secret = len(secret_word)


    print('Try to guess the word')

    print("Your Hint is: ", end="")
    for l in secret_word:
       print("_ ", end="")

    hint = ''

    attempt = 1

    guess_word = input('\nWhat is your guess? ').lower()
    range_guess = len(guess_word)


    while guess_word != secret_word:
        for i in range(range_guess):
            if guess_word[i] in secret_word:
                if (i + 1) > range_secret:
                    hint += guess_word[i]
                else:
                    if guess_word[i] == secret_word[i]:
                        hint += guess_word[i].upper()
                    else:
                        hint += guess_word[i]
            else:
                hint += '_ '
        attempt += 1
        print(f'Your hint is: {hint}')
        hint = ''
        guess_word = input('What is your guess? ').lower()
        range_guess = len(guess_word)

    print(f'Congratulation, you WON, the word is {secret_word.upper()}')
    print(f'It took you {attempt} guesses')

    play_again = input("\nDo you want to play again? (yes/no) ")

print("\nEnd Game")