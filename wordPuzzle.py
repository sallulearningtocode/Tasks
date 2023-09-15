import random

word_list = ["Father", "Bark", "Cry", "Green", "Aeroplane", "Python", "Dog", "Cat", "Mouse", "Elephant"]

def get_word_round():
    round_words = random.sample(word_list, 5)
    return round_words

def play_round():
    round_words = get_word_round()
    score = 0

    for word in round_words:
        word_chars = list(word)
        random.shuffle(word_chars)
        shuffled_word = ''.join(word_chars)

        print("Arrange the letters to form a valid word:")
        print(shuffled_word)

        user_input = input("Your answer: ")
        if user_input.lower() == word.lower():
            print("Correct")
            score += 1
        else:
            print("Wrong")

    return score

def play_game():
    total_score = 0
    rounds = 5

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}:")
        score = play_round()
        total_score += score
        print(f"Round {round_num} Score: {score}\n")

    print(f"Net Score is {total_score}")

if __name__ == "__main__":
    play_game()
