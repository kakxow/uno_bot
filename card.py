import dataclasses


colors = ["red", "blue", "yellow", "green"]
special_colors = ["black"]
values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
actions = ["skip", "draw_two", "reverse"]
special_actions = ["wild", "wild_draw_four"]
addon_actions = ["wild_swap_hands", "wild_shuffle_hands"]
scores = {
    "skip": 20,
    "draw_two": 20,
    "reverse": 20,
    "wild": 50,
    "wild_draw_four": 50,
    "wild_swap_hands": 40,
    "wild_shuffle_hands": 40,
}


@dataclasses.dataclass
class Card:
    color: str
    value: int | None = None
    action: str = ""
    is_active: bool = True

    def __repr__(self):
        return f"{self.color} {self.action or self.value}"


cards = (
    Card(color="red", value=0, action=""),
    Card(color="blue", value=0, action=""),
    Card(color="yellow", value=0, action=""),
    Card(color="green", value=0, action=""),
    Card(color="red", value=1, action=""),
    Card(color="blue", value=1, action=""),
    Card(color="yellow", value=1, action=""),
    Card(color="green", value=1, action=""),
    Card(color="red", value=2, action=""),
    Card(color="blue", value=2, action=""),
    Card(color="yellow", value=2, action=""),
    Card(color="green", value=2, action=""),
    Card(color="red", value=3, action=""),
    Card(color="blue", value=3, action=""),
    Card(color="yellow", value=3, action=""),
    Card(color="green", value=3, action=""),
    Card(color="red", value=4, action=""),
    Card(color="blue", value=4, action=""),
    Card(color="yellow", value=4, action=""),
    Card(color="green", value=4, action=""),
    Card(color="red", value=5, action=""),
    Card(color="blue", value=5, action=""),
    Card(color="yellow", value=5, action=""),
    Card(color="green", value=5, action=""),
    Card(color="red", value=6, action=""),
    Card(color="blue", value=6, action=""),
    Card(color="yellow", value=6, action=""),
    Card(color="green", value=6, action=""),
    Card(color="red", value=7, action=""),
    Card(color="blue", value=7, action=""),
    Card(color="yellow", value=7, action=""),
    Card(color="green", value=7, action=""),
    Card(color="red", value=8, action=""),
    Card(color="blue", value=8, action=""),
    Card(color="yellow", value=8, action=""),
    Card(color="green", value=8, action=""),
    Card(color="red", value=9, action=""),
    Card(color="blue", value=9, action=""),
    Card(color="yellow", value=9, action=""),
    Card(color="green", value=9, action=""),
    Card(color="red", value=1, action=""),
    Card(color="blue", value=1, action=""),
    Card(color="yellow", value=1, action=""),
    Card(color="green", value=1, action=""),
    Card(color="red", value=2, action=""),
    Card(color="blue", value=2, action=""),
    Card(color="yellow", value=2, action=""),
    Card(color="green", value=2, action=""),
    Card(color="red", value=3, action=""),
    Card(color="blue", value=3, action=""),
    Card(color="yellow", value=3, action=""),
    Card(color="green", value=3, action=""),
    Card(color="red", value=4, action=""),
    Card(color="blue", value=4, action=""),
    Card(color="yellow", value=4, action=""),
    Card(color="green", value=4, action=""),
    Card(color="red", value=5, action=""),
    Card(color="blue", value=5, action=""),
    Card(color="yellow", value=5, action=""),
    Card(color="green", value=5, action=""),
    Card(color="red", value=6, action=""),
    Card(color="blue", value=6, action=""),
    Card(color="yellow", value=6, action=""),
    Card(color="green", value=6, action=""),
    Card(color="red", value=7, action=""),
    Card(color="blue", value=7, action=""),
    Card(color="yellow", value=7, action=""),
    Card(color="green", value=7, action=""),
    Card(color="red", value=8, action=""),
    Card(color="blue", value=8, action=""),
    Card(color="yellow", value=8, action=""),
    Card(color="green", value=8, action=""),
    Card(color="red", value=9, action=""),
    Card(color="blue", value=9, action=""),
    Card(color="yellow", value=9, action=""),
    Card(color="green", value=9, action=""),
    Card(color="red", value=None, action="skip"),
    Card(color="blue", value=None, action="skip"),
    Card(color="yellow", value=None, action="skip"),
    Card(color="green", value=None, action="skip"),
    Card(color="red", value=None, action="draw_two"),
    Card(color="blue", value=None, action="draw_two"),
    Card(color="yellow", value=None, action="draw_two"),
    Card(color="green", value=None, action="draw_two"),
    Card(color="red", value=None, action="reverse"),
    Card(color="blue", value=None, action="reverse"),
    Card(color="yellow", value=None, action="reverse"),
    Card(color="green", value=None, action="reverse"),
    Card(color="red", value=None, action="skip"),
    Card(color="blue", value=None, action="skip"),
    Card(color="yellow", value=None, action="skip"),
    Card(color="green", value=None, action="skip"),
    Card(color="red", value=None, action="draw_two"),
    Card(color="blue", value=None, action="draw_two"),
    Card(color="yellow", value=None, action="draw_two"),
    Card(color="green", value=None, action="draw_two"),
    Card(color="red", value=None, action="reverse"),
    Card(color="blue", value=None, action="reverse"),
    Card(color="yellow", value=None, action="reverse"),
    Card(color="green", value=None, action="reverse"),
    Card(color="black", value=None, action="wild", is_active=False),
    Card(color="black", value=None, action="wild_draw_four"),
    Card(color="black", value=None, action="wild", is_active=False),
    Card(color="black", value=None, action="wild_draw_four"),
    Card(color="black", value=None, action="wild", is_active=False),
    Card(color="black", value=None, action="wild_draw_four"),
    Card(color="black", value=None, action="wild", is_active=False),
    Card(color="black", value=None, action="wild_draw_four"),
)
