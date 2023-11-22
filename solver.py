import json

class Card(object):
    def __init__(self, number, shape, color, fill) -> None:
        self.number = number
        self.shape = shape
        self.color = color
        self.fill = fill
    
    def __str__(self) -> str:
        return f"{self.number}, {self.shape}, {self.color}, {self.fill}"
    
    def __repr__(self) -> str:
        return f"Card({self.number}, {self.shape}, {self.color}, {self.fill})"
    
    def __eq__(self, other_card) -> bool:
        if (self.number == other_card.number and self.shape == other_card.shape 
            and self.color == other_card.color and self.fill == other_card.fill):
            return True
        return False


class Table(object):
    def __init__(self, cards):
        self.cards = cards

        self.group_number: None | dict = None
        self.group_shape: None | dict = None
        self.group_color: None | dict = None
        self.group_fill: None | dict = None

        self.set_group_dicts()

    def __contains__(self, card) -> bool:
        '''
        checks whether or not this table contains the specified card
        '''
        if card in self.cards:
            return True
        return False

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

    def solved_sets(self) -> dict:
        # HERE IS THE THING
        pass


def load_table_json(table_id) -> dict:
    with open("example_tables.json") as f:
        table_json = json.load(f)[table_id]
    return table_json


def get_cards_json(table_id) -> list:
    table_json = load_table_json(table_id)
    cards = table_json["Cards"]
    return cards


def make_cards_list(cards) -> Table:
    '''
    :param cards: list of Card objects
    '''
    print("BAKSJFLE")
    print(cards[0])
    cards_list = [Card(**card) for card in cards]
    return cards_list


def check_solutions(table_id, solution) -> bool:
    '''
    This is where I can compare the solutions that my program comes up with against "Solution Sets" from the json file
    '''
    expected_solns_json = load_table_json(table_id)["Solution Sets"]
    expected_solns_list = [make_cards_list(soln) for soln in expected_solns_json]
    print(expected_solns_list)
    print()
    print(solution)
    print()
    # result = (solution == expected_solns_list)
    result = True

    return result



if __name__ == '__main__':
    # numbers = 1, 2, 3
    # shape = diamond, oval, squiggle
    # color = purple, green, red
    # fill = empty, striped, solid

    table_id = 1 # 0 is actual, 1 is smaller

    cards_list = make_cards_list(get_cards_json(table_id))
    table = Table(cards_list)

    ex_table_1_soln = [[Card("one", "diamond", "purple", "solid"),
                        Card("two", "diamond", "purple", "solid"),
                        Card("three", "diamond", "purple", "solid")
                        ]]

    # print(check_solutions(table_id, ex_table_1_soln))
    print(table.__contains__(Card("one", "oval", "red", "striped")))