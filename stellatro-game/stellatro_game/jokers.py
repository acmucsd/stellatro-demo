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
    description = "+1 Mult if the hand includes Pair."

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
            return chips, mult + 1
        return chips, mult


class PairChipBoost(Joker):
    name = "Sly Joker"
    description = "+10 chips if the hand includes Pair."

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
    description = "+1 Mult if the hand includes Three of a Kind."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.THREE_OF_A_KIND,
            HandType.FULL_HOUSE,
            HandType.FOUR_OF_A_KIND,
        }:
            return chips, mult + 1
        return chips, mult


class TwoPairMultBoost(Joker):
    name = "Cheeky Joker"
    description = "+1 Mult if the hand includes Two Pair."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.TWO_PAIR,
            HandType.FULL_HOUSE,
            HandType.FOUR_OF_A_KIND,
        }:
            return chips, mult + 1
        return chips, mult


class StraightMultBoost(Joker):
    name = "Witty Joker"
    description = "+1 Mult if the hand includes Straight."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.STRAIGHT,
            HandType.STRAIGHT_FLUSH,
        }:
            return chips, mult + 1
        return chips, mult


class FlushMultBoost(Joker):
    name = "Daring Joker"
    description = "+1 Mult if the hand includes Flush."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.FLUSH,
            HandType.STRAIGHT_FLUSH,
        }:
            return chips, mult + 1
        return chips, mult


class TripletChipBoost(Joker):
    name = "Merry Joker"
    description = "+10 chips if the hand includes Three of a Kind."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.THREE_OF_A_KIND,
            HandType.FULL_HOUSE,
            HandType.FOUR_OF_A_KIND,
        }:
            return chips + 10, mult
        return chips, mult


class TwoPairChipBoost(Joker):
    name = "Jovial Joker"
    description = "+10 chips if the hand includes Two Pair."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.TWO_PAIR,
            HandType.FULL_HOUSE,
            HandType.FOUR_OF_A_KIND,
        }:
            return chips + 10, mult
        return chips, mult


class StraightChipBoost(Joker):
    name = "Lively Joker"
    description = "+10 chips if the hand includes Straight."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.STRAIGHT,
            HandType.STRAIGHT_FLUSH,
        }:
            return chips + 10, mult
        return chips, mult


class FlushChipBoost(Joker):
    name = "Vibrant Joker"
    description = "+10 chips if the hand includes Flush."

    def post_card_phase(self, chips, mult, hand):
        Checker_instance = Checker(hand)
        hand_type = Checker_instance.check()
        if hand_type in {
            HandType.FLUSH,
            HandType.STRAIGHT_FLUSH,
        }:
            return chips + 10, mult
        return chips, mult


class DiamondMultBoost(Joker):
    name = "Diamond Joker"
    description = "Scored cards with Diamond suit give +1 Mult."

    def apply_card_phase(
        self, chips: int, mult: int, rank: Rank, suit: Suit
    ) -> Tuple[int, int]:
        if suit == Suit.DIAMOND:
            return chips, mult + 1
        return chips, mult


class HeartMultBoost(Joker):
    name = "Heart Joker"
    description = "Scored cards with Heart suit give +1 Mult."

    def apply_card_phase(
        self, chips: int, mult: int, rank: Rank, suit: Suit
    ) -> Tuple[int, int]:
        if suit == Suit.HEART:
            return chips, mult + 1
        return chips, mult


class WishUponAStar(Joker):
    name = "Wish Upon a Star"
    description = "Lowest-ranked card in played hand gain 1 Stella before scoring."

    def pre_card_phase(self, hand: List[Card]) -> List[Card]:
        if not hand:
            return hand

        lowest_rank = min(card.rank for card in hand)
        for card in hand:
            if card.rank == lowest_rank:
                card.add_stella(1)
                break
        return hand


class Snowball(Joker):
    name="Snowball"
    description="+10 chips per stella in hand"
    def post_card_phase(self, chips, mult, hand):
        total_stella = 0
        for card in hand:
            total_stella += card.stella
        return chips+10*total_stella,mult

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
