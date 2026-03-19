"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ["J","Q","K"]:
       return 10
    if card in ["A"]:
       return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    value1 = value_of_card(card_one)
    value2 = value_of_card(card_two)
    if value1 > value2:
        return card_one
    if value1 == value2:
        return (card_one, card_two)
    return card_two



def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
def is_blackjack(card_one, card_two):
    """判断是否黑杰克（两张牌总点数为21，A按11算）"""
    def card_value(card):
        if card == 'A':
            return 11
        if card in ['J', 'Q', 'K']:
            return 10
        return int(card)

    return card_value(card_one) + card_value(card_two) == 21

def value_of_ace(card_one, card_two):
    """计算新拿到的A应该取1还是11，使手牌不超过21且尽可能大"""
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        if card == 'A':
            return 11   # 计算已有手牌时A暂按11
        return int(card)

    total = card_value(card_one) + card_value(card_two)
    # 若加11不爆则返回11，否则返回1
    return 11 if total + 11 <= 21 else 1

def can_split_pairs(card_one, card_two):
    """能否分牌：两张牌点数相同（value_of_card规则）"""
    return value_of_card(card_one) == value_of_card(card_two)



def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

def can_double_down(card_one, card_two):
    """能否加倍：手牌点数（考虑A的两种取值）存在9、10或11"""
    def possible_values(card):
        if card == 'A':
            return [1, 11]
        return [value_of_card(card)]   # J/Q/K已由value_of_card返回10

    totals = []
    for v1 in possible_values(card_one):
        for v2 in possible_values(card_two):
            s = v1 + v2
            if s <= 21:
                totals.append(s)

    return any(t in (9, 10, 11) for t in totals)

