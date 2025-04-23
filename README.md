# Spaceship World - Pygame

A 2D arcade-style game where you pilot an airplane through a sky filled with clouds and falling obstacles. The game is built using Python's **Pygame** library and demonstrates basic game development concepts like sprite handling, collision detection, and dynamic difficulty.

---

## 🎮 Gameplay Features

- Player Control – Use **arrow keys** to fly the airplane through obstacles  
- Dynamic Obstacles – Avoid randomly generated falling objects that increase in speed over time  
- Cloud Environment – Adds visual depth and motion to the sky  
- Score System – Points increase as you dodge obstacles  
- Game Over Screen – Final score displayed after collision  
- User Interface – Score display and instructional messages on screen  
- *(Sound system placeholder for future updates)*

---

## 🛠️ Setup & How to Play

### 🔧 Prerequisites

Make sure Python 3.x and Pygame are installed. To install Pygame:

```bash
pip install pygame
Keep all files in the same folder as game.by.alishba.py:

game.by.alishba.py – main game script

airplane.png – player sprite

obstacle.png – falling object

cloud.png – background cloud visuals

spaceship.png – game window icon

gameover.jpg – image shown after a collision

▶️ Running the Game
In the terminal or command prompt, navigate to the project directory and run:

python game.by.alishba.py
🎮 Controls
← Left Arrow – Move left

→ Right Arrow – Move right

↑ Up Arrow – Move up & speed up obstacles

🧠 How It Works
Game Initialization – Loads Pygame modules, display window, and assets

Sprite Management – Airplane, obstacles, and clouds are updated every frame

Movement & Collision – Real-time updates and collision detection using distance checks

Score Tracking – Score increments as obstacles pass

Game Loop – Runs frame-by-frame updates, rendering, input handling, and logic

Game Over – Triggered upon collision and displays final score

🚀 Future Improvements
Sound effects and background music

Power-ups (shield, score boost, etc.)

Difficulty levels (easy, medium, hard)

High score saving system

Menu UI for game start and settings

More visual polish and obstacle types

👩‍💻 Author
Developed with 💻 by Alishba.

📄 License
This project is open-source and free to use for educational or personal purposes.