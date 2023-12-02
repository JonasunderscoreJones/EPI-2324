'''EPR Übungsblatt 05'''
__author__="7987847, Werner"

import random
import blatt04


def load_players() -> [str]:
    '''Erstellt die Spieler des Spiels'''
    while True:
        try:
            player_count = int(input("Anzahl der Spieler (3-4): "))
            if player_count in [3, 4]:
                break
        except ValueError:
            pass

    player_names = []

    for i in range(player_count):
        print("Spieler", i+1, "Name: ", end='')
        name = input()
        if name == "":
            name = "Spieler " + str(i+1)
        player_names.append(name)

    return player_names


def initialize_variables(players:[str]) -> ({str: int}, {str: list}):
    '''Initialisiert die Variablen für das Spiel'''

    score_dict = {}
    hand_dict = {}

    # Erstelle und mische das Kratenblatt
    deck = blatt04.create_card_list(12)
    deck = blatt04.shuffle_card_list(deck)

    for i in players:
        score_dict[i] = 0
        hand_dict[i] = []

    hand_dict = blatt04.hand_out_cards_modified(deck, hand_dict, 3)

    return score_dict, hand_dict


def play_game(players: list, scores: {str: int}, all_hands: {str: list}) -> {str: int}:
    '''Spielt das Spiel'''

    game_over = False

    while not game_over:
        # Ermittlung einer zufälligen Reihenfolge der Spieler
        random.shuffle(players)

        trumpf = "any"
        played_cards = []
        for player in players:
            # Karte spielen
            # player hand von dict all_hands holen
            player_hand = all_hands.get(player)

            print("-------------------")
            print("Spieler", player, "ist an der Reihe")
            played_card, player_cards = play_card(player_hand, trumpf)
            all_hands[player] = player_cards

            # Wenn der Spieler an der Reihe ist
            if player == players[0]:
                trumpf = played_card[1]
                print("~~~~~~~~~~~~~~~~~~~")
                print("Trumpf ist", trumpf)
                print("~~~~~~~~~~~~~~~~~~~")
            played_cards.append(played_card)

        # Ermittlung des Gewinners
        winner = get_winner(played_cards, trumpf)

        # Punktevergabe
        if winner != -1:
            scores[players[winner]] += 1

            # Gewinner bekommt die Karten
            for card in played_cards:
                all_hands[players[winner]].append(card)

        print("Punktestand: ", scores)

        # Überprüfung ob das Spiel zu Ende ist
        for player in players:
            if len(all_hands[player]) == 0:
                game_over = True

    print("Das Spiel ist zu Ende.")
    # sortiere die spieler scores nach der höhe
    sorted_scores = sorted(scores.items(), key=lambda x: x[1])

    players_won = []
    players_won.append(sorted_scores[0][0])

    for i in range(len(sorted_scores)):
        if i == len(sorted_scores) - 1:
            break
        if sorted_scores[i][1] == sorted_scores[i+1][1]:
            players_won.append(sorted_scores[i+1][0])

    print("Die Spieler", players_won, "haben gewonnen.")





def check_card(card: (int, str), player_hand: list, trump: str) -> bool:
    '''Überprüft ob eine Karte gespielt werden darf'''

    if card[1] == trump:
        return True

    for i in player_hand:
        if i[1] == trump:
            return False

    return True


def play_card(player_hand: list, trump: str) -> ((int, str), list):
    '''Spielt eine Karte aus der Hand'''
    for i in player_hand:
        print(i + 1, player_hand[i])

    card_valid = False

    while not card_valid:
        played_card_index = input(
            "Karte wählen. Bei illegalem Zug wird dies wiederholt.\
(Nummer von 1 - " +
              str(len(player_hand)) + "): ")

        try:
            played_card_index = int(played_card_index)
            player_hand[played_card_index - 1]
        except ValueError:
            print("Keine gültige Zahl")
            continue

        card_valid = check_card(player_hand[played_card_index - 1], player_hand, trump)

    print("Karte gespielt: ", player_hand[i-1])

    return player_hand.pop(i-1), player_hand


def get_winner(current_trick: list, trump: str) -> int:
    '''Ermittelt den Gewinner eines Stiches'''

    # Ermittelt die Trumpfkarten der liste current_trick.
    trump_cards = list(filter(lambda x: x[1] == trump, current_trick))

    if len(trump_cards) > 0:
        # Ermittelt die höchste Trumpfkarte
        highest_trump = max(trump_cards, key=lambda x: x[0])
        return current_trick.index(highest_trump)

    # Wenn es keine Trumpkarten gibt, gewinnt niemand
    return -1














