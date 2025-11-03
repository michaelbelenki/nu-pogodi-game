// Game constants
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const WIDTH = 800;
const HEIGHT = 600;
const FPS = 60;

// Colors
const COLORS = {
    white: '#FFFFFF',
    black: '#000000',
    gray: '#C8C8C8',
    red: '#FF4444',
    yellow: '#FFD700',
    brown: '#8B4513'
};

// Game settings
const GAME_SETTINGS = {
    eggSpeedStart: 2,
    speedIncrement: 0.1,
    speedIncreaseInterval: 10,
    initialSpawnInterval: 120,
    minSpawnInterval: 60
};

// Wolf class
class Wolf {
    constructor() {
        this.positions = {
            'top_left': { x: 150, y: 200 },
            'bottom_left': { x: 150, y: 400 },
            'top_right': { x: 650, y: 200 },
            'bottom_right': { x: 650, y: 400 }
        };
        this.currentPosition = 'bottom_left';
        this.size = 60;
    }

    move(position) {
        if (this.positions[position]) {
            this.currentPosition = position;
        }
    }

    draw() {
        const pos = this.positions[this.currentPosition];
        
        // Draw wolf body
        ctx.fillStyle = COLORS.brown;
        ctx.beginPath();
        ctx.arc(pos.x, pos.y, this.size / 2, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw eyes
        ctx.fillStyle = COLORS.black;
        ctx.beginPath();
        ctx.arc(pos.x - 10, pos.y - 5, 3, 0, Math.PI * 2);
        ctx.arc(pos.x + 10, pos.y - 5, 3, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw basket
        ctx.strokeStyle = COLORS.yellow;
        ctx.lineWidth = 3;
        ctx.strokeRect(pos.x - 40, pos.y + 20, 80, 30);
        ctx.lineWidth = 1;
    }
}

// Egg class
class Egg {
    constructor(lane) {
        this.lane = lane;
        this.lanes = {
            'top_left': { sx: 100, sy: 50, ex: 150, ey: 200 },
            'bottom_left': { sx: 100, sy: 50, ex: 150, ey: 400 },
            'top_right': { sx: 700, sy: 50, ex: 650, ey: 200 },
            'bottom_right': { sx: 700, sy: 50, ex: 650, ey: 400 }
        };
        
        const laneData = this.lanes[lane];
        this.startX = laneData.sx;
        this.startY = laneData.sy;
        this.endX = laneData.ex;
        this.endY = laneData.ey;
        this.x = this.startX;
        this.y = this.startY;
        this.size = 20;
        this.caught = false;
        this.broken = false;
        this.progress = 0;
    }

    update(speed) {
        if (!this.caught && !this.broken) {
            this.progress += speed / 100;
            
            if (this.progress >= 1) {
                this.progress = 1;
                return true; // Reached end
            }
            
            // Interpolate position
            this.x = this.startX + (this.endX - this.startX) * this.progress;
            this.y = this.startY + (this.endY - this.startY) * this.progress;
        }
        return false;
    }

    draw() {
        if (!this.caught && !this.broken) {
            // Draw egg
            ctx.fillStyle = COLORS.white;
            ctx.strokeStyle = COLORS.black;
            ctx.lineWidth = 2;
            
            ctx.beginPath();
            ctx.ellipse(this.x, this.y, this.size / 2, this.size * 0.75, 0, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();
            ctx.lineWidth = 1;
        }
    }
}

// Game class
class Game {
    constructor() {
        this.wolf = new Wolf();
        this.eggs = [];
        this.score = 0;
        this.misses = 0;
        this.maxMisses = 3;
        this.gameOver = false;
        this.eggSpeed = GAME_SETTINGS.eggSpeedStart;
        this.spawnTimer = 0;
        this.spawnInterval = GAME_SETTINGS.initialSpawnInterval;
        this.lanes = ['top_left', 'bottom_left', 'top_right', 'bottom_right'];
        this.lastTime = Date.now();
    }

    spawnEgg() {
        const lane = this.lanes[Math.floor(Math.random() * this.lanes.length)];
        this.eggs.push(new Egg(lane));
    }

    checkCatch(egg) {
        if (egg.lane === this.wolf.currentPosition) {
            egg.caught = true;
            this.score++;
            this.updateScore();
            
            // Increase speed every interval
            if (this.score % GAME_SETTINGS.speedIncreaseInterval === 0) {
                this.eggSpeed += GAME_SETTINGS.speedIncrement;
                this.spawnInterval = Math.max(
                    GAME_SETTINGS.minSpawnInterval,
                    this.spawnInterval - 5
                );
            }
            return true;
        }
        return false;
    }

    update() {
        if (this.gameOver) return;

        // Spawn eggs
        this.spawnTimer++;
        if (this.spawnTimer >= this.spawnInterval) {
            this.spawnEgg();
            this.spawnTimer = 0;
        }

        // Update eggs
        const eggsToRemove = [];
        for (const egg of this.eggs) {
            if (egg.update(this.eggSpeed)) {
                if (!this.checkCatch(egg)) {
                    egg.broken = true;
                    this.misses++;
                    this.updateLives();
                    if (this.misses >= this.maxMisses) {
                        this.endGame();
                    }
                }
                eggsToRemove.push(egg);
            }
        }

        // Remove caught/broken eggs
        for (const egg of eggsToRemove) {
            const index = this.eggs.indexOf(egg);
            if (index > -1) {
                this.eggs.splice(index, 1);
            }
        }
    }

    draw() {
        // Clear canvas
        ctx.fillStyle = COLORS.gray;
        ctx.fillRect(0, 0, WIDTH, HEIGHT);

        // Draw chutes
        ctx.strokeStyle = COLORS.black;
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(100, 50);
        ctx.lineTo(150, 200);
        ctx.moveTo(100, 50);
        ctx.lineTo(150, 400);
        ctx.moveTo(700, 50);
        ctx.lineTo(650, 200);
        ctx.moveTo(700, 50);
        ctx.lineTo(650, 400);
        ctx.stroke();
        ctx.lineWidth = 1;

        // Draw chute tops (egg sources)
        ctx.fillStyle = COLORS.black;
        ctx.beginPath();
        ctx.arc(100, 50, 15, 0, Math.PI * 2);
        ctx.arc(700, 50, 15, 0, Math.PI * 2);
        ctx.fill();

        // Draw eggs
        for (const egg of this.eggs) {
            egg.draw();
        }

        // Draw wolf
        this.wolf.draw();
    }

    updateScore() {
        document.getElementById('score').textContent = this.score;
    }

    updateLives() {
        for (let i = 1; i <= 3; i++) {
            const lifeElement = document.getElementById(`life${i}`);
            if (i <= this.misses) {
                lifeElement.classList.add('lost');
            } else {
                lifeElement.classList.remove('lost');
            }
        }
    }

    endGame() {
        this.gameOver = true;
        document.getElementById('finalScore').textContent = this.score;
        document.getElementById('gameOver').classList.add('show');
    }

    reset() {
        this.wolf = new Wolf();
        this.eggs = [];
        this.score = 0;
        this.misses = 0;
        this.gameOver = false;
        this.eggSpeed = GAME_SETTINGS.eggSpeedStart;
        this.spawnTimer = 0;
        this.spawnInterval = GAME_SETTINGS.initialSpawnInterval;
        
        this.updateScore();
        this.updateLives();
        document.getElementById('gameOver').classList.remove('show');
    }
}

// Initialize game
let game = new Game();
let animationId;

// Game loop
function gameLoop() {
    game.update();
    game.draw();
    animationId = requestAnimationFrame(gameLoop);
}

// Keyboard controls
document.addEventListener('keydown', (e) => {
    const key = e.key.toLowerCase();
    
    if (game.gameOver && (key === ' ' || key === 'spacebar')) {
        game.reset();
        return;
    }

    if (!game.gameOver) {
        switch (key) {
            case 'q':
            case '1':
                game.wolf.move('top_left');
                break;
            case 'a':
            case '2':
                game.wolf.move('bottom_left');
                break;
            case 'p':
            case '9':
                game.wolf.move('top_right');
                break;
            case 'l':
            case '0':
                game.wolf.move('bottom_right');
                break;
        }
    }
});

// Restart button
document.getElementById('restartBtn').addEventListener('click', () => {
    game.reset();
});

// Start game
gameLoop();
