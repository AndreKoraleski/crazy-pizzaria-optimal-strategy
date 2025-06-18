import pytest
from engine.components import LuckCard, LuckCardType, Ingredient
from engine.game import GameState

def test_resolve_luck_card_gain_1(game_state: GameState):
    """Tests the GAIN_1 luck card."""
    player = game_state.players[0]
    needed_ingredient = list(game_state._needed_ingredients(player))[0]
    
    card = LuckCard(LuckCardType.GAIN_1, 1)
    game_state._resolve_luck_card(card, player)

    assert needed_ingredient in player.ingredients

def test_resolve_luck_card_steal_1(game_state: GameState):
    """Tests the STEAL_1 luck card."""
    if len(game_state.players) < 2:
        pytest.skip("Stealing requires at least 2 players.")

    thief = game_state.players[0]
    victim = game_state.players[1]

    needed_ingredients = game_state._needed_ingredients(thief)
    if not needed_ingredients:
        pytest.skip("Thief needs no ingredients to steal.")
    
    ingredient_to_steal = list(needed_ingredients)[0]
    victim.ingredients.add(ingredient_to_steal)

    card = LuckCard(LuckCardType.STEAL_1, 1)
    game_state._resolve_luck_card(card, thief)

    assert ingredient_to_steal in thief.ingredients
    assert ingredient_to_steal not in victim.ingredients

def test_resolve_luck_card_lose_1(game_state: GameState):
    """Tests the LOSE_1 luck card."""
    player = game_state.players[0]
    player.ingredients.add(Ingredient.EGGS)
    
    card = LuckCard(LuckCardType.LOSE_1, 1)
    game_state._resolve_luck_card(card, player)
    
    assert not player.ingredients

def test_resolve_luck_card_lose_all(game_state: GameState):
    """Tests the LOSE_ALL luck card."""
    player = game_state.players[0]
    player.ingredients.add(Ingredient.HAM)
    player.ingredients.add(Ingredient.PEAS)

    card = LuckCard(LuckCardType.LOSE_ALL, 1)
    game_state._resolve_luck_card(card, player)

    assert not player.ingredients