if __name__ == '__main__':
    players = load_players()
    scores, hands = initialize_variables(players)
    play_game(players, scores, hands)

    # Testfälle

    # a)
    # load_players()
    # Ausgabe: Anzahl der Spieler (3-4): 3
    # Spieler 1 Name: Spieler 1
    # Spieler 2 Name: Spieler 2
    # Spieler 3 Name: Spieler 3
    # Rückgabe: ['Spieler 1', 'Spieler 2', 'Spieler 3']

    # load_players()
    # Ausgabe: Anzahl der Spieler (3-4): 4
    # Spieler 1 Name: Spieler 1
    # Spieler 2 Name: Spieler 2
    # Spieler 3 Name: Spieler 3
    # Spieler 4 Name: Spieler 4
    # Rückgabe: ['Spieler 1', 'Spieler 2', 'Spieler 3', 'Spieler 4']

    # load_players()
    # Ausgabe: Anzahl der Spieler (3-4): 2
    # Anzahl der Spieler (3-4): 5
    # Anzahl der Spieler (3-4): 3
    # Spieler 1 Name: Spieler 1
    # Spieler 2 Name: Spieler 2
    # Spieler 3 Name: Spieler 3
    # Rückgabe: ['Spieler 1', 'Spieler 2', 'Spieler 3']

    # b)
    # initialize_variables(['Spieler 1', 'Spieler 2', 'Spieler 3'])
    # Rückgabe: ({'Spieler 1': 0, 'Spieler 2': 0, 'Spieler 3': 0},
    # {'Spieler 1': [(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Spieler 2':
    # [(1, 'Karo'), (2, 'Kreuz'), (2, 'Pik')], 'Spieler 3': [(2, 'Herz'),
    # (2, 'Karo'), (3, 'Kreuz')]})

    # initialize_variables(['Spieler 1', 'Spieler 2', 'Spieler 3', 'Spieler 4'])
    # Rückgabe: ({'Spieler 1': 0, 'Spieler 2': 0, 'Spieler 3': 0,
    # 'Spieler 4': 0}, {'Spieler 1': [(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')],
    # 'Spieler 2': [(1, 'Karo'), (2, 'Kreuz'), (2, 'Pik')], 'Spieler 3':
    # [(2, 'Herz'), (2, 'Karo'), (3, 'Kreuz')], 'Spieler 4': [(3, 'Pik'),
    # (3, 'Herz'), (3, 'Karo')]})

    # initialize_variables(['Spieler 1', 'Spieler 2'])
    # Rückgabe: ({'Spieler 1': 0, 'Spieler 2': 0}, {'Spieler 1': [(1, 'Kreuz'),
    # (1, 'Pik'), (1, 'Herz')], 'Spieler 2': [(1, 'Karo'), (2, 'Kreuz'),
    # (2, 'Pik')]})

    # c)
    # play_game(['Spieler 1', 'Spieler 2', 'Spieler 3'], {'Spieler 1': 0,
    # 'Spieler 2': 0, 'Spieler 3': 0}, {'Spieler 1': [(1, 'Kreuz'), (1, 'Pik'),
    # (1, 'Herz')], 'Spieler 2': [(1, 'Karo'), (2, 'Kreuz'), (2, 'Pik')],
    # 'Spieler 3': [(2, 'Herz'), (2, 'Karo'), (3, 'Kreuz')]})
    # Spiel wird gespielt

    # play_game(['Spieler 1', 'Spieler 2', 'Spieler 3', 'Spieler 4'],
    # {'Spieler 1': 0, 'Spieler 2': 0, 'Spieler 3': 0, 'Spieler 4': 0},
    # {'Spieler 1': [(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Spieler 2':
    # [(1, 'Karo'), (2, 'Kreuz'), (2, 'Pik')], 'Spieler 3': [(2, 'Herz'),
    # (2, 'Karo'), (3, 'Kreuz')], 'Spieler 4': [(3, 'Pik'), (3, 'Herz'),
    # (3, 'Karo')]})
    # Spiel wird gespielt

    # play_game(['Spieler 1', 'Spieler 2'], {'Spieler 1': 0, 'Spieler 2': 0},
    # {'Spieler 1': [(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Spieler 2':
    # [(1, 'Karo'), (2, 'Kreuz'), (2, 'Pik')]})
    # Spiel wird gespielt

    # d)
    # check_card((1, 'Kreuz'), [(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Karo')
    # Rückgabe: True

    # check_card((1, 'Kreuz'), [(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Pik')
    # Rückgabe: False

    # check_card((1, 'Kreuz'), [(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Herz')
    # Rückgabe: True

    # e)
    # play_card([(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Karo')
    # Ausgabe: 1 (Karte wählen. Bei illegalem Zug wird dies wiederholt. (Nummer von 1 - 3): 1
    # Karte gespielt: (1, 'Kreuz')
    # Rückgabe: ((1, 'Kreuz'), [(1, 'Pik'), (1, 'Herz')])
    # (Kann auch anders aussehen)

    # play_card([(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Pik')
    # Ausgabe: 1 (Karte wählen. Bei illegalem Zug wird dies wiederholt. (Nummer von 1 - 3): 1
    # Karte gespielt: (1, 'Kreuz')
    # Rückgabe: ((1, 'Kreuz'), [(1, 'Pik'), (1, 'Herz')])
    # (Kann auch anders aussehen)

    # play_card([(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Herz')
    # Ausgabe: 1 (Karte wählen. Bei illegalem Zug wird dies wiederholt. (Nummer von 1 - 3): 1
    # Karte gespielt: (1, 'Kreuz')
    # Rückgabe: ((1, 'Kreuz'), [(1, 'Pik'), (1, 'Herz')])
    # (Kann auch anders aussehen)

    # f)
    # get_winner([(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Karo')
    # Rückgabe: 0

    # get_winner([(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Pik')
    # Rückgabe: 0

    # get_winner([(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz')], 'Herz')
    # Rückgabe: 0
