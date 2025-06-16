from typing import List, Set

from .components import (
    Ingredient, PizzaCard,
    LuckCard, LuckCardType, LUCK_DECK_COMPOSITION,
    BoardSpace, BoardSpaceType, BOARD_LAYOUT
) 

from .policy import PlayerController
from .player import PlayerState

import random
    
# =====================
#  Game State
# =====================

class GameState:
    def __init__(self, num_players: int, player_recipes: List[List[PizzaCard]], 
                controllers: List[PlayerController],
                starting_pos: int = 0) -> None:
        
        assert num_players in {2, 3, 6}
        assert len(player_recipes) == num_players
        assert len(controllers) == num_players

        expected_pizzas = {2: 3, 3: 2, 6: 1}[num_players]
        for recipes in player_recipes:
            assert len(recipes) == expected_pizzas

        self.players = [
            PlayerState(id=i, recipes=player_recipes[i]) for i in range(num_players)
        ]

        self.controllers = controllers

        # --- Game Variables ---

        self.current_player_index = 0                                                   
        self.pawn_position = starting_pos if starting_pos else random.randint(1, 35) 
        
        self.luck_deck = self._build_luck_deck()
        random.shuffle(self.luck_deck)  

        self.board = BOARD_LAYOUT
        self.game_over = False
        self.winner_id = -1

    # === Space Methods ===
    
    def step(self) -> None:
        """
        Simulates a step on the board using a '6-sided dice'.
        """

        if self.game_over:
            return
        
        player = self.players[self.current_player_index]
        roll = random.randint(1, 6)
        self.pawn_position = (self.pawn_position + roll - 1) % 35 + 1

        space = self.board[self.pawn_position - 1]
        self._resolve_space(space, player)

        self._advance_turn()

    def _resolve_space(self, space: BoardSpace, player: PlayerState):
        """
        Resolves the effect of the space it landed on.
        """

        controller = self.controllers[player.id]

        if space.space_type == BoardSpaceType.INGREDIENT:
            if space.ingredient in self._needed_ingredients(player):
                player.ingredients.add(space.ingredient)

        elif space.space_type == BoardSpaceType.CHEF:
            needed = self._needed_ingredients(player)
            if needed:
                chosen = controller.choose_ingredient(needed, player)
                if chosen:
                    player.ingredients.add(chosen)

        elif space.space_type == BoardSpaceType.GOOD_OR_BAD_LUCK:
            if not self.luck_deck:
                self.luck_deck = self._build_luck_deck()
                random.shuffle(self.luck_deck)
            card = self.luck_deck.pop()
            self._resolve_luck_card(card, player)

        elif space.space_type == BoardSpaceType.LOSE_EVERYTHING:
            player.ingredients.clear()

    def _advance_turn(self):
        """
        Advances the turn by changing which player goes now.
        """

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    # === Luck Deck Methods ===
    
    def _build_luck_deck(self) -> List[LuckCard]:
        """
        Create and returns the deck list built based on the definitons in 'engine/components.py'.
        """

        deck = []
        for card in LUCK_DECK_COMPOSITION:
            deck.extend([card] * card.count)
        return deck
    
    def _resolve_luck_card(self, card: LuckCard, player: PlayerState):
        """
        Resolves the effect of a Good or Bad Luck Card.
        """

        if card.card_type == LuckCardType.GAIN_1:
            self._gain_ingredients(player, 1)
        elif card.card_type == LuckCardType.GAIN_2:
            self._gain_ingredients(player, 2)
        elif card.card_type == LuckCardType.STEAL_1:
            self._steal_ingredients(player, 1)
        elif card.card_type == LuckCardType.STEAL_2:
            self._steal_ingredients(player, 2)
        elif card.card_type == LuckCardType.LOSE_1:
            self._lose_ingredients(player, 1)
        elif card.card_type == LuckCardType.LOSE_2:
            self._lose_ingredients(player, 2)
        elif card.card_type == LuckCardType.LOSE_ALL:
            player.ingredients.clear()

    # === Ingredient Helpers ===

    def _needed_ingredients(self, player: PlayerState) -> Set[Ingredient]:
        """
        Gets the Ingredients the player currently needs to win.
        """

        needed = set()
        for recipe in player.recipes:
            needed.update(recipe.ingredients)
        return needed
    
    def _gain_ingredients(self, player: PlayerState, amount: int):
        """
        Adds Ingredients to the player's Inventory.
        """

        needed = self._needed_ingredients(player)
        controller = self.controllers[player.id]

        for _ in range(amount):
            if not needed:
                break
            chosen = controller.choose_ingredient(needed, player)
            if chosen:
                player.ingredients.add(chosen)
                needed.discard(chosen)

    def _steal_ingredients(self, thief: PlayerState, amount: int):
        """
        Steal Ingredients from one or more players and gives them to the thief.
        """

        controller = self.controllers[thief.id]
        opponents = [p for p in self.players if p != thief and p.ingredients]

        for _ in range(amount):
            if not opponents:
                break
            victim = controller.choose_opponent(thief, opponents)
            if not victim or not victim.ingredients:
                continue
            stolen = controller.choose_ingredient(victim.ingredients, thief)
            if stolen in victim.ingredients:
                victim.ingredients.remove(stolen)
                thief.ingredients.add(stolen)

    def _lose_ingredients(self, player: PlayerState, amount: int):
        """
        Removes Ingredients from the player's Inventory.
        """
        
        controller = self.controllers[player.id]
        to_remove = controller.choose_ingredients_to_lose(player, amount)
        for ing in to_remove:
            if ing in player.ingredients:
                player.ingredients.remove(ing)
