"""Programming a Simple Hangman Game!"""

import random, os

hangman_pics: list[str] = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def play() -> str:
    word_file = os.path.join("words", "hangman_wordbank")
    secret: str = random.choice(open(word_file).read().split())
    secret = secret.replace(",","")
    print(hangman_pics[0])
    result: str = "_ " * len(secret)
    print(result)
    n: int = result.count("_")
    m: int = result.count("_")
    used_letters: list[str] = []
    pic: int = 1
    while n > 0: 
        result: str = input_guess(secret, result, pic, used_letters)
        print(result)
        if "_" not in result and "lost" not in result: 
            return f"You won! Congratulations! Type in \"play()\" to play again :)"
        n = result.count("_")
        if n == m:
            pic += 1
        else:
            m = n
        

def input_guess(secret: str, result: str, num: int, already_guessed: list[str]) -> str:
    guess: str = input("Choose a letter: ").lower()
    while not ((guess in "abcdefghijklmnopqrstuvwxyz") and (len(guess) == 1)):
        guess = input("Invalid input. Please choose a single letter: ").lower()
    while guess in already_guessed:
        guess = input("That letter was already guessed! Please choose another letter: ").lower()
    new_string: str = ''
    i: int = 0
    j: int = 0
    counter: int = 0
    while i < len(result) and j < len(secret):
        if result[i] == "_" and secret[j] == guess:
            new_string += f'{guess}'
            counter += 1
        elif result[i] == "_" and secret[j] != guess:
            new_string += "_"
        elif result[i] in "abcdefghijklmnopqrstuvwxyz":
            new_string += result[i]
        elif result[i] == " ":
            new_string += " "
            j -= 1
        i += 1
        j += 1
    already_guessed.append(guess)
    if counter < 1:
        print(f"{hangman_pics[num]}")
        if num == 6:
            return f"You lost! Better luck next time!\nThe word was {secret}.\nType in \"play()\" to play again :)"
    return new_string
