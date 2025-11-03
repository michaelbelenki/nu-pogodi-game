# Nu Pogodi - Web Version

A browser-based JavaScript remake of the classic Soviet electronic handheld game "Nu Pogodi" (Well, Just You Wait!).

## Overview

This is a web version that runs directly in your browser without any installation. Play the nostalgic egg-catching game right from your web browser!

## Features

- **No Installation Required**: Just open `index.html` in your browser
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Beautiful, clean interface with smooth animations
- **Classic Gameplay**: Authentic Nu Pogodi experience
- **Progressive Difficulty**: Game speeds up as you catch more eggs
- **Keyboard Controls**: Simple and intuitive controls

## How to Run

### Option 1: Local File
1. Navigate to the `web_version` folder
2. Double-click `index.html` to open it in your default browser
3. Start playing!

### Option 2: Local Server (Recommended)
For the best experience, run a local web server:

**Using Python:**
```bash
cd web_version
python -m http.server 8000
```
Then open: http://localhost:8000

**Using Node.js (with npx):**
```bash
cd web_version
npx http-server
```

**Using VS Code:**
- Install the "Live Server" extension
- Right-click on `index.html`
- Select "Open with Live Server"

## Controls

| Key | Action |
|-----|--------|
| Q or 1 | Move to top left position |
| A or 2 | Move to bottom left position |
| P or 9 | Move to top right position |
| L or 0 | Move to bottom right position |
| SPACE | Restart game (after game over) |

## How to Play

1. Open the game in your browser
2. Eggs fall from four different chutes at the top
3. Use the keyboard controls to move the Wolf to catch the eggs
4. Each caught egg adds 1 point to your score
5. Missing an egg costs you one life (you have 3 lives)
6. The game speeds up every 10 eggs you catch
7. Try to achieve the highest score!

## Game Mechanics

- **Starting Speed**: Moderate pace for beginners
- **Speed Increase**: Every 10 eggs caught
- **Spawn Rate**: Eggs appear more frequently as score increases
- **Lives**: 3 lives total (shown at the top)

## Files Structure

```
web_version/
│
├── index.html       # Main HTML file
├── style.css        # Styling and layout
├── game.js          # Game logic and mechanics
└── README.md        # This file
```

## Browser Compatibility

This game works in all modern browsers:
- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

## Customization

You can easily customize the game by editing:

- **Colors**: Modify the `COLORS` object in `game.js`
- **Speed**: Adjust `GAME_SETTINGS` in `game.js`
- **Styling**: Edit `style.css` for visual changes
- **Layout**: Modify `index.html` for structure changes

## Technical Details

- **Canvas API**: Used for game rendering
- **Pure JavaScript**: No frameworks or libraries required
- **CSS3**: Modern styling with animations
- **Responsive**: Adapts to different screen sizes

## Future Enhancements

Ideas for improvement:
- [ ] Touch controls for mobile devices
- [ ] Sound effects
- [ ] High score leaderboard (localStorage)
- [ ] Multiple difficulty levels
- [ ] Sprite graphics
- [ ] Animation effects for caught/missed eggs
- [ ] Pause functionality

## Credits

Based on the original "Nu Pogodi" electronic game by Elektronika (USSR, 1980s)

Inspired by the Soviet cartoon series "Ну, погоди!" (Well, Just You Wait!)

---

Enjoy the game in your browser! Ну, погоди! 🐺🥚
