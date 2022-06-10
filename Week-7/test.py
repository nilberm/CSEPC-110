secret_word = "computer"

guess_attempt = 0

guess_word = ""


wrong_answer = True

hint = "________"

print("\nWelcome to the word guessing game!\n")

print(f"Your hint is {hint}\n")

hint = ""

count = 0
guess_word = input("What is your guess? ").lower()

for letter in guess_word:
  for i in range(0, 8):
    if letter in secret_word:
      print(f"{letter} guess word, {secret_word[i]} secret word")
      print(secret_word[count])
      print(i)
      count += 1
      break
    else:
      print(letter, "NOT in secret word")
      print(secret_word[count])
      print(i)
      count += 1
      break


print(hint)