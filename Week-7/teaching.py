secret_word = "mosiah"
range_secret = len(secret_word)

hint = "______"

print("Try to guess the word")
print(f"Your hint is {hint}")

hint = ""

guess_word = input("What is your guess? ").lower()
range_guess = len(guess_word)

attempt = 1

while guess_word != secret_word:
  for i in range(range_guess):
      if guess_word[i] in secret_word:
          if ( i + 1) > range_secret:
            hint += guess_word[i]
          else:
            if guess_word[i] == secret_word[i]:
              hint += guess_word[i].upper()
            else:
              hint += guess_word[i]
      else:
        hint += "_"
  attempt += 1
  print(f"Your hint is: {hint}")
  hint = ""
  guess_word = input("What is your guess? ").lower()
  range_guess = len(guess_word)



print(f'Congratulation, you WON, the word is {secret_word.upper()}')
print(f'It took you {attempt} guesses')