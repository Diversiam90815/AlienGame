# Space War Game

Space War is an engaging 2D arcade-style game inspired by classic space shooter games. Built using Python and Pygame, this project offers an interactive gameplay experience where players defend their spaceship against waves of alien invaders.



## Features

- **Dynamic Gameplay**: Survive against increasingly challenging waves of alien ships.
- **Player Controls**: Move the spaceship and shoot lasers to eliminate enemies.
- **Enemy Attacks**: Aliens shoot lasers to retaliate.
- **Explosions**: Realistic animations for destroyed enemies.
- **High Score Tracking**: Keep track of your best scores across sessions.
- **Audio Effects**: Immersive sound effects for shooting, explosions, and button clicks.
- **Main Menu and Options**: Intuitive UI for starting the game and customizing settings.



## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/space-war.git
   cd space-war
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed and install Pygame:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   ```bash
   python space_war.py
   ```



## Controls

- **Arrow Keys**: Move the spaceship left or right.
- **Space Bar**: Shoot lasers.
- **Escape**: Pause the game and return to the main menu.



## Project Structure

- `space_war.py`: Main game file handling core logic.
- `AssetManager.py`: Manages all game assets (images, sounds, etc.).
- `audio.py`: Handles sound effects.
- `button.py`: Creates and manages UI buttons.
- `alien.py`: Defines alien behavior.
- `alien_laser.py`: Controls the alien laser projectiles.
- `bullet.py`: Manages player projectiles.
- `explosion.py`: Handles explosion animations.
- `game_stats.py`: Tracks game statistics and high scores.
- `scoreboard.py`: Displays player score, level, and remaining lives.
- `ship.py`: Manages the player spaceship.



## Assets

Assets are located in the `Assets` folder and include:
- **Images**: Spaceships, lasers, background, explosions.
- **Audio**: Sound effects for shooting, explosions, and button clicks.



## Planned Features

- **Expanded Fleet**: Add different types of alien ships with unique behaviors.
- **Customizable Settings**: Enable players to adjust game difficulty and audio levels.
- **Adaptive Music**: Dynamic background music that changes based on gameplay intensity.



## Acknowledgments

This project was developed as a fun, educational exercise to explore Pygame and Python game development. Feedback and suggestions are always appreciated!

