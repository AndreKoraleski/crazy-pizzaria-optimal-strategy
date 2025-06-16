import random
from typing import Set, List, Optional

from ..policy import PlayerController
from ..components import Ingredient
from ..player import PlayerState

"""
This policy will override Player Controller and just make random choices.
"""

class RandomPolicy(PlayerController):
    def choose_ingredient(self, needed: Set[Ingredient], player: PlayerState) -> Optional[Ingredient]:
        return random.choice(list(needed)) if needed else None

    def choose_opponent(self, player: PlayerState, opponents: List[PlayerState]) -> Optional[PlayerState]:
        return random.choice(opponents) if opponents else None

    def choose_ingredients_to_lose(self, player: PlayerState, amount: int) -> List[Ingredient]:
        return random.sample(list(player.ingredients), min(amount, len(player.ingredients)))
