from typing import List, Set
from .components import Ingredient
from .player import PlayerState

class PlayerController:
    def choose_ingredient(self, needed: Set[Ingredient], player: PlayerState) -> Ingredient:
        raise NotImplementedError

    def choose_opponent(self, player: PlayerState, opponents: List[PlayerState]) -> PlayerState:
        raise NotImplementedError

    def choose_ingredients_to_lose(self, player: PlayerState, amount: int) -> List[Ingredient]:
        raise NotImplementedError
