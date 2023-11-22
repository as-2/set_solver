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

    def group_number(self) -> dict:
        group_number_dict = {}
        pass
    
    def group_shape(self) -> dict:
        pass

    def group_color(self) -> dict:
        # creates a new cards dict that groups them by color
        # {'green':{...}, 'red':{...}, ...}
        pass

    def group_fill(self) -> dict:
        pass

    def solved_sets(self) -> dict:
        # HERE IS THE THING
        pass


def load_table_json(table_id) -> dict:
    with open("example_tables.json") as f:
        table_json = json.load(f)[table_id]
    print(type(table_json))
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
    print(new_card)

    table_list = make_table(0)
    print(table_list)
    for card in table_list:
        print(card)