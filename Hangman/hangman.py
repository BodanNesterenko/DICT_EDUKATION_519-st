import random
word_list = ["Space",
             "Human",
             "Cat",
             "Cow",
             "Rocket",
             "Star"]


def word_selection():
    word = random.choice(word_list)
    return word.lower()


def game(word):
    under = "_" * len(word)
    guessed = False
    tries = 8
    guessed_letters = []
    guessed_words = []
    print(under)
    print("Tries=", tries)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess the word:>").lower()
        if len(guess) == 1:
            if guess in guessed_letters:
                print("You guess the latter", guess)
                tries -= 1
            if guess in guessed_letters:
                print("no improvements")
                tries -= 1
            elif guess not in word:
                print("That letter doesn't appear in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess, "Is in the word")
                guessed_letters.append(guess)
                word_as_list = list(under)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                under = "".join(word_as_list)
                if "_" not in under:
                    guessed = True

        print("HANGMAN")
        print("Tries=", tries)
        print(under)
        print("\n")
    if guessed:
        print("Congratulation, you guessed the word! You win!")
    else:
        print("You lose. The word is", word)


def main():
    print("HANGMAN")
    word = word_selection()
    game(word)


main()
