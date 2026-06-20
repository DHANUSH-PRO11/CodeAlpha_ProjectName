import random
import string


def display_word(secret_word: str, guessed_letters: set[str]) -> str:
    return " ".join(ch if ch in guessed_letters else "_" for ch in secret_word)


def get_valid_letter() -> str:
    while True:
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue
        if guess not in string.ascii_lowercase:
            print("Please enter a valid alphabet letter (a-z).")
            continue
        return guess


def main():
    words = [
        "python",
        "hangman",
        "developer",
        "computer",
        "challenge",
    ]

    secret_word = random.choice(words)
    guessed_letters: set[str] = set()

    max_incorrect = 6
    incorrect_guesses = 0

    print("=== Hangman ===")
    print(f"You have {max_incorrect} incorrect guesses remaining.")
    print(display_word(secret_word, guessed_letters))

    while True:
        if incorrect_guesses >= max_incorrect:
            print(f"\nYou lost! The word was: {secret_word}")
            break

        if all(ch in guessed_letters for ch in secret_word):
            print(f"\nYou won! The word is: {secret_word}")
            break

        letter = get_valid_letter()

        if letter in guessed_letters:
            print(f"You already guessed '{letter}'. Try another letter.")
            continue

        guessed_letters.add(letter)

        if letter in secret_word:
            print(f"Good guess: '{letter}' is in the word!")
        else:
            incorrect_guesses += 1
            remaining = max_incorrect - incorrect_guesses
            print(f"Wrong guess: '{letter}' is not in the word.")
            print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect} (remaining: {remaining})")

        print(display_word(secret_word, guessed_letters))


if __name__ == "__main__":
    main()

