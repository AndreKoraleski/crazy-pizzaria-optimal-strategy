# 🍕 Crazy Pizzaria
**Optimal Strategy & Simulation Suite**

Welcome to **Crazy Pizzaria**, a computational framework for simulating, analyzing, and mastering the chaotic, luck-filled strategy of the tabletop game *Crazy Pizzaria*. Whether you're a data scientist, a game theorist, or just a pizza lover with a competitive streak — this project is for you.

---

## 🎯 Project Goals

- 🧠 Build a faithful and extensible simulation engine
- 🤖 Train intelligent agents using multi-agent reinforcement learning (MARL)
- 📊 Visualize and interpret strategic insights from high-volume simulations
- 📚 Provide both human-readable and machine-usable strategy guides
- 🎮 Support a real-time GUI for interactive game observation

---

## 📁 Project Structure

| Folder        | Description |
|---------------|-------------|
| `engine/`     | Core game logic and simulation framework |
| `env/`        | PettingZoo-compatible MARL environment |
| `agents/`     | Reinforcement learning agents and training scripts |
| `gui/`        | Optional GUI (Pygame or Tkinter) for visualization |
| `scripts/`    | One-off runnable Python scripts for testing, demos, and diagnostics |
| `data/`       | Simulation outputs, logs, and trained models |
| `strategy/`   | Extracted strategic insights (e.g., decision trees, policy files) |
| `notebooks/`  | Jupyter notebooks for analysis and experimentation |
| `tests/`      | Unit and behavior tests for code validation |

---

## 🚀 Getting Started

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/AndreKoraleski/crazy-pizzaria-optimal-strategy.git
    cd crazy-pizzaria-optimal-strategy
    ```

2.  **Set up the environment and install dependencies:**
    This project is configured as an installable Python package. From the root directory, run:
    ```sh
    pip install -e .
    ```
    This command uses the `setup.py` file to install all required dependencies and makes the project's `engine` module correctly importable in your environment. The `-e` flag installs it in "editable" mode, so your code changes take effect immediately.

3.  **Run a test simulation:**
    After installation, you can run a sample game using the convenient command-line script:
    ```sh
    # Run with --n 2, 3 or 6 (default 3) 
    # for different player combinations
    run-random-pizzaria-game
    ```
    Alternatively, you can always execute the script directly:
    ```sh
    python3 scripts/test_random_game.py
    ```

---

## 🧪 Running Tests

This project uses `pytest` to validate the core logic of the simulation engine. Tests cover game initialization, turn flow, space resolution, and luck card effects.

To run the full test suite, execute the following command in the root directory:
```sh
pytest
```
---

## 📜 Game Rules: *Crazy Pizzaria – The Complete Rulebook*

### 1. Objective

Be the first chef to complete all your Pizza Recipe cards by collecting their required ingredients.

### 2. Components

- 1 Game Board (35 spaces)
- 1 Shared Player Pawn (used by all players)
- 1 Six-sided Die
- 6 Pizza Recipe Cards
- Ingredient Tokens (unlimited supply, 10 types)
- 24 Good or Bad Luck Cards

### 3. The Recipes

Each recipe requires 5 specific ingredients:

- **Calabresa**: Salami, Broccoli, Eggs, Olives, Peas
- **Portuguese**: Corn, Ham, Cheese, Olives, Eggs
- **Toscane**: Salami, Ham, Tomato, Olives, Onion
- **Marguerita**: Cheese, Tomato, Salami, Corn, Broccoli
- **Roman**: Ham, Cheese, Corn, Peas, Onion
- **Vegetarian**: Broccoli, Tomato, Eggs, Onion, Peas

_All ingredients appear in exactly 3 recipes — no rare ingredients!_

### 4. Board Layout (Clockwise Order)

1. Good or Bad Luck
2. Broccoli
3. Good or Bad Luck
4. Chef
5. Corn
6. Tomato
7. Ham
8. Good or Bad Luck
9. Peas
10. Corn
11. Good or Bad Luck
12. Good or Bad Luck
13. Olives
14. Eggs
15. Tomato
16. Good or Bad Luck
17. Good or Bad Luck
18. Cheese
19. Salami
20. Good or Bad Luck
21. Onion
22. **LOSE EVERYTHING**
23. Good or Bad Luck
24. Olives
25. Broccoli
26. Good or Bad Luck
27. Peas
28. Cheese
29. Chef
30. Ham
31. Good or Bad Luck
32. Salami
33. Good or Bad Luck
34. Onion
35. Eggs

### 5. Setup

1. Place the board and ingredient tokens.
2. Lay out all 6 Pizza Recipe cards face up.
3. Players draft recipe cards based on player count:
    - **6 players**: 1 card each
    - **3 players**: 2 cards each, snake order (P1, P2, P3, P3, P2, P1)
    - **2 players**: 3 cards each, full snake (P1, P2, P2, P1, P1, P2)
4. Shuffle the Luck Deck and place it face down.
5. Place the Shared Pawn on a random board space.

### 6. Gameplay

On your turn:

1. Roll the die (1–6).
2. Move the Shared Pawn clockwise.
3. Perform the action of the space — applies only to you.
4. Check if you’ve completed all your recipes. If yes, you win!

### 7. Board Space Effects

- **Ingredient Space**: Take that ingredient if you need it.
- **Chef**: Take any one needed ingredient of your choice.
- **Good or Bad Luck**: Draw and resolve a Luck Card.
- **Lose Everything**: Return all collected ingredients to the supply.

### 8. The Luck Deck (24 Cards)

- Gain 1 Ingredient (×7)
- Gain 2 Ingredients (×2)
- Steal 1 Ingredient (×3)
- Steal 2 Ingredients (×1): choose
    - Option A: Steal 2 from one opponent
    - Option B: Steal 1 each from two opponents
- Lose 1 Ingredient (×8)
- Lose 2 Ingredients (×2)
- Lose All Ingredients (×1)

### 9. Winning the Game

First player to complete all their Pizza Recipe cards wins immediately.

---