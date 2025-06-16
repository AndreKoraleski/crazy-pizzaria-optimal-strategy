import pytest
from typing import List
from engine.game import GameState
from engine.policy import PlayerController
from engine.components import ALL_PIZZAS

class MockPolicy(PlayerController):
    """A simple mock policy for predictable test behavior."""
    def choose_ingredient(self, needed, player):
        return list(needed)[0] if needed else None

    def choose_opponent(self, player, opponents):
        return opponents[0] if opponents else None

    def choose_ingredients_to_lose(self, player, amount):
        return list(player.ingredients)[:amount]

@pytest.fixture(params=[2, 3, 6])
def game_state(request) -> GameState:
    """Fixture to create a GameState, parameterized by the number of players."""
    num_players = request.param
    
    recipes_per_player = {2: 3, 3: 2, 6: 1}[num_players]
    
    all_recipes = [
        [ALL_PIZZAS[j % len(ALL_PIZZAS)] for j in range(recipes_per_player)]
        for i in range(num_players)
    ]
    controllers: List[PlayerController] = [MockPolicy() for _ in range(num_players)]
    
    return GameState(
        num_players=num_players, 
        player_recipes=all_recipes, 
        controllers=controllers, 
        starting_pos=1
    )