import random

# List of words for the game
words = ['school', 'books', 'friends', 'maths', 'parents', 'zoology', 'games', 'television', 'space', 'rocket', 'chemistry', 'house', 'studies', 'project']

def shuffle_word(words):
    word_list = list(words)
    random.shuffle(word_list)
    return ''.join(word_list)

def play_game():
    random_word = random.choice(words)
    shuffled_word = shuffle_word(random_word)
    print("Shuffled word:", shuffled_word)

    user_input = input("Enter your guess (or 'quit' to end the game): ")

    if user_input.lower() == 'quit':
        print("Game ended. Goodbye!")
        return

    if user_input.lower() == random_word:
        print("Congratulations! You guessed the word correctly.")
    else:
        print("Sorry, you lost. The word was:", random_word)

def main():
    print("Welcome to the Jumbled Words game!")

    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thank you for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
