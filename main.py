import random
import time
from words import word_list

def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)

def play_game():
    score = 0
    time_left = 15

    while time_left > 0:
        word = random.choice(word_list)
        scrambled = scramble(word)
        print(f"Unscramble this word: {scrambled}")

        start = time.time()
        guess = input(f"Time left: {int(time_left)}seconds").strip().lower()
        elapsed = time.time() - start
        time_left -= elapsed

        if time_left <= 0:
            print("Out of time!")
            break

        if guess == word:
            print("Correct!")
            score += 1
            time_left += 5
        else:
            print("Incorrect!")
            time_left -= 2
            if time_left <= 0:
                print("Out of time!")
                break

    print(f"You lost! Final score: {score}")

if __name__ == "__main__":
    play_game()