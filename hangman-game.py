import random
import string

def clear():
    print("\n" * 10)

try:
    # replit provides a nice clear screen function but if the package isn't installed ignore it
    from replit import clear
except ImportError as error:
    pass

words = "action adjective adult age animal back bed blood body book box boy car child chocolate city clothes color company country cycle date day death dictionary direction door earth egg electricity employee face family farm father fish floor flowers food foot fridge friend fruit furniture future game garden girl glass government group health hill holiday idea island jewelry job kitchen market material mirror mobile month name news number ocean park party pencil picture place plant queen rain river road rock room school shape ship shoe shop size son sun street table taxi tea teacher time train vehicle water weather woman work year yesterday zoo"
words = words.split()

def print_word(guessed_word):

    out_word = ''

    for c in guessed_word:
        out_word += c + ' '

    print(f"Your word: {out_word}")

def player_choice(current_word, guessed_word, guess_letter):
    if not guess_letter in current_word:
        print(f"Sorry, there are no {guess_letter}'s in this word.")
    else:
        num_of_matching = 0
        
        for i, c in enumerate(current_word):
            if c == guess_letter:
                guessed_word[ i ] = guess_letter
                num_of_matching += 1

        print(f"Good job, there are {num_of_matching} {guess_letter}'s in this word.")

should_continue = True
while should_continue:
    #clear()
    player_wants_to_play = input('SHALL WE PLAY A GAME? [Y/n] ').lower()

    if (player_wants_to_play == 'n'):
        should_continue = False
    else:
        current_word = list(random.choice(words))
        guessed_word = ['_' ] * len(current_word)
        letters_remaining = list(string.ascii_lowercase)

        has_won = False
        while not has_won:
            print_word(guessed_word)
           
            print(f"Letters remaining: {''.join(letters_remaining)}")
            user_guess = input('Guess a letter> ').lower()[0]

            if user_guess in letters_remaining:

                letters_remaining.remove(user_guess)
            
                player_choice(current_word, guessed_word, user_guess)

                if current_word == guessed_word:
                    has_won = True
                    print(f"GOOD JOB! You solved the puzzle!  The word was: {''.join(current_word)}")
            else:
                print(f"You already guessed: {user_guess}")

print("""
A STRANGE GAME.
THE ONLY WINNING MOVE IS
NOT TO PLAY.
        """)
