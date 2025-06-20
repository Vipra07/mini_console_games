cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
def starting_cards():
    start_set = []
    for i in range(2):
        start_set.append(random.choice(cards))
    return start_set
def sum_of_cards(l):
    s = 0
    for value in l:
        s += value
    return s

def final(a, b):
    c = sum_of_cards(a)
    d = sum_of_cards(b)
    if c == d:
        print("It's a draw")
    elif c > d:
        print("You win")
    elif c < d:
        print("You lose")

def blackjack():
    import art


    print("\n"*20)
    print(art.logo)
    y_cards = starting_cards()
    print(f"Your cards: {y_cards}, current score = {sum_of_cards(y_cards)}")
    c_cards = starting_cards()
    print(f"Computer's first card: {c_cards[0]}")
    game_over = False
    while not game_over:
        y_score = sum_of_cards(y_cards)
        c_score = sum_of_cards(c_cards)
        if y_score == 21 and c_score== 21:
            print(f"Your final hand: {y_cards}, final score: {y_score}")
            print(f"Computer's final hand: {c_cards}, final score: {c_score}")
            print("It's a draw")
            game_over = False
        elif y_score == 21:
            print(f"Your final hand: {y_cards}, final score: {y_score}")
            print(f"Computer's final hand: {c_cards}, final score: {c_score}")
            print("You win")
            game_over = False
        elif c_score == 21:
            print(f"Your final hand: {y_cards}, final score: {y_score}")
            print(f"Computer's final hand: {c_cards}, final score: {c_score}")
            print("You lose")
            game_over = False
        else:
            conti = True
            while conti and not game_over:
                h_s = input("Type 'y' to get another card, type 'n' to pass: ")
                if h_s == "y":
                    ace = random.choice(cards)

                    if ace == 11:
                        if y_score+11 > 21:
                            y_cards.append(1)
                        else:
                            y_cards.append(11)
                    else:
                        y_cards.append(ace)




                    print(f"Your cards: {y_cards}, current score: {sum_of_cards(y_cards)}")
                    print(f"Computer's first card: {c_cards[0]}")
                    y_score = sum_of_cards(y_cards)

                    if y_score > 21:

                        print(f"Your final hand: {y_cards}, final score: {y_score}")
                        print(f"Computer's final hand: {c_cards}, final score: {c_score}")
                        print("You went over. You lose 😭")
                        game_over = True

                    elif y_score == 21:
                        print(f"Your final hand: {y_cards}, final score: {y_score}")
                        print(f"Computer's final hand: {c_cards}, final score: {c_score}")
                        print("You win")
                        game_over = True

                elif h_s == "n":
                    conti = False


                else:
                    conti = True

            if not game_over:
                c_score = sum_of_cards(c_cards)
                while c_score < 17:
                    r = random.choice(cards)
                    if r == 11:
                        if c_score + 11 > 21:
                            c_cards.append(1)
                        else:
                            c_cards.append(11)
                    else:
                        c_cards.append(r)


                    c_score += r
                if c_score > 21:
                    print(f"Your final hand: {y_cards}, final score: {y_score}")
                    print(f"Computer's final hand: {c_cards}, final score: {c_score}")
                    print("Computer went over. You win")
                    game_over = True
                else:
                    print(f"Your final hand: {y_cards}, final score: {y_score}")
                    print(f"Computer's final hand: {c_cards}, final score: {c_score}")
                    final(y_cards, c_cards)
                    game_over = True
