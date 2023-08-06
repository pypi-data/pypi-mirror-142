"""

Project: AnyDeck python library
Author: Thomas Amore Jr
License: MIT
Purpose: Generate and handle a highly customizable deck of cards
Errata: If you make use of this library please send me a message and
        let me know what your made. I'd love to see it but if you don't
        want to that is just fine as well. Thanks for looking.

"""

import random

DEFAULT_SUITS = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
DEFAULT_CARDS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self,
                 face=None,
                 suit=None,
                 value=0,
                 suit_id=0,
                 suit_order_num=0,
                 child_order_num=None,
                 unique_card_num=None,
                 child_deck_num=None):
        self.face = face
        self.suit = suit
        self.value = value
        self.suit_id = suit_id
        self.suit_order_num = suit_order_num
        self.child_order_num = child_order_num
        self.unique_card_num = unique_card_num
        self.child_deck_num = child_deck_num


class AnyDeck:

    def __init__(self,
                 decks=1,
                 shuffled=False,
                 wilds=None,
                 suits=None,
                 cards=None,
                 special_cards=None,
                 override_defaults=False):

        if suits is None and cards is None and not override_defaults:
            suits, cards = DEFAULT_SUITS, DEFAULT_CARDS

        self._deck = []
        self._used_cards = []
        self._child_decks = decks
        self._shuffled = bool(shuffled)

        self._suits = self.__validate_input(suits)
        self._cards = self.__validate_input(cards)
        if type(wilds) is int:
            wilds = ['Wild'] * wilds
        self._wilds = self.__validate_input(wilds)
        self._special_cards = self.__validate_card(special_cards)

        self.new_deck(decks=self._child_decks,
                      shuffled=self._shuffled,
                      wilds=self._wilds,
                      suits=self._suits,
                      cards=self._cards,
                      special_cards=self._special_cards,
                      override_defaults=override_defaults)

        self._total_cards = len(self._deck)
        self._remaining_cards = len(self._deck)
        self.deck_info = self.get_deck_info()
        self._full_deck = self._deck.copy()

    @property
    def deck(self):
        return self._deck

    @property
    def used_cards(self):
        return self._used_cards

    @property
    def total_cards(self):
        return self._total_cards

    @property
    def remaining_cards(self):
        self._remaining_cards = len(self._deck)
        return self._remaining_cards

    @property
    def full_deck(self):
        return self._full_deck

    def new_deck(self,
                 decks=1,
                 shuffled=False,
                 wilds=None,
                 suits=None,
                 cards=None,
                 special_cards=None,
                 override_defaults=False,
                 retain_unused=False,
                 retain_used=False):

        if suits is None and cards is None and not override_defaults:
            suits, cards = DEFAULT_SUITS, DEFAULT_CARDS

        retained = []
        retained_info = dict()

        if retain_unused:
            retained = [card for card in self._deck]
            retained_info = self.get_deck_info()

        if not retain_used:
            self._used_cards.clear()

        self._deck.clear()

        self._child_decks = decks
        self._shuffled = bool(shuffled)
        self._suits = self.__validate_input(suits)
        self._cards = self.__validate_input(cards)
        if type(wilds) is int:
            wilds = ['Wild'] * wilds
        self._wilds = self.__validate_input(wilds)
        self._special_cards = self.__validate_card(special_cards)

        for card in retained:
            card.unique_card_num = len(self._deck) + 1
            self._deck.append(card)

        for card in self._special_cards:
            card.unique_card_num = len(self._deck) + 1
            self._deck.append(card)

        if len(self._suits) == 0:
            self._suits = ['']

        for child_deck_num in range(decks):
            deck_order_num = 1
            for suit_id, suit in enumerate(self._suits):
                for suit_order_num, face in enumerate(self._cards):
                    card = Card(face=face,
                                suit=suit,
                                value=self.__value_from_face(face),
                                suit_id=suit_id + 1,
                                suit_order_num=suit_order_num + 1,
                                child_order_num=deck_order_num,
                                unique_card_num=len(self._deck) + 1,
                                child_deck_num=child_deck_num + 1)
                    if suit == '':
                        card.suit = None
                    deck_order_num += 1
                    self._deck.append(card)

            if self._wilds:
                for wild in self._wilds:
                    card = Card(face=wild,
                                suit='Wild',
                                suit_order_num=0,
                                suit_id=0,
                                child_order_num=deck_order_num,
                                unique_card_num=len(self._deck) + 1,
                                child_deck_num=child_deck_num + 1)
                    deck_order_num += 1
                    self._deck.append(card)

        self._total_cards = len(self._deck)

        if shuffled:
            self.shuffle()

        if retain_unused:
            self._child_decks += retained_info.get('child_decks')

            self._suits = list(set(self._suits + retained_info.get('suits')))
            self._cards = list(set(self._cards + retained_info.get('cards')))
            self._wilds = list(set(self._wilds + retained_info.get('wilds')))
            self._special_cards = list(set(self._special_cards + retained_info.get('special_cards')))

        self.deck_info = self.get_deck_info()

        self._full_deck = self._deck.copy()

    def draw(self, position='top'):
        if len(self._deck) == 0:
            return None

        if type(position) is int:
            drawn_card = self._deck.pop(int(position))
        elif position.lower() == 'random':
            drawn_card = self._deck.pop(random.randrange(0, len(self._deck)))
        elif position.lower() == 'top':
            drawn_card = self._deck.pop(0)
        elif position.lower() == 'middle':
            drawn_card = self._deck.pop(int(len(self._deck) / 2))
        elif position.lower() == 'bottom':
            drawn_card = self._deck.pop(len(self._deck) - 1)
        else:
            raise Exception('position argument is invalid')

        self._used_cards.append(drawn_card)
        self._remaining_cards = len(self._deck)
        return drawn_card

    def draw_hand(self, cards, hands=1, alternating=True, refill=True):

        drawn_list = []

        if hands > 0:
            for _ in range(hands):
                drawn_list.append([])
            if alternating:
                for i in range(cards):
                    for j in range(hands):
                        if self.remaining_cards > 0:
                            drawn_list[j].append(self.draw())
                        elif self.remaining_cards <= 0 and refill:
                            self.replace_used_cards(shuffle=True)
                            if len(self.deck) <= 0:
                                for card in self._full_deck:
                                    self._deck.append(card)
                                self.shuffle()
                            drawn_list[j].append(self.draw())
                        else:
                            return drawn_list
            else:
                for i in range(hands):
                    for j in range(cards):
                        if self.remaining_cards > 0:
                            drawn_list[i].append(self.draw())
                        elif self.remaining_cards <= 0 and refill:
                            self.replace_used_cards(shuffle=True)
                            if len(self.deck) <= 0:
                                for card in self._full_deck:
                                    self._deck.append(card)
                                self.shuffle()
                            drawn_list[i].append(self.draw())
                        else:
                            return drawn_list

        return drawn_list

    def add_card(self, card, position='bottom'):

        if type(card) is Card:
            self._total_cards += 1
            card.unique_card_num = self._total_cards
            if type(position) is int:
                self._deck.insert(int(position), card)
            elif position.lower() == 'random':
                self._deck.insert(random.randrange(0, len(self._deck)), card)
            elif position.lower() == 'top':
                self._deck.insert(0, card)
            elif position.lower() == 'middle':
                self._deck.insert(int(len(self._deck) / 2), card)
            elif position.lower() == 'bottom':
                self._deck.append(card)
            else:
                raise Exception('position argument is invalid')
        else:
            raise Exception('added card must be of type \'Card\'')

    def shuffle(self):
        random.shuffle(self._deck)
        self._shuffled = True

    def replace_used_cards(self, shuffle=False, shuffle_used=False):
        if shuffle_used:
            random.shuffle(self._used_cards)
        for card in self._used_cards:
            self._deck.append(card)
        if shuffle:
            random.shuffle(self._deck)
        self._remaining_cards = len(self._deck)
        self._used_cards.clear()

    def dict_to_value(self, value_dict):
        for card in self._deck:
            if card.face in value_dict:
                card.value = value_dict.get(card.face)

    def get_deck_info(self):

        deck_info = {'child_decks': self._child_decks,
                     'suits': sorted(self._suits),
                     'cards': sorted(self._cards),
                     'wilds': sorted(self._wilds),
                     'special_cards': [sc.face for sc in self._special_cards if type(self._special_cards) is not None],
                     'total_cards': self._total_cards}
        return deck_info

    def clear_values(self):
        for card in self._deck:
            card.value = None

    @staticmethod
    def __value_from_face(face):

        try:
            if face.upper() in ['ACE']:
                value = 11
            elif face.upper() in ['KING', 'QUEEN', 'JACK']:
                value = 10
            elif str(face).isnumeric():
                value = int(face)
            else:
                value = 0
        except ValueError:
            value = 0

        return value

    @staticmethod
    def __validate_input(validate):
        output = []
        if validate is not None:
            if type(validate) is str:
                output.append(validate)
            else:
                output = [item for item in validate if type(item) is str]
                if len(output) != len(validate):
                    raise Exception('Non string item input')
        return output

    @staticmethod
    def __validate_card(validate):
        output = []
        if validate is not None:
            if type(validate) is Card:
                output.append(validate)
            else:
                output = [item for item in validate if type(item) is Card]
                if len(output) != len(validate):
                    raise Exception('Non card object input')
        return output
