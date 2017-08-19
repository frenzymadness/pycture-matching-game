#!/usr/bin/env python3

# This program generates the set of n^2+n+1 cards to play the Spot It
# (aka Dobble) game for all n power of prime.

# This set of cards has below properties that are those of a projective
# plane of order n:

# There are n^2+n+1 cards and n^2+n+1 symbols
# Each card contains n+1 symbols
# Each symbol appears on n+1 cards
# Every two cards have exactly one symbol in common
# For every two symbols there is exactly one card that has both of them

import sys
from os import path
from itertools import combinations
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from string import ascii_uppercase, ascii_lowercase, digits
from random import choice


def is_prime(n):
    return all(n % i for i in range(2, n))


def random_symbols(num):
    chars = ascii_uppercase + ascii_lowercase + digits
    result = []
    while len(result) < num:
        symbol = ''.join(choice(chars) for _ in range(2))
        if symbol not in result:
            result.append(symbol)
    return result


def generator(symbols, symbols_per_card):
    result = []
    cards = list(combinations(symbols, symbols_per_card))
    while len(cards):
        # print('Round started with {} cards'.format(len(cards)))
        result.append(cards[0])
        next_round = []
        for card in cards:
            if len(set(card) & set(cards[0])) == 1:
                # print('{} and {} have union equal 1'.format(cards[0], card))
                next_round.append(card)
        cards = next_round

    return result


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
    parser.add_argument('-n', '--number', dest='number',
                        metavar='N', default=5, type=int,
                        help='The prime number to base generator on.')

    args = parser.parse_args()

    if not is_prime(args.number):
        print('Input has to be prime number!')
        sys.exit(1)

    # Calculate amount of cards and amount of symbols per one card
    amount_of_cards = args.number ** 2 + args.number + 1
    symbols_per_card = args.number + 1

    # Generate random symbols or use file as source?
    if args.random:
        symbols_names = random_symbols(amount_of_cards)
    else:
        symbols_names_file = path.join(path.dirname(path.abspath(__file__)),
                                       args.symbols_file)

        with open(symbols_names_file) as fh:
            symbols_names = fh.read().split('\n')[:amount_of_cards]

    if len(symbols_names) < amount_of_cards:
        print('Amount of symbols are too low. You have to provide at least {} symbols.'.format(amount_of_cards))
        sys.exit(1)

    cards = generator(symbols_names, symbols_per_card)

    print('{} cards/symbols generated. Each card contains {} symbols'.format(amount_of_cards, symbols_per_card))

    for card in cards:
        print(card)
