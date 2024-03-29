# Step 1
import random
import os
from Hangman_art import logo, stages
from Hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
user_ans = ["_"] * len(chosen_word)
lives = 6
new = list(chosen_word)
while lives > 0:
    guess = input("Guess a letter\n").lower()
    if guess in user_ans:
        print(f"You've already guessed {guess}")

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            user_ans[index] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print(
                f"\nYou Lose.\n\
You Lost all the lives. The correct answer was {chosen_word}"
            )
    print(f"{' '.join(user_ans)}")

    if new == user_ans:
        print("".join(user_ans) + ", " + "you have guessed the word right")
        break
    else:
        print(stages[lives])
