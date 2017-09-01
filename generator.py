#!/usr/bin/env python3

import json
from os import path
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
    if filename is not None:
        symbols_names_path = path.join(path.dirname(path.abspath(__file__)),
                                       filename)

        with open(symbols_names_path) as fh:
            return iter(fh.read().split('\n')[:num])
    else:
        return iter(random_symbols(num))


# Scalar multiply a 3-tuple's elements (in field F, i.e. multiply modulo N)
def scalar_multiply(order, n, coords):
    return tuple(((coords[i] * n) % order for i in range(3)))


def is_representative(coords, P2F):
    return coords in P2F


def get_equvalence_class(order, coords, P2F):
    """Get representative vector of "coords"'s equivalence class"""
    for n in range(order):
        candidate = scalar_multiply(order, n, coords)
        if is_representative(candidate, P2F):
            return candidate
    assert False, "couldn't get equivalence class"


def generate_projection(order):
    # Get P^2(F) -- items are the representative vectors
    P2F = {(0, 0, 1)}
    P2F.update((0, 1, x) for x in range(order))
    P2F.update((1, x, y) for x in range(order) for y in range(order))

    P2F = sorted(P2F)

    lines = set()
    for x in P2F:
        for y in P2F:
            if x <= y:
                continue
            line = set()
            for kx in range(order):
                for ky in range(order):
                    if kx == ky == 0:
                        continue
                    tp = tuple(kx * x[i] + ky * y[i] for i in range(3))
                    line.add(get_equvalence_class(order, tp, P2F))
            lines.add(tuple(sorted(line)))
    return lines


def generate_cards(projection, symbols):
    mapping = {}
    cards = []
    for line in projection:
        card = []
        for point in line:
            try:
                card.append(mapping[point])
            except KeyError:
                next_project = next(symbols)
                mapping[point] = next_project
                card.append(next_project)
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
    parser.add_argument('-o', '--order', dest='order',
                        metavar='N', default=7, type=int,
                        help='Order of projection [2,3,5,7]')

    args = parser.parse_args()

    deck_size = args.order ** 2 + args.order + 1
    projection = generate_projection(args.order)

    # Generate random symbols or use file as source?
    if args.random:
        symbols_names = load_symbols(deck_size)
    else:
        symbols_names = load_symbols(deck_size, filename=args.symbols_file)

    cards = generate_cards(projection, symbols_names)

    print('{} cards/symbols with {} symbols on each'.format(len(cards), len(cards[0])))

    for card in cards:
        print(card)

    filename = '{}-output.json'.format(args.order)
    output_path = path.join(path.dirname(path.abspath(__file__)), filename)

    with open(output_path, 'w') as fh:
        fh.write(json.dumps(cards))
