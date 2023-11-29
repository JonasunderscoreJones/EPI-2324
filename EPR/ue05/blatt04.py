'''EPR Übungsblatt 04'''
__author__="7987847, Werner"

import random

# a)
def create_card_list(number_of_cards:int) -> [(int, str)]:
    '''Erzeugt eine Liste mit Karten mit den vier Farben
    und Zahlen von 1 bis number_of_cards
    number_of_cards: Anzahl der Karten
    '''
    card_list = []
    for i in range(1, int((number_of_cards+1)/4)+1):
        card_list.append((i, "Kreuz"))
        card_list.append((i, "Pik"))
        card_list.append((i, "Herz"))
        card_list.append((i, "Karo"))
    return card_list


# b)
def shuffle_card_list(cards:[(int, str)]) -> [(int, str)]:
    '''Mischt eine Liste mit Karten
    cards: Liste mit Karten
    '''
    random.shuffle(cards)
    return cards


# c)
def compare_two_cards(card_one:(int, str), card_two:(int, str)) -> int:
    '''Vergleicht zwei Karten
    card_one: Erste Karte
    card_two: Zweite Karte
    '''
    if card_one[0] < card_two[0]:
        return 0
    if card_one[0] == card_two[0]:
        return 1
    return 2


# d)
def compare_two_cards_trump(card_one:(int, str), card_two:(int, str),
trump:str) -> int:
    '''Vergleiche Zwei Karten mit dem Trumpf
    '''
    if card_one[1] == trump and card_two[1] != trump:
        return 0
    if card_one[1] != trump and card_two[1] == trump:
        return 1
    return compare_two_cards(card_one, card_two)


# e)
def hand_out_cards(list_cards: [(int, str)], players: int, number_of_cards:
int) -> [[(int, str)]]:
    '''Teilt die Karten an die Spieler aus
    list_cards: Liste mit Karten
    players: Anzahl der Spieler
    number_of_cards: Anzahl der Karten pro Spieler
    '''
    list_players = []
    for _ in range(players):
        list_players.append([])

    for _ in range(number_of_cards):
        for j in range(players):
            list_players[j].append(list_cards.pop(0))

    return list_players


