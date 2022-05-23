"""
File: hangman.py
Name: Andy Chi
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program creates the famous game: "Hangman." Players will
    have N turns to guess the correct answer. With each wrong
    answer, players will lose one turn until they guess the correct
    string or all turns have been used.
    """
    answer = random_word()
    blank = create_word(answer)
    n = N_TURNS
    print("The word looks like: " + str(blank))
    print("You have " + str(n) + " guesses left.")
    hang_man(answer, n, blank)


def hang_man(answer, n, blank):
    """
    This function creates the hangman process.
    """
    while n != 0:
        input_ch = input("Your guess: ")
        if input_ch.isalpha():
            if len(input_ch) == 1:
                input_upper = input_ch.upper()
                ans = ""
                if input_upper in answer:
                    for i in range(len(answer)):
                        alphabet = answer[i]
                        if alphabet == input_upper:
                            ans += input_upper
                        elif alphabet in blank:
                            ans += alphabet
                        else:
                            ans += "-"
                    print("You are correct!")
                    blank = ans
                    if blank == answer:
                        print("You win!!")
                        print("The word was: " + str(answer))
                        break
                else:
                    n -= 1
                    print("There is no " + str(input_upper) + "'s" + " in the word.")
                    if n == 0:
                        print("You are completely hung : (")
                        print("The word was: " + str(answer))
                        break
                print("The word looks like: " + str(blank))
                print("You have " + str(n) + " guesses left.")
            else:
                print("Illegal format.")
        else:
            print("Illegal format.")


def create_word(answer):
    """
    This function creates the black spaces corresponding to the
    random word.
    """
    ans = ""
    for i in range(len(answer)):
        ans += "-"
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
