import random

# List of words for the game
words = ["apple", "banana", "cherry", "grape",
         "orange", "strawberry", "watermelon"]


def choose_word(words):
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    selected_word = choose_word(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(selected_word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in selected_word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            if attempts == 0:
                print("Sorry, you lost. The word was:", selected_word)
                break
        else:
            word_display = display_word(selected_word, guessed_letters)
            print(word_display)

            if "_" not in word_display:
                print("Congratulations, you won!")
                break


hangman()