def main():
    '''Hauptprogramm'''
    # Testfälle

    # a)
    # create_card_list(0)
    # Rückgabe: []

    # create_card_list(32)
    # Rückgabe: [(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz'), (1, 'Karo'),
    # (2, 'Kreuz'), (2, 'Pik'), (2, 'Herz'), (2, 'Karo'), (3, 'Kreuz'),
    # (3, 'Pik'), (3, 'Herz'), (3, 'Karo'), (4, 'Kreuz'), (4, 'Pik'),
    # (4, 'Herz'), (4, 'Karo'), (5, 'Kreuz'), (5, 'Pik'), (5, 'Herz'),
    # (5, 'Karo'), (6, 'Kreuz'), (6, 'Pik'), (6, 'Herz'), (6, 'Karo'),
    # (7, 'Kreuz'), (7, 'Pik'), (7, 'Herz'), (7, 'Karo'), (8, 'Kreuz'),
    # (8, 'Pik'), (8, 'Herz'), (8, 'Karo')]

    # create_card_list(-10)
    # Rückgabe: []

    # b)
    # shuffle_card_list([])
    # Rückgabe: []

    # shuffle_card_list([(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz'), (1, 'Karo'),
    # (2, 'Kreuz'), (2, 'Pik'), (2, 'Herz'), (2, 'Karo'), (3, 'Kreuz'),
    # (3, 'Pik'), (3, 'Herz'), (3, 'Karo'), (4, 'Kreuz'), (4, 'Pik'),
    # (4, 'Herz'), (4, 'Karo'), (5, 'Kreuz'), (5, 'Pik'), (5, 'Herz'),
    # (5, 'Karo'), (6, 'Kreuz'), (6, 'Pik'), (6, 'Herz'), (6, 'Karo'),
    # (7, 'Kreuz'), (7, 'Pik'), (7, 'Herz'), (7, 'Karo'), (8, 'Kreuz'),
    # (8, 'Pik'), (8, 'Herz'), (8, 'Karo')])
    # Rückgabe: [(6, 'Pik'), (1, 'Kreuz'), (4, 'Karo'), (5, 'Kreuz'),
    # (8, 'Karo'), (6, 'Herz'), (3, 'Herz'), (1, 'Herz'), (4, 'Pik'),
    # (8, 'Pik'), (2, 'Kreuz'), (5, 'Pik'), (3, 'Karo'), (2, 'Herz'),
    # (7, 'Pik'), (2, 'Pik'), (7, 'Herz'), (1, 'Pik'), (8, 'Herz'),
    # (7, 'Karo'), (6, 'Karo'), (5, 'Herz'), (4, 'Herz'), (3, 'Pik'),
    # (2, 'Karo'), (5, 'Karo'), (6, 'Kreuz'), (1, 'Karo'), (8, 'Kreuz'),
    # (3, 'Kreuz'), (7, 'Kreuz'), (4, 'Kreuz')]
    # (Kann auch anders aussehen)

    # shuffle_card_list([(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz'), (1, 'Karo')]
    # Rückgabe: [(1, 'Pik'), (1, 'Kreuz'), (1, 'Karo'), (1, 'Herz')]
    # (Kann auch anders aussehen)

    # c)
    # compare_two_cards((1, 'Kreuz'), (1, 'Pik'))
    # Rückgabe: 1

    # compare_two_cards((1, 'Kreuz'), (2, 'Pik'))
    # Rückgabe: 0
    # compare_two_cards(('Pik), (1))
    # Rückgabe: TypeError: 'int' object is not subscriptable

    # d)
    # compare_two_cards_trump((1, 'Kreuz'), (1, 'Pik'), 'Kreuz')
    # Rückgabe: 1

    # compare_two_cards_trump((1, 'Kreuz'), (1, 'Pik'), 'Pik')
    # Rückgabe: 0

    # compare_two_cards_trump((1, 'Kreuz'), (1, 'Pik'), 'Herz')
    # Rückgabe: 0

    # e)
    # hand_out_cards([(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz'), (1, 'Karo'),
    # (2, 'Kreuz'), (2, 'Pik'), (2, 'Herz'), (2, 'Karo'), (3, 'Kreuz'),
    # (3, 'Pik'), (3, 'Herz'), (3, 'Karo'), (4, 'Kreuz'), (4, 'Pik'),
    # (4, 'Herz'), (4, 'Karo'), (5, 'Kreuz'), (5, 'Pik'), (5, 'Herz'),
    # (5, 'Karo'), (6, 'Kreuz'), (6, 'Pik'), (6, 'Herz'), (6, 'Karo'),
    # (7, 'Kreuz'), (7, 'Pik'), (7, 'Herz'), (7, 'Karo'), (8, 'Kreuz'),
    # (8, 'Pik'), (8, 'Herz'), (8, 'Karo')], 0, 0)

    # Rückgabe: []

    # hand_out_cards([(1, 'Kreuz'), (1, 'Pik'), (1, 'Herz'), (1, 'Karo'),
    # (2, 'Kreuz'), (2, 'Pik'), (2, 'Herz'), (2, 'Karo'), (3, 'Kreuz'),
    # (3, 'Pik'), (3, 'Herz'), (3, 'Karo'), (4, 'Kreuz'), (4, 'Pik'),
    # (4, 'Herz'), (4, 'Karo'), (5, 'Kreuz'), (5, 'Pik'), (5, 'Herz'),
    # (5, 'Karo'), (6, 'Kreuz'), (6, 'Pik'), (6, 'Herz'), (6, 'Karo'),
    # (7, 'Kreuz'), (7, 'Pik'), (7, 'Herz'), (7, 'Karo'), (8, 'Kreuz'),
    # (8, 'Pik'), (8, 'Herz'), (8, 'Karo')], 4, 0)

    # Rückgabe: [[], [], [], []]

    # hand_out_cards([], 4, 4)

    # Rückgabe: IndexError: pop from empty list

    print("Es wird ein Kartenspiel erstellt.")
    print("Geben Sie die Anzahl der Spieler ein.")
    players = int(input("Anzahl der Spieler: "))
    print("Geben Sie die Anzahl der Karten ein.")
    number_of_cards = int(input("Anzahl der Karten: "))
    print("Geben Sie den Trumpf ein.")
    trump = input("Trumpf: ")

    card_list = create_card_list(number_of_cards)
    card_list = shuffle_card_list(card_list)
    player_list = hand_out_cards(card_list, players, number_of_cards)

    print("Die Karten werden ausgegeben.")

    for i in range(players):
        print("Spieler " + str(i + 1) + ":")
        for j in range(number_of_cards):
            print(player_list[i][j], end=" ")
        print()

    print("Es werden die Karten mit dem Trumpf verglichen.")

    for i in range(players):
        print("Spieler " + str(i + 1) + ":")
        for j in range(number_of_cards):
            if player_list[i][j][1] == trump:
                print(player_list[i][j], end=" ")
        print()

if __name__ == '__main__':
    main()
