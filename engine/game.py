from dataclasses import dataclass, field
from typing import List, Set

from .components import (
    Ingredient, PizzaCard,
    LuckCard, LuckCardType, LUCK_DECK_COMPOSITION,
    BoardSpace, BoardSpaceType, BOARD_LAYOUT
) 

import random

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
    
# =====================
#  Game State
# =====================

class GameState:
    def __init__(self, num_players: int, player_recipes: List[List[PizzaCard]], starting_pos: int = 0) -> None:
        # Guarantee we are trying to start a game with a valid number of players
        assert num_players in {2, 3, 6}, "Only 2, 3 or 6 players are supported."

        # Checking if the distribution of cards is correct
        expected_pizza_cards = {2: 3, 3: 2, 6: 1}[num_players]
        for recipes in player_recipes:
            assert len(recipes) == expected_pizza_cards, f"Each player must have {expected_pizza_cards} pizza cards."
        assert len(player_recipes) == num_players

        self.players = [
            PlayerState(id=i, recipes=player_recipes[i]) for i in range(num_players)
        ]

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

        space = self.board[self.pawn_position]
        
    def _resolve_space(self, space: BoardSpace, player: PlayerState):
        """
        Resolves the effect of the space it landed on.
        """

        # --- Ingredient Spaces ---

        if space.space_type == BoardSpaceType.INGREDIENT:
            if space.ingredient in self._needed_ingredients(player):
                player.ingredients.add(space.ingredient)

        # --- Chef Spaces ---

        elif space.space_type == BoardSpaceType.CHEF:
            needed = self._needed_ingredients(player)
            if needed:
                chosen = random.choice(list(needed))
                player.ingredients.add(chosen)

        # --- Good or Bad Luck Spaces ---

        elif space.space_type == BoardSpaceType.GOOD_OR_BAD_LUCK:
            if not self.luck_deck:
                self.luck_deck = self._build_luck_deck()
                random.shuffle(self.luck_deck)
            card = self.luck_deck.pop()
            self._resolve_luck_card(card, player)

        # --- Lose Everything ---
        
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

    # === ingredient Helpers ===

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

        needed = list(self._needed_ingredients(player))
        random.shuffle(needed)
        for i in range(min(amount, len(needed))):
            player.ingredients.add(needed[i])

    def _steal_ingredients(self, thief: PlayerState, amount: int):
        """
        Steal Ingredients from one or more players and gives them to the thief.
        """

        opponents = [p for p in self.players if p != thief and p.ingredients]
        if not opponents:
            return
        for _ in range(amount):
            if not opponents:
                break
            victim = random.choice(opponents)
            if victim.ingredients:
                stolen = random.choice(list(victim.ingredients))
                victim.ingredients.remove(stolen)
                thief.ingredients.add(stolen)
                if not victim.ingredients:
                    opponents.remove(victim)

    def _lose_ingredients(self, player: PlayerState, amount: int):
        """
        Removes Ingredients from the player's Inventory.
        """
        
        for _ in range(min(amount, len(player.ingredients))):
            to_remove = random.choice(list(player.ingredients))
            player.ingredients.remove(to_remove)