from engine.components import PizzaCard, ALL_PIZZAS
from engine.game import GameState
from engine.policies.random_policy import RandomPolicy
from engine.policy import PlayerController


def get_default_recipe_draft(num_players: int) -> list[list[PizzaCard]]:
    """
    Returns hardcoded balanced recipe drafts for 2, 3, or 6 players.
    """

    all_pizzas = ALL_PIZZAS
    if num_players == 2:
        return [all_pizzas[:3], all_pizzas[3:]]
    elif num_players == 3:
        return [[all_pizzas[0], all_pizzas[1]],
                [all_pizzas[2], all_pizzas[3]],
                [all_pizzas[4], all_pizzas[5]]]
    elif num_players == 6:
        return [[p] for p in all_pizzas]
    else:
        raise ValueError("Only 2, 3, or 6 players are supported.")

def main():
    num_players = 3
    recipe_draft = get_default_recipe_draft(num_players)
    controllers: list[PlayerController] = [RandomPolicy() for _ in range(num_players)]

    game = GameState(num_players=num_players, player_recipes=recipe_draft, controllers=controllers)

    turn = 1
    while not game.game_over and game.winner_id == -1:
        print(f"\n=== TURN {turn} ===")
        print(f"Pawn is on space {game.pawn_position}")
        game.step()

        for player in game.players:
            if player.has_completed_all_recipes():
                game.game_over = True
                game.winner_id = player.id
                break 

        for player in game.players:
            ing = ', '.join(i.name for i in sorted(player.ingredients, key=lambda x: x.name))
            print(f"Player {player.id}: {ing}")

        turn += 1

    print(f"\nGame Over! Winner: Player {game.winner_id}")

if __name__ == "__main__":
    main()