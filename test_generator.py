import pytest
from itertools import combinations
from generator import generate_projection, generate_cards, load_symbols


# Returns generated projection with size depending on param
@pytest.fixture(scope="module", params=[2, 3, 5, 7])
def projection(request):
    return request.param, generate_projection(request.param)


# Return projection with mapped symbols depending on param
# None - return projection without mapping to names
# True - Use random generated symbols for mapping
# str(filename) - use symbols from file for mapping
@pytest.fixture(scope="module", params=[None, True, 'list_of_projects.txt'])
def cards(request, projection):
    if request.param is None:
        return projection
    elif request.param is True:
        order, projection = projection
        num_symbols = order ** 2 + order + 1
        symbols = load_symbols(num_symbols)
        return order, generate_cards(projection, symbols)
    elif isinstance(request.param, str):
        order, projection = projection
        num_symbols = order ** 2 + order + 1
        symbols = load_symbols(num_symbols, filename=request.param)
        return order, generate_cards(projection, symbols)


def test_num_of_cards(cards):
    order, cards = cards
    assert order ** 2 + order + 1 == len(cards)


def test_each_card_length(cards):
    order, cards = cards
    right_count = order + 1
    assert all([False for card in cards if len(card) != right_count])


def test_right_num_of_uniq_symbols(cards):
    order, cards = cards
    uniq_symbols = order ** 2 + order + 1

    all_symbols = []
    for card in cards:
        all_symbols.extend(card)
    assert len(set(all_symbols)) == uniq_symbols


def test_all_pairs(cards):
    order, cards = cards
    all_combinations = combinations(cards, 2)

    for comb in all_combinations:
        card1, card2 = comb
        assert len(set(card1) & set(card2)) == 1
