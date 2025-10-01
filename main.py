import random
from words import word_list

def scramble(word):
    characters = list(word)
    random.shuffle(characters)
    return "".join(characters)

def start_game():
    word = random.choice(word_list)
    scrambled = scramble(word)
    print(f"Unscramble this word: {scrambled}")
    guess = input("Your guess: ").strip().lower()
    if guess == word:
        print("Correct!")
    else:
        print(f"Wrong! The word was '{word}'.")

def play_game():
    score = 0
    while True:
        start_game()
        score += 1
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != "y":
            break
    print(f"Your final score is {score}.")

if __name__ == "__main__":
    play_game()