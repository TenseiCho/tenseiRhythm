# TenseiRhythm

This project is a rhythm game inspired by the Japanese arcade game WACCA, implemented using Python and Pygame.

## Features

- Circular gameplay area with keys arranged around the perimeter
- Main menu with options to play, adjust settings, and exit
- Beatmap system for timing key presses to music
- Background music and sound effects

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install Pygame:
   ```
   pip install pygame
   ```
3. Clone this repository or download the source code.

## Game Controls

- Use the mouse to navigate the main menu
- In the game, press the keys (W, Q, P, O, I, U, R, E) as they appear on the circular interface
- Press ESC to exit the game

## Project Structure

- `menu.py`: Implements the main menu and game flow
- `game.py`: Contains the core game logic and rendering
- `options.py`: Handles game options (not included in the provided code snippets)
- `beatmaps/`: Directory containing JSON files with beatmap data for songs
- `music/`: Directory for storing music files (WAV format)
- `images/`: Directory for storing image files (e.g., menu background)
- `sounds/`: Directory for storing sound effect files

## Adding New Songs

To add a new song:
1. Create a WAV file in the `music/` directory
2. Create a corresponding JSON beatmap file in the `beatmaps/` directory
3. Update the game code to include the new song in the song selection logic

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.