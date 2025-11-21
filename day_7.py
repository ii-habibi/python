import random
from day_7_hangman_words import word_list
from day_7_hangman_art import stages, logo
chosen_word = random.choice(word_list)
lives = 6

display = ["_"] * len(chosen_word)

print(logo)
print(f"The chosen word is {chosen_word}")
print(f"Your current word is: {' '.join(display)}")

end_game = False

while not end_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess in display:
        print(f"You've already guessed {guess}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        if lives == 0:
            end_game = True
            print("You've run out of lives. Game over!")
            print(f"The word was: {chosen_word}")    

    print(f"Updated word: {' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("Congratulations! You've guessed the word!")