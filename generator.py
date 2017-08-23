#!/usr/bin/env python3

from os import path
from itertools import combinations
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from string import ascii_uppercase, ascii_lowercase, digits
from random import choice


def random_symbols(num):
    chars = ascii_uppercase + ascii_lowercase + digits
    result = []
    while len(result) < num:
        symbol = ''.join(choice(chars) for _ in range(2))
        if symbol not in result:
            result.append(symbol)
    return result


def load_symbols(num, filename=None):
    if filename:
        symbols_names_path = path.join(path.dirname(path.abspath(__file__)),
                                       filename)

        with open(symbols_names_path) as fh:
            return fh.read().split('\n')[:num]
    else:
        return random_symbols(num)


def get_column(matrix, column):
    return [row[column] for row in matrix]


def check_validity(matrix, maximum, row_num):

    # Stop, if we have more than allowed symbols on one card
    for row in matrix[:row_num + 1]:
        if sum(row) > maximum:
            return False, 'row'

    # Stop if we have one symbol on more cards than allowed
    for x in range(len(matrix[0])):
        if sum(get_column(matrix, x)) > maximum:
            return False, 'column'

    all_pairs = list(combinations(matrix[:row_num + 1], 2))

    # Stop, if some pair of cards has more than one in common
    for row1, row2 in all_pairs:
        common = 0
        for x, y in zip(row1, row2):
            if x == y == 1:
                common += 1
        if common > 1:
            return False, 'more than one in common {} {} - {} and {} '.format(matrix.index(row1), matrix.index(row2), row1, row2)

    return True, None


def generate_matrix(symbols_per_card):
    add_symbols = 0
    while True:
        # Calculate matrix size and fill first row
        cards = symbols_per_card * (symbols_per_card - 1) + 1
        symbols = cards + add_symbols
        matrix = [list(map(int, list('0' * symbols))) for _ in range(cards)]
        first_row = list('1' * symbols_per_card) + list('0' * (symbols - symbols_per_card))
        first_row = list(map(int, first_row))
        matrix[0] = first_row

        # Try to change every cell and check validity
        for x in range(1, cards):
            for y in range(symbols):
                matrix[x][y] = 1
                valid, reason = check_validity(matrix, symbols_per_card, x)
                if not valid:
                    matrix[x][y] = 0
                    if reason == 'row':
                        break
            # Check if we have right amount of symbols on the last card
            # if not, extend number of symbols and start again
            if sum(matrix[x]) != symbols_per_card:
                add_symbols += 1
                break
        else:
            return matrix


def generate_cards(matrix, symbols):
    if len(matrix[0]) > len(symbols):
        raise ValueError(
            'Not enough symbols provided. Minimum is {}'.format(len(matrix[0]))
        )

    cards = []
    for row in matrix:
        card = []
        for num, x in enumerate(row):
            if x == 1:
                card.append(symbols[num])
        cards.append(card)

    return cards


if __name__ == '__main__':

    parser = ArgumentParser(
        description='Dobble card generator',
        formatter_class=ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-r', '--random', dest='random',
                        default=False, action='store_true',
                        help='Generate symbols randomly')
    parser.add_argument('-f', '--symbols_file', dest='symbols_file',
                        metavar='FILE', default='list_of_projects.txt',
                        type=str, help='File with symbols names')
    parser.add_argument('-s', '--symbols_per_card', dest='symbols_per_card',
                        metavar='N', default=4, type=int,
                        help='How many symbols per card')

    args = parser.parse_args()

    matrix = generate_matrix(args.symbols_per_card)
    deck_size = len(matrix[0])

    # Generate random symbols or use file as source?
    if args.random:
        symbols_names = load_symbols(deck_size)
    else:
        symbols_names = load_symbols(deck_size, args.symbols_file)

    cards = generate_cards(matrix, symbols_names)

    print('{} cards with {} symbols on each and {} total symbols'.format(len(cards), len(cards[0]), len(matrix[0])))
    for card in cards:
        print(card)
