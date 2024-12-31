<img width="1440" alt="Screenshot 2024-12-31 at 7 03 46 PM" src="https://github.com/user-attachments/assets/939073cd-e164-450b-86fa-888db8457711" />
# Snake Game

## Description
This is a simple implementation of the classic Snake Game using Python's `turtle` module. The game involves controlling a snake to collect food and grow longer while avoiding collisions with the edges of the screen or itself. The player's score increases with each piece of food collected, and the game keeps track of the highest score achieved during the session.

## Features
- Control the snake using arrow keys.
- Food appears at random locations on the screen.
- The snake grows longer with each piece of food collected.
- Keeps track of the current score and the high score.
- Game restarts if the snake collides with the screen edges or itself.

## Requirements
- Python 3.x
- `turtle` module (pre-installed with Python)

## How to Run
1. Ensure you have Python installed on your system.
2. Copy the script into a Python file, e.g., `snake_game.py`.
3. Run the script using the command:
   ```
   python snake_game.py
   ```
4. Use the arrow keys to control the snake's movement.

## Controls
- **Arrow Up (↑):** Move the snake up
- **Arrow Down (↓):** Move the snake down
- **Arrow Left (←):** Move the snake left
- **Arrow Right (→):** Move the snake right

## Rules
1. The game starts with the snake at the center of the screen, moving to the right.
2. Collect food (red circles) to increase your score and the length of the snake.
3. Avoid colliding with the edges of the screen or the snake's own body.
4. If a collision occurs, the game resets:
   - The snake is repositioned to the center.
   - The score is reset to zero (but the high score remains).
   - All snake segments are cleared.

## Scoring
- Each piece of food collected increases the score by **10 points**.
- The high score updates if the current score exceeds the previous high score.

## Code Highlights
1. **Snake Movement:** The snake's direction is controlled using the `turtle` module's `onkeypress` functionality.
2. **Food Positioning:** Food appears at random positions within the screen boundaries using the `random.randint` function.
3. **Collision Detection:**
   - Collision with the screen edges.
   - Collision with the snake's own body.
4. **Dynamic Snake Growth:** New segments are added to the snake whenever food is collected.
5. **Game Speed:** The delay decreases slightly with each piece of food collected, making the game progressively faster and more challenging.



Enjoy playing the Snake Game!


