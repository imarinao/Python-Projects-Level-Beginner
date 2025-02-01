import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)


def choose_random_word():
    """Selects a random word from the list."""
    return random.choice(word_list)


def display_formated_placeholder(placeholder):
    """Formats and prints the placeholder list as a string."""
    formated_placeholder = " ".join(placeholder)
    print(formated_placeholder)


def replace_placeholder_with_correct_input(chosen_word, placeholder, user_input, lives):
    """Replaces underscores with correctly guessed letters."""
    if user_input not in chosen_word:
        lives -= 1  # Reduce lives only if the letter is not found
    else:
        for index, letter in enumerate(chosen_word):
            if letter == user_input:
               placeholder[index] = letter  # Update the correct index

    return lives  # Return updated lives count
    # letter_position = 0
    # for letter in chosen_word:
    #     if letter == user_input:
    #         placeholder[letter_position] = letter
    #     letter_position += 1


def play_game():
    """Main game loop."""
    chosen_word = choose_random_word()
    print(chosen_word)
    placeholder = ["_"] * len(chosen_word)
    print(f"The word has {len(chosen_word)} letters.")
    display_formated_placeholder(placeholder)  # Show the initial dashes

    lives = 6
    game_over = False

    while not game_over:

        if lives > 0:  # Game continues while lives remain
            print(stages[lives])
            user_input = input("Guess a letter: ").lower()

            # Store updated lives after checking the letter
            lives = replace_placeholder_with_correct_input(chosen_word, placeholder, user_input, lives)  # Update the word
            display_formated_placeholder(placeholder)  # Show the updated word
            if "_" not in placeholder:  # Check if all the letters were guessed
                print(f"Congratulations! You guessed the word: {chosen_word}")
                game_over = True
        else:
            game_over = True
            print(stages[0])
            print(f"The word was {chosen_word}. You lost")


# Run the game
play_game()








