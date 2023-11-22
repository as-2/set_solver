import json
from itertools import combinations

class Card(object):
    def __init__(self, number, shape, color, fill) -> None:
        self.number = number
        self.shape = shape
        self.color = color
        self.fill = fill
    
    def __str__(self) -> str:
        return f"{self.number}, {self.shape}, {self.color}, {self.fill}"
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.number!r}, {self.shape!r}, {self.color!r}, {self.fill!r})"
    
    def __eq__(self, other_card) -> bool:
        if (self.number == other_card.number and self.shape == other_card.shape 
            and self.color == other_card.color and self.fill == other_card.fill):
            return True
        return False


class Card_Collection(object):
    def __init__(self, cards) -> None:
        self.cards = cards

    def __eq__(self, other_cards) -> bool:
        if len(self.cards) != len(other_cards):
            return False
        for card in self.cards:
            if card not in other_cards:
                return False
        return True
    
    def __contains__(self, card) -> bool:
        '''
        checks whether or not this collection contains the specified card
        '''
        if card in self.cards:
            return True
        return False
    
    def __len__(self) -> int:
        return len(self.cards)
    
    def __iter__(self):
        return iter(self.cards)

    def __str__(self) -> str:
        return f"{self.cards}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.cards})"


class Table(Card_Collection):
    def __init__(self, cards: list | Card_Collection):
        super().__init__(cards)
        # self.cards = cards

        self.group_number: None | dict = None
        self.group_shape: None | dict = None
        self.group_color: None | dict = None
        self.group_fill: None | dict = None

        self.set_group_dicts()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.cards})"

    def set_group_dicts(self) -> None:
        group_number_dict = {"one": [], "two": [], "three": []}
        group_shape_dict = {"diamond": [], "oval": [], "squiggle": []}
        group_color_dict = {"purple": [], "green": [], "red": []}
        group_fill_dict = {"empty": [], "striped": [], "solid": []}
        
        for card in self.cards:
            group_number_dict[card.number].append(card)
            group_shape_dict[card.shape].append(card)
            group_color_dict[card.color].append(card)
            group_fill_dict[card.fill].append(card)
        
        self.group_number = group_number_dict
        self.group_shape = group_shape_dict
        self.group_color = group_color_dict
        self.group_fill = group_fill_dict
        return

    def card_combinations(self) -> list:
        '''
        With 12 cards, should always have len = 220
        '''
        combos = list(combinations(self.cards, 3))
        return combos

    def solved_sets(self) -> list:
        # HERE IS THE THING
        # should return a list of Card_Collections
        # each Card_Collection object should have solution sets
        solutions = []
        return solutions


def load_table_json(table_id:int) -> dict:
    '''
    Loads the specified table_id from JSON file and returns entire table
    '''
    with open("example_tables.json") as f:
        table_json = json.load(f)[table_id]
    return table_json


def get_cards_json(table_id:int) -> list:
    '''
    Loads the specified table_id from the JSON file and returns list of cards
    '''
    table_json = load_table_json(table_id)
    cards = table_json["Cards"]
    return cards


def make_cards_list(cards:list) -> list:
    '''
    :param cards: list of Card objects
    '''
    cards_list = [Card(**card) for card in cards]
    return cards_list


def compare_cards(cards_1: Table | Card_Collection, cards_2: Table | Card_Collection) -> bool:
    """
    Given two collections of cards, returns bool whether or not they contain the same cards
    """
    return (cards_1 == cards_2)


def check_solutions(table_id:int, solutions:list) -> bool:
    '''
    This is where I can compare the solutions that my program comes up with against "Solution Sets" from the json file;
    Program must get EVERY solution set, or returns False
    :param table_id: 
    :param solutions: list of Card_Collection objects
    '''
    expected_solns_json = load_table_json(table_id)["Solution Sets"]
    expected_solns_list = [Card_Collection(make_cards_list(soln)) for soln in expected_solns_json]

    for expected_soln in expected_solns_list:
        if expected_soln not in solutions:
            return False

    return True



if __name__ == '__main__':
    # numbers = one, two, three
    # shape = diamond, oval, squiggle
    # color = purple, green, red
    # fill = empty, striped, solid

    table_id = 0 # 0 is actual, 1 is smaller

    cards_list = make_cards_list(get_cards_json(table_id))
    table1 = Table(cards_list)
    # print(table1)
    # print()

    table2 = Table(Card_Collection(cards_list))
    # print(table2)

    ex_table_2_solns = [Card_Collection([Card('two', 'diamond', 'purple', 'empty'), Card('two', 'oval', 'green', 'solid'), Card('two', 'squiggle', 'red', 'striped')]),
      Card_Collection([Card('three', 'squiggle', 'red', 'solid'), Card('one', 'diamond', 'green', 'solid'), Card('two', 'oval', 'purple', 'solid')]),
      Card_Collection([Card('one', 'squiggle', 'green', 'solid'), Card('three', 'diamond', 'green', 'solid'), Card('two', 'oval', 'green', 'solid')]),
      Card_Collection([Card('two', 'squiggle', 'red', 'striped'), Card('two', 'diamond', 'green', 'empty'), Card('two', 'oval', 'purple', 'solid')]),
      Card_Collection([Card('two', 'squiggle', 'green', 'empty'), Card('one', 'squiggle', 'purple', 'striped'), Card('three', 'squiggle', 'red', 'solid')]),
      Card_Collection([Card('three', 'diamond', 'red', 'empty'), Card('one', 'squiggle', 'purple', 'striped'), Card('two', 'oval', 'green', 'solid')])]

    ex_table_1_solns = [[Card("one", "diamond", "purple", "solid"),
                        Card("two", "diamond", "purple", "solid"),
                        Card("three", "diamond", "purple", "solid")
                        ]]

    # print(check_solutions(table_id, ex_table_2_solns))
    # print(compare_cards(table1, table2))
    combos = Table.card_combinations(table1)
    combos_ = [Card('two', 'squiggle', 'red', 'striped'), Card('two', 'diamond', 'purple', 'empty'), Card('one', 'squiggle', 'green', 'solid')]
    print(combos[0])
    print()
    print(combos_)
    # print(combos[0])
    print(compare_cards(Card_Collection(combos_), Card_Collection(combos[0])))
    # print(type(combos))