from enum import Enum, auto         # To avoid that future changes in values break other systems
from dataclasses import dataclass   # For using Frozen=True so the dataclasses are imutable
from typing import List, Optional   # Just for type checking

# =====================
#  Ingredient
# =====================

class Ingredient(Enum):
    SALAMI = auto()
    BROCCOLI = auto()
    EGGS = auto()
    OLIVES = auto()
    PEAS = auto()
    CORN = auto()
    HAM = auto()
    CHEESE = auto()
    TOMATO = auto()
    ONION = auto()

# =====================
#  Pizza Card
# =====================

# --- Class ---

@dataclass(frozen=True)
class PizzaCard:
    name: str
    ingredients: List[Ingredient]

# --- Pizza Card Definitions ---

CALABRESA = PizzaCard(
    "Calabresa",
    [Ingredient.SALAMI, Ingredient.BROCCOLI, Ingredient.EGGS, Ingredient.OLIVES, Ingredient.PEAS]
)

PORTUGUESE = PizzaCard(
    "Portuguese",
    [Ingredient.CORN, Ingredient.HAM, Ingredient.CHEESE, Ingredient.OLIVES, Ingredient.EGGS]
)

TOSCANE = PizzaCard(
    "Toscane",
    [Ingredient.SALAMI, Ingredient.HAM, Ingredient.TOMATO, Ingredient.OLIVES, Ingredient.ONION]
)

MARGUERITA = PizzaCard(
    "Marguerita",
    [Ingredient.CHEESE, Ingredient.TOMATO, Ingredient.SALAMI, Ingredient.CORN, Ingredient.BROCCOLI]
)

ROMAN = PizzaCard(
    "Roman",
    [Ingredient.HAM, Ingredient.CHEESE, Ingredient.CORN, Ingredient.PEAS, Ingredient.ONION]
)

VEGETARIAN = PizzaCard(
    "Vegetarian",
    [Ingredient.BROCCOLI, Ingredient.TOMATO, Ingredient.EGGS, Ingredient.ONION, Ingredient.PEAS]
)

# --- List of all Pizza Cards ---

ALL_PIZZAS = [CALABRESA, PORTUGUESE, TOSCANE, MARGUERITA, ROMAN, VEGETARIAN]

# =====================
#  Board Space Types
# =====================

class BoardSpaceType(Enum):
    INGREDIENT = auto()
    GOOD_OR_BAD_LUCK = auto()
    CHEF = auto()
    LOSE_EVERYTHING = auto()

# =====================
#  Board Space
# =====================

# --- Class ---

@dataclass(frozen=True)
class BoardSpace:
    position: int
    space_type: BoardSpaceType
    ingredient: Optional[Ingredient] = None

# --- Board Layout ---

BOARD_LAYOUT = [
    BoardSpace(1, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(2, BoardSpaceType.INGREDIENT, Ingredient.BROCCOLI),
    BoardSpace(3, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(4, BoardSpaceType.CHEF),
    BoardSpace(5, BoardSpaceType.INGREDIENT, Ingredient.CORN),
    BoardSpace(6, BoardSpaceType.INGREDIENT, Ingredient.TOMATO),
    BoardSpace(7, BoardSpaceType.INGREDIENT, Ingredient.HAM),
    BoardSpace(8, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(9, BoardSpaceType.INGREDIENT, Ingredient.PEAS),
    BoardSpace(10, BoardSpaceType.INGREDIENT, Ingredient.CORN),
    BoardSpace(11, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(12, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(13, BoardSpaceType.INGREDIENT, Ingredient.OLIVES),
    BoardSpace(14, BoardSpaceType.INGREDIENT, Ingredient.EGGS),
    BoardSpace(15, BoardSpaceType.INGREDIENT, Ingredient.TOMATO),
    BoardSpace(16, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(17, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(18, BoardSpaceType.INGREDIENT, Ingredient.CHEESE),
    BoardSpace(19, BoardSpaceType.INGREDIENT, Ingredient.SALAMI),
    BoardSpace(20, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(21, BoardSpaceType.INGREDIENT, Ingredient.ONION),
    BoardSpace(22, BoardSpaceType.LOSE_EVERYTHING),
    BoardSpace(23, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(24, BoardSpaceType.INGREDIENT, Ingredient.OLIVES),
    BoardSpace(25, BoardSpaceType.INGREDIENT, Ingredient.BROCCOLI),
    BoardSpace(26, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(27, BoardSpaceType.INGREDIENT, Ingredient.PEAS),
    BoardSpace(28, BoardSpaceType.INGREDIENT, Ingredient.CHEESE),
    BoardSpace(29, BoardSpaceType.CHEF),
    BoardSpace(30, BoardSpaceType.INGREDIENT, Ingredient.HAM),
    BoardSpace(31, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(32, BoardSpaceType.INGREDIENT, Ingredient.SALAMI),
    BoardSpace(33, BoardSpaceType.GOOD_OR_BAD_LUCK),
    BoardSpace(34, BoardSpaceType.INGREDIENT, Ingredient.ONION),
    BoardSpace(35, BoardSpaceType.INGREDIENT, Ingredient.EGGS),
]

# =====================
#  Luck Card Type
# =====================

class LuckCardType(Enum):   # The effects of the cards are almost self-explanatory
    GAIN_1 = auto()
    GAIN_2 = auto()
    STEAL_1 = auto()        
    STEAL_2 = auto()        # You choose either: a) Two players, then steal an Ingredient from each; b) Steal two cards from a player
    LOSE_1 = auto()
    LOSE_2 = auto()
    LOSE_ALL = auto()

# =====================
#  Luck Card
# =====================

# --- Class ---

@dataclass(frozen=True)
class LuckCard:
    card_type: LuckCardType
    count: int

# --- Deck Definition ---

LUCK_DECK_COMPOSITION = [               # Total of 24 cards (13 of Good Luck, 11 of Bad Luck)
    LuckCard(LuckCardType.GAIN_1, 7),   
    LuckCard(LuckCardType.GAIN_2, 2),   
    LuckCard(LuckCardType.STEAL_1, 3),  
    LuckCard(LuckCardType.STEAL_2, 1),  
    LuckCard(LuckCardType.LOSE_1, 8),   
    LuckCard(LuckCardType.LOSE_2, 2),   
    LuckCard(LuckCardType.LOSE_ALL, 1), 
]
