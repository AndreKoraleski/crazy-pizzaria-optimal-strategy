from engine.game import GameState

def test_game_state_initialization(game_state: GameState):
    """Tests that the game state is initialized correctly for all player counts."""
    num_players = len(game_state.players)
    expected_pizzas = {2: 3, 3: 2, 6: 1}[num_players]

    assert len(game_state.players) == num_players
    assert len(game_state.controllers) == num_players
    assert len(game_state.players[0].recipes) == expected_pizzas
    assert game_state.pawn_position == 1
    assert len(game_state.luck_deck) == 24
    assert not game_state.game_over