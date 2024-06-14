import turtle as tk
import time
import random
from gallows import draw_gallows
from draw_hangman import draw_hangman

def get_user_input(text_pos):
    while True:
        guess = tk.textinput("Make a guess", "Guess a letter: ")
        if guess is None:
            raise SystemExit("You did not enter anything. Game end.")
        guess = guess.strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            error_turtle = tk.Turtle()
            error_turtle.hideturtle()
            error_turtle.up()
            error_turtle.setposition(text_pos)
            error_turtle.down()
            error_turtle.clear()
            error_turtle.write("Invalid input. Please enter a single letter.", font=("Arial", 12, "normal"))
            time.sleep(2)
            error_turtle.clear()
            time.sleep(3)       
        else:
            return guess

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
    sol_word.hideturtle()
    sol_word.up()
    sol_word.setposition(sol_pos)
    sol_word.down()
    
    
    # While loop for allowing guesses until the word has been guessed or the number of attempts has been exceeded
    while attempts < 6:

        if "".join(solution) == word:
            you_won_turtle = tk.Turtle()
            you_won_turtle.hideturtle()
            you_won_turtle.up()
            you_won_turtle.setposition(text_pos)
            you_won_turtle.down()
            you_won_turtle.clear()
            you_won_turtle.write("Congratulations, you guessed the word!", font=("Arial", 12, "normal"))
            time.sleep(3)       
            break

        try:
            guess = get_user_input(text_pos)
        except SystemExit as e:
            print(e)
            break

        if guess in solution:
            already_guessed_turtle = tk.Turtle()
            already_guessed_turtle.hideturtle()
            already_guessed_turtle.up()
            already_guessed_turtle.setposition(text_pos)
            already_guessed_turtle.down()
            already_guessed_turtle.clear()
            already_guessed_turtle.write("You already guess that letter. Try agian.", font=("Arial", 12, "normal"))
            time.sleep(2)
            already_guessed_turtle.clear()
            time.sleep(3) 
               
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