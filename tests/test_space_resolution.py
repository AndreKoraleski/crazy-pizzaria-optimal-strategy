from engine.components import Ingredient, BoardSpaceType, ALL_PIZZAS
from engine.game import GameState, BOARD_LAYOUT

def test_resolve_ingredient_space(game_state: GameState):
    """Tests landing on an INGREDIENT space."""
    player = game_state.players[0]
    space = BOARD_LAYOUT[1] 
    
    player.recipes = [next(p for p in ALL_PIZZAS if Ingredient.BROCCOLI in p.ingredients)]
    player.ingredients.clear()

    game_state._resolve_space(space, player)
    assert Ingredient.BROCCOLI in player.ingredients

def test_resolve_chef_space(game_state: GameState):
    """Tests landing on a CHEF space."""
    player = game_state.players[0]
    needed_ingredient = list(game_state._needed_ingredients(player))[0]

    space = next(s for s in BOARD_LAYOUT if s.space_type == BoardSpaceType.CHEF)
    game_state._resolve_space(space, player)
    
    assert needed_ingredient in player.ingredients

def test_resolve_lose_everything_space(game_state: GameState):
    """Tests landing on a LOSE_EVERYTHING space."""
    player = game_state.players[0]
    player.ingredients.add(Ingredient.CHEESE)
    
    space = next(s for s in BOARD_LAYOUT if s.space_type == BoardSpaceType.LOSE_EVERYTHING)
    game_state._resolve_space(space, player)

    assert not player.ingredients