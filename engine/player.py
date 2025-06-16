from dataclasses import dataclass, field
from typing import List, Set
from .components import Ingredient, PizzaCard

# =====================
#  Player State
# =====================

@dataclass
class PlayerState:
    id: int
    recipes: List[PizzaCard]
    ingredients: Set[Ingredient] = field(default_factory=set)

    # === Methods ===

    def has_completed_all_recipes(self) -> bool:
        """
        Checks to see if the win condition 'Has completed all recipes' has been reached or not.
        """

        for recipe in self.recipes:
            if not all(ingredient in self.ingredients for ingredient in recipe.ingredients):
                return False
        return True