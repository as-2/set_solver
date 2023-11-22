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


class Table(object):
    def __init__(self, cards):
        self.cards = cards

        self.group_number = None
        self.group_shape = None
        self.group_color = None
        self.group_fill = None

    def make_group_dicts(self) -> None:
        group_number_dict = {"one": [], "two": [], "three": []}
        group_shape_dict = {"diamond": [], "oval": [], "squiggle": []}
        group_color_dict = {"purple": [], "green": [], "red": []}
        group_fill_dict = {"empty": [], "striped": [], "solid": []}

        print(type(self.cards))
        
        for card in self.cards:
            group_number_dict[card.number].append(card)
            group_shape_dict[card.shape].append(card)
            group_color_dict[card.color].append(card)
            group_fill_dict[card.fill].append(card)
        
        print(group_number_dict)
        print()
        print(group_shape_dict)
        print()
        print(group_color_dict)
        print()
        print(group_fill_dict)
        return

    def solved_sets(self) -> dict:
        # HERE IS THE THING
        pass


def load_table_json(table_id) -> dict:
    with open("example_tables.json") as f:
        table_json = json.load(f)[table_id]
    return table_json


def make_table(table_id) -> Table:
    table_json = load_table_json(table_id)
    cards = table_json["Cards"]

    table_list = [Card(**card) for card in cards]

    return table_list

    

if __name__ == '__main__':
    # numbers = 1, 2, 3
    # shape = diamond, oval, squiggle
    # color = purple, green, red
    # fill = empty, striped, solid
    new_card = Card(2, "diamond", "purple", "striped")
    # print(new_card)

    table_list = make_table(0)
    # print(table_list)
    # for card in table_list:
    #     print(card)
    table = Table(table_list)
    print(table)
    table.make_group_dicts()