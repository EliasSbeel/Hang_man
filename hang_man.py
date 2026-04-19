import random 
from hang_man_word import word_list
from hangman_stages import stages, logo

lives = 6
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
placeholder = ""
for p in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
conrrect_letters = []

while not game_over:
    print(f"## {lives}/6 LIVES LEFT")

    guess = input("Guess a letter: ").lower()
    if guess in conrrect_letters:
        print(f"You have already guessed this {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess
            conrrect_letters.append(guess)
        elif letter in conrrect_letters:
            display += letter
        else:
            display += "_"

    print(f"Word to guess: {display}")
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"It was {chosen_word} You Lose.")
            
    if "_" not in display:
        game_over = True
        print("You Win.")
    
    print(stages[lives])


