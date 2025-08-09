import random

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Pick a random word
original_word = random.choice(words)
print(f"(cheat: The word is {original_word})")

# Scramble the word
scrambled = ''.join(random.sample(original_word, len(original_word)))

print("Welcome to Word Scramble!")
print(f"Unscramble this word: {scrambled}")

attempts = 3
while attempts > 0:
    guess = input("Your guess: ").strip().lower()
    if guess == original_word:
        print("Correct! You unscrambled the word.")
        break
    else:
        attempts -= 1
        print(f"Incorrect! You have {attempts} attempts left.")