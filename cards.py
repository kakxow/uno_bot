import dataclasses


colors = ["red", "blue", "yellow", "green"]
special_colors = ["black"]
values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
actions = ["skip", "draw_two", "reverse"]
special_actions = ["wild", "wild_draw_four"]


@dataclasses.dataclass
class Card:
    color: str
    value: int | None = None
    action: str = ""
    is_active: bool = True

    def __repr__(self):
        return f"{self.color} {self.action or self.value} {self.is_active}"


# cards = ([Card(color, number) for number in values for color in colors] +
#          [Card(color, number) for number in values[1:] for color in colors] +  # All number cards are doubled, but zeroes (values[1:])
#          [Card(color, None, action) for action in actions for color in colors] * 2 +
#          [Card(color, None, action) for action in special_actions for color in special_colors] * 4)
# with open("cards.txt", "w") as f:
#     print(*cards, sep="\n", file=f)

cards = (
    Card(color='red', value=0, action=""),
    Card(color='blue', value=0, action=""),
    Card(color='yellow', value=0, action=""),
    Card(color='green', value=0, action=""),
    Card(color='red', value=1, action=""),
    Card(color='blue', value=1, action=""),
    Card(color='yellow', value=1, action=""),
    Card(color='green', value=1, action=""),
    Card(color='red', value=2, action=""),
    Card(color='blue', value=2, action=""),
    Card(color='yellow', value=2, action=""),
    Card(color='green', value=2, action=""),
    Card(color='red', value=3, action=""),
    Card(color='blue', value=3, action=""),
    Card(color='yellow', value=3, action=""),
    Card(color='green', value=3, action=""),
    Card(color='red', value=4, action=""),
    Card(color='blue', value=4, action=""),
    Card(color='yellow', value=4, action=""),
    Card(color='green', value=4, action=""),
    Card(color='red', value=5, action=""),
    Card(color='blue', value=5, action=""),
    Card(color='yellow', value=5, action=""),
    Card(color='green', value=5, action=""),
    Card(color='red', value=6, action=""),
    Card(color='blue', value=6, action=""),
    Card(color='yellow', value=6, action=""),
    Card(color='green', value=6, action=""),
    Card(color='red', value=7, action=""),
    Card(color='blue', value=7, action=""),
    Card(color='yellow', value=7, action=""),
    Card(color='green', value=7, action=""),
    Card(color='red', value=8, action=""),
    Card(color='blue', value=8, action=""),
    Card(color='yellow', value=8, action=""),
    Card(color='green', value=8, action=""),
    Card(color='red', value=9, action=""),
    Card(color='blue', value=9, action=""),
    Card(color='yellow', value=9, action=""),
    Card(color='green', value=9, action=""),
    Card(color='red', value=1, action=""),
    Card(color='blue', value=1, action=""),
    Card(color='yellow', value=1, action=""),
    Card(color='green', value=1, action=""),
    Card(color='red', value=2, action=""),
    Card(color='blue', value=2, action=""),
    Card(color='yellow', value=2, action=""),
    Card(color='green', value=2, action=""),
    Card(color='red', value=3, action=""),
    Card(color='blue', value=3, action=""),
    Card(color='yellow', value=3, action=""),
    Card(color='green', value=3, action=""),
    Card(color='red', value=4, action=""),
    Card(color='blue', value=4, action=""),
    Card(color='yellow', value=4, action=""),
    Card(color='green', value=4, action=""),
    Card(color='red', value=5, action=""),
    Card(color='blue', value=5, action=""),
    Card(color='yellow', value=5, action=""),
    Card(color='green', value=5, action=""),
    Card(color='red', value=6, action=""),
    Card(color='blue', value=6, action=""),
    Card(color='yellow', value=6, action=""),
    Card(color='green', value=6, action=""),
    Card(color='red', value=7, action=""),
    Card(color='blue', value=7, action=""),
    Card(color='yellow', value=7, action=""),
    Card(color='green', value=7, action=""),
    Card(color='red', value=8, action=""),
    Card(color='blue', value=8, action=""),
    Card(color='yellow', value=8, action=""),
    Card(color='green', value=8, action=""),
    Card(color='red', value=9, action=""),
    Card(color='blue', value=9, action=""),
    Card(color='yellow', value=9, action=""),
    Card(color='green', value=9, action=""),
    Card(color='red', value=None, action='skip'),
    Card(color='blue', value=None, action='skip'),
    Card(color='yellow', value=None, action='skip'),
    Card(color='green', value=None, action='skip'),
    Card(color='red', value=None, action='draw_two'),
    Card(color='blue', value=None, action='draw_two'),
    Card(color='yellow', value=None, action='draw_two'),
    Card(color='green', value=None, action='draw_two'),
    Card(color='red', value=None, action='reverse'),
    Card(color='blue', value=None, action='reverse'),
    Card(color='yellow', value=None, action='reverse'),
    Card(color='green', value=None, action='reverse'),
    Card(color='red', value=None, action='skip'),
    Card(color='blue', value=None, action='skip'),
    Card(color='yellow', value=None, action='skip'),
    Card(color='green', value=None, action='skip'),
    Card(color='red', value=None, action='draw_two'),
    Card(color='blue', value=None, action='draw_two'),
    Card(color='yellow', value=None, action='draw_two'),
    Card(color='green', value=None, action='draw_two'),
    Card(color='red', value=None, action='reverse'),
    Card(color='blue', value=None, action='reverse'),
    Card(color='yellow', value=None, action='reverse'),
    Card(color='green', value=None, action='reverse'),
    Card(color='black', value=None, action='wild', is_active=False),
    Card(color='black', value=None, action='wild_draw_four'),
    Card(color='black', value=None, action='wild', is_active=False),
    Card(color='black', value=None, action='wild_draw_four'),
    Card(color='black', value=None, action='wild', is_active=False),
    Card(color='black', value=None, action='wild_draw_four'),
    Card(color='black', value=None, action='wild', is_active=False),
    Card(color='black', value=None, action='wild_draw_four'),
)
