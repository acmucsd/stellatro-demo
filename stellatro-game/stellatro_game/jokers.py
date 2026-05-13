import random
from .card import Card, Rank, Suit, SUITS, rank_to_score
from typing import List, Tuple
from .checker import HandType, Checker
from itertools import product
import math


# Base class for jokers
class Joker:
    name: str
    description: str

    def pre_card_phase(self, hand: List[Card]) -> Tuple[List[Card]]:
        """Return (hand) after pre-phase application of joker."""
        return hand

    def apply_card_phase(
        self, chips: int, mult: int, rank: Rank, suit: Suit
    ) -> Tuple[int, int]:
        """Return (chips, mult) after hand evaluation application of joker."""
        return chips, mult

    def post_card_phase(
        self, chips: int, mult: int, hand: List[Card]
    ) -> Tuple[int, int]:
        """Return (chips, mult) after post-phase application of joker."""
        return chips, mult

    def __str__(self) -> str:
        return self.name + ": " + self.description


class RegularJoker(Joker):
    name = "Regular Joker"
    description = "No special abilities."


class PairMultBoost(Joker):
    name = "Jolly Joker"
    description = "Boost multiplier by 3 if the hand includes Pair."

    def post_card_phase(
        self, chips: int, mult: int, hand: List[Card]
    ) -> Tuple[int, int]:
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.PAIR,
            HandType.TWO_PAIR,
            HandType.THREE_OF_A_KIND,
            HandType.FULL_HOUSE,
            HandType.FOUR_OF_A_KIND,
        }:
            return chips, mult + 3
        return chips, mult


class PairChipBoost(Joker):
    name = "Sly Joker"
    description = "Add 30 chips if the hand includes Pair."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.PAIR,
            HandType.TWO_PAIR,
            HandType.THREE_OF_A_KIND,
            HandType.FULL_HOUSE,
            HandType.FOUR_OF_A_KIND,
        }:
            return chips + 10, mult
        return chips, mult


class TripletMultBoost(Joker):
    name = "Zany Joker"
    description = "+5 if the hand includes Three of a Kind."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.THREE_OF_A_KIND,
            HandType.FULL_HOUSE,
            HandType.FOUR_OF_A_KIND,
        }:
            return chips, mult + 5
        return chips, mult


class TwoPairMultBoost(Joker):
    name = "Cheeky Joker"
    description = "Boost multiplier by 4 if the hand includes Two Pair."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.TWO_PAIR,
            HandType.FULL_HOUSE,
            HandType.FOUR_OF_A_KIND,
        }:
            return chips, mult + 4
        return chips, mult


class StraightMultBoost(Joker):
    name = "Witty Joker"
    description = "Boost multiplier by 6 if the hand includes Straight."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.STRAIGHT,
            HandType.STRAIGHT_FLUSH,
        }:
            return chips, mult + 6
        return chips, mult


class FlushMultBoost(Joker):
    name = "Daring Joker"
    description = "Boost multiplier by 7 if the hand includes Flush."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.FLUSH,
            HandType.STRAIGHT_FLUSH,
        }:
            return chips, mult + 7
        return chips, mult


class TripletChipBoost(Joker):
    name = "Merry Joker"
    description = "Add 15 chips if the hand includes Three of a Kind."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.THREE_OF_A_KIND,
            HandType.FULL_HOUSE,
            HandType.FOUR_OF_A_KIND,
        }:
            return chips + 15, mult
        return chips, mult


class TwoPairChipBoost(Joker):
    name = "Jovial Joker"
    description = "Add 12 chips if the hand includes Two Pair."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.TWO_PAIR,
            HandType.FULL_HOUSE,
            HandType.FOUR_OF_A_KIND,
        }:
            return chips + 12, mult
        return chips, mult


class StraightChipBoost(Joker):
    name = "Lively Joker"
    description = "Add 20 chips if the hand includes Straight."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.STRAIGHT,
            HandType.STRAIGHT_FLUSH,
        }:
            return chips + 20, mult
        return chips, mult


class FlushChipBoost(Joker):
    name = "Vibrant Joker"
    description = "Add 25 chips if the hand includes Flush."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.FLUSH,
            HandType.STRAIGHT_FLUSH,
        }:
            return chips + 25, mult
        return chips, mult


class DiamondMultBoost(Joker):
    name = "Diamond Joker"
    description = "Played cards with Diamond suit boost multiplier by 2."

    def apply_card_phase(
        self, chips: int, mult: int, rank: Rank, suit: Suit
    ) -> Tuple[int, int]:
        if suit == Suit.DIAMOND:
            return chips, mult + 2
        return chips, mult


class HeartMultBoost(Joker):
    name = "Heart Joker"
    description = "Played cards with Heart suit boost multiplier by 2."

    def apply_card_phase(
        self, chips: int, mult: int, rank: Rank, suit: Suit
    ) -> Tuple[int, int]:
        if suit == Suit.HEART:
            return chips, mult + 2
        return chips, mult


class WishUponAStar(Joker):
    name = "Wish Upon a Star"
    description = "Lowest-ranked card gain 8 Stella before scoring."

    def pre_card_phase(self, hand: List[Card]) -> List[Card]:
        if not hand:
            return hand

        lowest_rank = min(card.rank for card in hand)
        for card in hand:
            if card.rank == lowest_rank:
                card.add_stella(8)
                break
        return hand


class Snowball(Joker):
    name="Snowball"
    description="+40 chips per stella"
    def post_card_phase(self, chips, mult, hand):
        total_stella = 0
        for card in hand:
            total_stella += card.stella
        return chips+40*total_stella,mult

ALL_JOKER_CLASSES = [
    RegularJoker,
    PairMultBoost,
    PairChipBoost,
    TripletMultBoost,
    TwoPairMultBoost,
    StraightMultBoost,
    FlushMultBoost,
    TripletChipBoost,
    TwoPairChipBoost,
    StraightChipBoost,
    FlushChipBoost,
    DiamondMultBoost,
    HeartMultBoost,
    WishUponAStar,
    Snowball,
]


def _instantiate_joker(joker_cls, rng=None) -> Joker:
    if rng is not None:
        try:
            return joker_cls(rng=rng)
        except TypeError:
            pass
    return joker_cls()


def generate_jokers(num_jokers: int, rng=None) -> List[Joker]:
    joker_classes = ALL_JOKER_CLASSES

    shuffler = rng or random
    joker_classes = joker_classes[:]
    shuffler.shuffle(joker_classes)
    return [
        _instantiate_joker(joker_classes[i % len(joker_classes)], rng=rng)
        for i in range(num_jokers)
    ]
