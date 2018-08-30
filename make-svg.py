#!/usr/bin/env python3
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from math import ceil
import os
import glob
import json
import sys


def generate_svgs(cards):
    with open('templates/with-card-placeholders.svg') as templatefile:
        template = templatefile.read()

    lists = []

    lists = [template for _ in range(ceil(len(cards) / 12))]

    for cnum, card in enumerate(cards):
        listno = int(cnum / 12)
        cnum = cnum % 12 + 1
        for snum, symbol in enumerate(card, 1):
            print('list {}, card {}, symbol {}, name {}'.format(listno, cnum,
                                                                snum, symbol))
            toreplace = 'card{}-{}'.format(cnum, snum)

            lists[listno] = lists[listno].replace(toreplace, card[snum - 1])

    for n, l in enumerate(lists):
        with open('list-{}.svg'.format(n), 'w') as cardfile:
            cardfile.write(l)


if __name__ == '__main__':

    parser = ArgumentParser(
        description='Dobble card SVG generator',
        formatter_class=ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-c', '--cards', dest='cards_file',
                        metavar='FILE', default=None, type=str,
                        help='JSON file with cards created by generator')

    args = parser.parse_args()

    if args.cards_file is None:
        print('Trying to find the newest generator output ...')
        json_files = glob.glob('*-output.json')
        try:
            cards_file = max(json_files, key=os.path.getctime)
        except ValueError:
            print('Cannot find generated JSON file.',
                  'Use -c to select input file manually')
            sys.exit(1)

    try:
        with open(args.cards_file) as fh:
            cards = json.load(fh)
    except:
        print('Cannot load cards from JSON file.')
        sys.exit(1)

    generate_svgs(cards)
