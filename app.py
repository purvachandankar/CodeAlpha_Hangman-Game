import random

words = ["python", "java", "flask", "mysql", "django"]

word = random.choice(words)

display = ["_"] * len(word)

max_guesses = 6
incorrect_guesses = 0

guessed_letters = []

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

while incorrect_guesses < max_guesses and "_" in display:

    print("\nWord:", " ".join(display))
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:

        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:

        print("Wrong guess!")
        incorrect_guesses += 1


if "_" not in display:
    print("\nCongratulations! You won!")
    print("The word was:", word)

else:
    print("\nGame Over!")
    print("The word was:", word)