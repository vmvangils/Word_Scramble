import random
from words import word_list

def scramble(word):
    characters = list(word)
    scrambled = "".join(characters)
    while scrambled == word:
        random.shuffle(characters)
        scrambled = "".join(characters)
    return scrambled

def start_game():
    word = random.choice(word_list)
    scrambled = scramble(word)
    print(f"Unscramble this word ({len(word)} letters): {scrambled}")

    while True:
        guess = input("Your guess: ").strip().lower()
        if guess == word:
            print("Correct!")
            return True
        else:
            print("Wrong! Try again.")

def play_game():
    score = 0
    while True:
        if start_game():
            score += 1
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != "y":
            break
    print(f"Your final score is {score}.")

if __name__ == "__main__":
    play_game()