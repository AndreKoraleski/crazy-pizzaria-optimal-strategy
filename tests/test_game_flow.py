from unittest.mock import patch
from engine.game import GameState

def test_advance_turn(game_state: GameState):
    """Tests that the turn advances correctly for any number of players."""
    num_players = len(game_state.players)
    initial_player_index = game_state.current_player_index

    game_state._advance_turn()
    assert game_state.current_player_index == (initial_player_index + 1) % num_players

@patch('random.randint', return_value=4)
def test_step_advances_turn_and_position(mock_randint, game_state: GameState):
    """Tests that a step moves the pawn and advances the turn."""
    initial_player = game_state.current_player_index
    game_state.step()
    assert game_state.pawn_position == 5
    assert game_state.current_player_index != initial_player

def test_win_condition(game_state: GameState):
    """Tests that the game correctly identifies a winner."""
    player = game_state.players[0]
    for recipe in player.recipes:
        for ingredient in recipe.ingredients:
            player.ingredients.add(ingredient)
    
    game_state._check_for_winner()
    
    assert game_state.game_over
    assert game_state.winner_id == player.id