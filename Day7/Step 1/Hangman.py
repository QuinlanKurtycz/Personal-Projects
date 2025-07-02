import random
import HangmanArt
import HangmanWords

chosen_word = random.choice(HangmanWords.web2lowerset)

print("Welcome to the Gallows")
print("Here is your Word: \n")
blanks = ''
for letter in chosen_word:
    blanks += '_'
print(blanks)




game_over = False
num_lives = 6
correct_letters = []
guessed_letters = []

while not game_over:
    display = ""
    guess = input("\nSubmit thy guess in letter form: ").lower()
    correct_guess = False
    
    if guess in guessed_letters:
        print(f"You already guessed [{guess}] dingdong")
        correct_guess = True

    guessed_letters.append(guess)

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
            correct_guess = True
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if correct_guess == False:
        num_lives -= 1
        print(HangmanArt.stages[num_lives])
        print(f"Number of guesses remaining: {num_lives}")

    print(display)
 
    if "_" not in display:
        game_over = True
        print(HangmanArt.win_art)
        print("You win.")
    elif num_lives == 0:
        game_over = True
        print("You lose.")

print(f"The word was: {chosen_word}")




    


