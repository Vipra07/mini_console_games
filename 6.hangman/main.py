import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
    "apple", "banana", "grape", "orange", "peach", "cherry", "mango", "lemon", "kiwi", "melon",
    "zebra", "tiger", "lion", "elephant", "giraffe", "monkey", "panda", "kangaroo", "rhino", "hippo",
    "python", "java", "ruby", "swift", "kotlin", "golang", "perl", "haskell", "lisp", "rust",
    "house", "window", "garden", "kitchen", "garage", "balcony", "bedroom", "bathroom", "ceiling", "floor",
    "school", "teacher", "student", "pencil", "notebook", "chalk", "desk", "board", "marker", "eraser",
    "car", "train", "airplane", "bicycle", "subway", "boat", "scooter", "truck", "bus", "motorcycle",
    "pizza", "burger", "salad", "noodle", "sushi", "steak", "fries", "taco", "pasta", "soup",
    "cloud", "storm", "sunshine", "rainbow", "thunder", "wind", "fog", "snow", "lightning", "hail",
    "planet", "galaxy", "comet", "meteor", "asteroid", "earth", "venus", "mars", "jupiter", "saturn",
    "robot", "matrix", "cyborg", "android", "network", "system", "binary", "code", "device", "signal"
]
chosen_word = random.choice(word_list)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

game_over = False
guessed_words = []
# display = ["_" for _ in chosen_word]
lives = 6

while game_over is False:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in guessed_words:
        print("You already guessed it")
    elif guess in chosen_word:
        # display = ""
        for letter in chosen_word:
            if letter == guess:
                display += letter
                guessed_words.append(letter)
            elif letter in guessed_words:
                display += letter
            else:
                display += "_"
        print(display)
        print(stages[lives])
        print(f"****************{lives}/6 LIVES LEFT***************")

        if "_" not in display:
            game_over = True
            print("You win")

    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        print(stages[lives])
        print(f"****************{lives}/6 LIVES LEFT***************")
