import turtle as tk
import time
import random
from gallows import draw_gallows
from draw_hangman import draw_hangman

def run_hangman():
    """Runs the hangman game."""
    
    #Wordbank
    words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

    # Return a single random word from the wordbank
    word = random.choice(words)

    # Create a list with underscores for each letter in the word
    solution = []
    for i in range(len(word)):
        solution += "_"
        
    # Keep track of attempts made
    attempts = 0

    # Where to write text
    text_pos = (-300, -400)
    sol_pos = (-300, -430)
    
    tk.speed(0)

    # Draw the gallows
    draw_position = draw_gallows()
    
    # Create the solution word turtle object once
    sol_word = tk.Turtle()
    sol_word.up()
    sol_word.setposition(sol_pos)
    sol_word.down()
    
    
    # While loop for allowing guesses until the word has been guessed or the number of attempts has been exceeded
    while attempts < 6:

        if "".join(solution) == word:
            tk.penup()
            tk.setposition(text_pos)
            tk.pendown()
            tk.write("Congratulations! You've guessed the word!", font=("Arial", 12, "normal"))
            time.sleep(3)
            
            break

        guess = tk.textinput("Make a guess", "Guess a letter: ")

        # Counter for position of letter in the word
        i = 0

        for letter in word:
            if guess.lower() == letter:
                solution[i] = letter
            i += 1

        # Keep track of worng guesses and draw hangman accordingly
        if guess not in word:
            attempts += 1
            draw_hangman(attempts, word, draw_position, text_pos)
            
            # Control how long the turtle screen stays open before it closes
            time.sleep(3)

        # Delete the last solution and write the current one
        sol_word.clear()
        sol_word.write(solution, font=("Arial", 14, "normal"))
        

if __name__ == "__main__":
    run_hangman()