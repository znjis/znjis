
import random
from hangman import Hangman
from words import words



def game():
    category = input("\n\npick a category (food, countries, animals or cars):\n\n")
    if category not in words:
        print("this is not a category")
        game()
    objet = Hangman(random.choice(words[category]))
    while True:
        if objet.gagner():
            print("\n\n You won! \n\n")
            break
        if objet.perdre():
            print(objet)
            print("\n\n" + f"You lost! The word was : {objet.mot}" + "\n\n")
            break
        print(objet)
        objet.guess()


if __name__ == '__main__':

    game()