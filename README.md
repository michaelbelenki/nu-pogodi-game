# Nu Pogodi Game (Ну, погоди!)

A remake of the classic Soviet electronic handheld game "Nu Pogodi" (Well, Just You Wait!) available in both Python and JavaScript versions.

## Description

This is a recreation of the iconic 1980s Soviet electronic game where you control the Wolf character catching eggs falling from four different chutes. The game is based on the popular Soviet cartoon series of the same name.

## 🎮 Two Versions Available

### Python Version (Desktop)
A desktop application built with Pygame for a native gaming experience.

### Web Version (Browser)
A browser-based version using HTML5 Canvas - no installation required!

## Features

- Classic 4-position gameplay (top-left, bottom-left, top-right, bottom-right)
- Progressive difficulty - game speeds up as you catch more eggs
- Score tracking
- 3 lives system
- Simple, nostalgic graphics

---

## 🐍 Python Version

### Requirements
- Python 3.7 or higher
- Pygame library

### Installation

1. Make sure you have Python installed on your system
2. Install the required dependency:

```bash
pip install pygame
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

### How to Run

Navigate to the game directory and run:

```bash
python nu_pogodi.py
```

Or open the project in Visual Studio Code and run the `nu_pogodi.py` file, or press **F5** to debug.

---

## 🌐 Web Version

### How to Run

**Option 1: Quick Start**
- Navigate to the `web_version` folder
- Double-click `index.html` to open in your browser

**Option 2: Local Server (Recommended)**

Using Python:
```bash
cd web_version
python -m http.server 8000
```
Then open: http://localhost:8000

Using Node.js:
```bash
cd web_version
npx http-server
```

**Option 3: VS Code Live Server**
- Install "Live Server" extension in VS Code
- Right-click on `index.html`
- Select "Open with Live Server"

---

## 🎯 Controls

| Key | Action |
|-----|--------|
| Q or 1 | Move to top left position |
| A or 2 | Move to bottom left position |
| P or 9 | Move to top right position |
| L or 0 | Move to bottom right position |
| SPACE | Restart game (after game over) |

## How to Play

1. Eggs fall from four different chutes at the top of the screen
2. Move the Wolf to the correct position to catch the eggs
3. Each caught egg adds 1 point to your score
4. Missing an egg costs you one life (you have 3 lives total)
5. The game speeds up every 10 eggs you catch
6. Try to achieve the highest score possible!

## Game Mechanics

- **Starting Speed**: Eggs fall at a moderate pace
- **Speed Increase**: Every 10 eggs caught, the speed increases
- **Spawn Rate**: Eggs spawn more frequently as your score increases
- **Lives**: You can miss up to 3 eggs before game over

## 📁 Project Structure

```
nu_pogodi_game/
│
├── .vscode/              # VS Code configuration
│   ├── launch.json       # Debug settings
│   └── settings.json     # Editor settings
│
├── web_version/          # Browser version
│   ├── index.html        # Main HTML file
│   ├── style.css         # Styling
│   ├── game.js           # Game logic
│   └── README.md         # Web version docs
│
├── .gitignore            # Git ignore file
├── nu_pogodi.py          # Python game file
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## 🛠️ Development

This project was created as a nostalgic tribute to the classic Soviet handheld game. Feel free to modify and enhance it!

### Potential Improvements

- [ ] Add sound effects
- [ ] Create sprite graphics for Wolf and eggs
- [ ] Add difficulty levels
- [ ] Implement high score saving (localStorage for web, file for Python)
- [ ] Add animations
- [ ] Create a menu system
- [ ] Touch controls for mobile (web version)
- [ ] Leaderboard system

## 🌟 Which Version Should I Use?

**Choose Python Version if:**
- You want a native desktop application
- You're learning Python/Pygame
- You prefer better performance
- You want to package it as a standalone executable

**Choose Web Version if:**
- You want instant play without installation
- You want to share the game easily (just send the folder)
- You want to host it online
- You're learning web development
- You want mobile compatibility (with touch controls)

## 📝 Credits

Based on the original "Nu Pogodi" electronic game by Elektronika (USSR, 1980s)

Inspired by the Soviet cartoon series "Ну, погоди!" (Well, Just You Wait!)

## 📄 License

This is a fan project created for educational and nostalgic purposes.

---

Enjoy the game! Ну, погоди! 🐺🥚
