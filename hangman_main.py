# Step 5
from hangman_words import word_list
from hangman_art import logo, stages
import random

print(logo)
print(stages[6])
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"Guess a word: {'_ '.join(display)}")

list_of_guesses = []
while not end_of_game and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in list_of_guesses:
        print(f"You already guessed {guess}, try again.")

    # Checking guessed letter
    elif guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print("Great guess!")
    else:
        lives -= 1
        print(stages[lives])
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    # Joining all the elements in the list and turn it into a String.
    list_of_guesses += guess
    print(f"{' '.join(display)}")

if "_" not in display:
    end_of_game = True
    print(f"{'_'.join(display)} \nCongratulations! You win.")
elif lives == 0:
    print("Unfortunately, you used all your lives. You lose. The word was: " + chosen_word)





