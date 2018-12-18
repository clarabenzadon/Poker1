import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_number(self):
        i = 0
        while i < len(ranks):
            if self.rank == ranks[i]:
                return i
            i += 1

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def sort(self):
        i = 0
        while i < 4:
            if self.cards[i].get_number() < self.cards[i + 1].get_number():
                self.cards[i], self.cards[i + 1] = self.cards[i + 1], self.cards[i]
                i = 0
            else:
                i += 1

    def check_same_suit(self):
        for i in range(len(self.cards) - 1):
            if self.cards[i].get_suit() != self.cards[i + 1].get_suit():
                return False
        return True

    def check_flush(self):
        for i in range(len(self.cards) - 1):
            if self.cards[i].get_number() != self.cards[i + 1].get_number() + 1:
                return False
        return True

    def check_straight_flush(self):
        return self.check_same_suit() and self.check_flush()

    def check_play(self, play_counter):
        if hand.check_flush():                                             # CheckFlush
            if hand.check_same_suit():                                     # CheckStraightFlush
                if hand.cards[0].get_number == 12:                         # CheckRoyalFlush
                    play_counter["Royal Flush"] += 1
                else:
                    play_counter["Straight Flush"] += 1
            else:
                play_counter["Flush"] += 1
        else:
            for i in range(len(self.cards) - 1):
                if self.cards[i].get_rank() == self.cards[i + 1].get_rank():                        # CheckPair
                    if i < 3:
                        if self.cards[i+1].get_rank() == self.cards[i + 2].get_rank():              # CheckThree
                            if i < 2:
                                if self.cards[i+2].get_rank() == self.cards[i+3].get_rank():        # CheckFour
                                    play_counter["Four of a Kind"] += 1
                                    break
                                if i == 0 and self.cards[i+3].get_rank() == self.cards[i + 4].get_rank(): # CheckFullHouse
                                    play_counter["Full House"] += 1
                                    break
                                else:
                                    play_counter["Three of a Kind"] += 1
                                    break
                    if i < 2:
                        if self.cards[i + 2].get_rank() == self.cards[i + 3].get_rank():            # Check2Pairs
                            play_counter["Two Pair"] += 1
                            break
                        if i == 0:
                            if self.cards[i + 3].get_rank() == self.cards[i + 4].get_rank():
                                play_counter["Two Pair"] += 1
                                break
                    play_counter["Pair"] += 1
                    break
                if i == 3:                                                                          # HighCard
                    play_counter["High Card"] += 1
        return play_counter


play_counter = {"Royal Flush": 0, "Straight Flush": 0, "Four of a Kind": 0, "Full House": 0, "Flush": 0, "Three of a Kind": 0, "Two Pair": 0, "Pair": 0, "High Card": 0}

for i in range(50000):  # made it higher to increase the probabilities of getting straight flushes
    new_deck = Deck()
    new_deck.shuffle()
    hand = Hand(new_deck)
    hand.sort()
    play_counter = hand.check_play(play_counter)

print(play_counter)
