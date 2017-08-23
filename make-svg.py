#!/usr/bin/env python3
from math import ceil
from generator import generate_matrix, generate_cards, load_symbols


matrix = generate_matrix(6)
symbols = load_symbols(len(matrix[0]))
cards = generate_cards(matrix, symbols)

with open('cards/with-card-placeholders.svg') as templatefile:
    template = templatefile.read()

lists = []

lists = [template for _ in range(ceil(len(matrix) / 12))]

for cnum, card in enumerate(cards):
    listno = int(cnum / 12)
    cnum = cnum % 12 + 1
    for snum, symbol in enumerate(cards[0], 1):
        print('list {}, card {}, symbol {}, name {}'.format(listno, cnum, snum, symbol))
        toreplace = 'card{}-{}'.format(cnum, snum)

        lists[listno] = lists[listno].replace(toreplace, card[snum - 1])

for n, l in enumerate(lists):
    with open('list-{}.svg'.format(n), 'w') as cardfile:
        cardfile.write(l)
