import game_data
import random
import art
print(art.logo)

def vs(l1, l2):
    name1 = l1['name']
    des1 = l1['description']
    origin1 = l1['country']
    fol1 = l1['follower_count']

    name2 = l2['name']
    des2 = l2['description']
    origin2 = l2['country']
    fol2 = l2['follower_count']


    print(f"Compare A: {name1}, a {des1}, from{origin1}")
    print(art.vs)
    print(f"Compare B: {name2}, a {des2}, from{origin2}")

def correct_answer(l1, l2):
    a = l1['follower_count']
    b = l2['follower_count']
    if a > b:
        return 'A'
    elif b > a:
        return 'B'
    else:
        return None

def check_answer(answer, actual_answer):
    if answer == actual_answer:
        return 1
    else:
        return 0

game_over = False
option1 = random.choice(game_data.data)
score = 0
while not game_over:
    option2 = random.choice(game_data.data)
    vs(option1, option2)
    guess = input("Who has more followers? Type 'A' or 'B': ")
    higher_follower_option = correct_answer(option1, option2)
    result = check_answer(guess, higher_follower_option)
    option1 = option2
    if result == 1:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
