# Project 11 - Blackjack
# Trail game link : https://games.washingtonpost.com/games/blackjack/

import random
import pyautogui
from day_011.art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    player_cards = random.choices(cards, k=2)
    dealer_cards = random.choices(cards, k=2)

    def blackjack_win_check():
        player_has_blackjack = player_cards[0] + player_cards[1]
        dealer_has_blackjack = dealer_cards[0] + dealer_cards[1]

        if player_has_blackjack == 21 and dealer_has_blackjack == 21:
            return True, "Push, Match is Tie."
        elif player_has_blackjack == 21:
            return True, "Win with a blackjack."
        elif dealer_has_blackjack == 21:
            return True, "You lose, Dealer win with a blackjack."
        else:
            return False, "Nil"

    blackjack_win = blackjack_win_check()

    def win_check(sumofplayer, sumofdealer):
        if blackjack_win[0]:
            return blackjack_win[1]
        elif sumofplayer > 21:
            return "Bust, you went over. You lose "
        elif sumofdealer > 21:
            return "Bust, dealer went over. You Win"
        elif sumofplayer > sumofdealer:
            return "You Win"
        elif sumofplayer < sumofdealer:
            return "You Lose"
        elif sumofplayer == sumofdealer:
            return "Push, Match is Tie"

    print(logo)
    should_continue = True
    while should_continue:
        sum_of_player_cards = sum(player_cards)
        sum_of_dealer_cards = sum(dealer_cards)
        result = None

        print(f"Your cards: {player_cards}, current score: {sum_of_player_cards}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if blackjack_win[0]:
            should_continue = False
            result = win_check(sum_of_player_cards, sum_of_dealer_cards)
        else:
            next_move = pyautogui.confirm("Click 'hit' to get another card, Click 'stand' to pass:",
                                          buttons=['Hit', 'Stand'])
            if next_move == "Hit":
                next_card = random.choice(cards)
                player_cards.append(next_card)
                sum_of_player_cards = sum(player_cards)
            elif next_move == "Stand":
                while sum_of_dealer_cards < 16:
                    next_card = random.choice(cards)
                    dealer_cards.append(next_card)
                    sum_of_dealer_cards = sum(dealer_cards)

                if sum_of_dealer_cards > 21:
                    if 11 in dealer_cards:
                        dealer_index_of_ace = dealer_cards.index(11)
                        dealer_cards[dealer_index_of_ace] = 1
                        sum_of_dealer_cards = sum(dealer_cards)

                result = win_check(sum_of_player_cards, sum_of_dealer_cards)
                should_continue = False
        if sum_of_player_cards > 21:
            if 11 in player_cards:
                index_of_ace = player_cards.index(11)
                player_cards[index_of_ace] = 1
            else:
                result = win_check(sum_of_player_cards, sum_of_dealer_cards)

        if result is not None:
            print(f"Your final hand: {player_cards}, final score: {sum_of_player_cards}")
            print(f"Dealer's final hand: {dealer_cards}, final score: {sum_of_dealer_cards}")
            print(result)
            should_continue = False


continue_the_game = True
while continue_the_game:
    play_a_game = pyautogui.confirm("Do you want to play a game of Blackjack?", buttons=['Play', 'Exit'])
    if play_a_game == "Play":
        blackjack()
    else:
        pyautogui.alert("BlackJack is closed")
        break


# Easy method
#
# import random
# from day_011.art import logo
#
#
# def deal_card():
#     """" Returns the random card from the deck"""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
#
#
# def calculate_score(cards):
#     """Take the list of cards and returns the score calculated from the cards"""
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#
#     return sum(cards)
#
#
# def compare(userscore, dealerscore):
#     if userscore == dealerscore:
#         return "Draw 🙃"
#     elif dealerscore == 0:
#         return "Lose, opponent has Blackjack 😱"
#     elif userscore == 0:
#         return "Win with a Blackjack 😎"
#     elif userscore > 21:
#         return "You went over. You lose 😭"
#     elif dealerscore > 21:
#         return "Opponent went over. You win 😁"
#     elif userscore > dealerscore:
#         return "You win 😃"
#     else:
#         return "You lose 😤"
#
#
# def play_blackjack():
#     print(logo)
#
#     user_cards = []
#     dealer_cards = []
#     is_game_over = False
#
#     for _ in range(2):
#         user_cards.append(deal_card())
#         dealer_cards.append(deal_card())
#
#     user_score = calculate_score(user_cards)
#     dealer_score = calculate_score(dealer_cards)
#
#     while not is_game_over:
#
#         print(f"    Your cards: {user_cards}, current score: {user_score}")
#         print(f"    Dealer's first card: {dealer_cards[0]}")
#
#         if user_score > 21 or user_score == 0 or dealer_score == 0:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card or type 'n' to pass? ").lower()
#             if user_should_deal == 'y':
#                 user_cards.append(deal_card())
#                 user_score = calculate_score(user_cards)
#             else:
#                 is_game_over = True
#
#     while dealer_score != 0 and dealer_score < 17:
#         dealer_cards.append(deal_card())
#         dealer_score = calculate_score(dealer_cards)
#
#     print(f"   Your final hand: {user_cards}, final score: {user_score}")
#     print(f"   Computer's final hand: {dealer_cards}, final score: {dealer_score}")
#     print(compare(user_score, dealer_score))
#
#
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     play_blackjack()
