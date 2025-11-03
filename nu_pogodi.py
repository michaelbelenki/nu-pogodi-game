import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
BROWN = (139, 69, 19)

# Game settings
EGG_SPEED_START = 2
SPEED_INCREMENT = 0.1
SPEED_INCREASE_INTERVAL = 10

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nu Pogodi - Ну, погоди!")
clock = pygame.time.Clock()

# Fonts
font_large = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 36)

class Wolf:
    def __init__(self):
        self.positions = {
            'top_left': (150, 200),
            'bottom_left': (150, 400),
            'top_right': (650, 200),
            'bottom_right': (650, 400)
        }
        self.current_position = 'bottom_left'
        self.size = 60
    
    def move(self, position):
        if position in self.positions:
            self.current_position = position
    
    def draw(self, surface):
        pos = self.positions[self.current_position]
        # Draw wolf as a simple character
        pygame.draw.circle(surface, BROWN, pos, self.size // 2)
        # Draw basket
        basket_rect = pygame.Rect(pos[0] - 40, pos[1] + 20, 80, 30)
        pygame.draw.rect(surface, YELLOW, basket_rect, 3)

class Egg:
    def __init__(self, lane):
        self.lane = lane
        self.lanes = {
            'top_left': (100, 50, 150, 200),
            'bottom_left': (100, 50, 150, 400),
            'top_right': (700, 50, 650, 200),
            'bottom_right': (700, 50, 650, 400)
        }
        self.start_x, self.start_y, self.end_x, self.end_y = self.lanes[lane]
        self.x = self.start_x
        self.y = self.start_y
        self.size = 20
        self.caught = False
        self.broken = False
    
    def update(self, speed):
        if not self.caught and not self.broken:
            # Move egg towards target position
            dx = (self.end_x - self.start_x) / 100
            dy = (self.end_y - self.start_y) / 100
            self.x += dx * speed
            self.y += dy * speed
            
            # Check if reached end
            if abs(self.x - self.end_x) < 10 and abs(self.y - self.end_y) < 10:
                return True
        return False
    
    def draw(self, surface):
        if not self.caught and not self.broken:
            pygame.draw.ellipse(surface, WHITE, (self.x - self.size // 2, 
                                                  self.y - self.size, 
                                                  self.size, self.size * 1.5))
            pygame.draw.ellipse(surface, BLACK, (self.x - self.size // 2, 
                                                  self.y - self.size, 
                                                  self.size, self.size * 1.5), 2)

class Game:
    def __init__(self):
        self.wolf = Wolf()
        self.eggs = []
        self.score = 0
        self.misses = 0
        self.max_misses = 3
        self.game_over = False
        self.egg_speed = EGG_SPEED_START
        self.spawn_timer = 0
        self.spawn_interval = 120
        self.lanes = ['top_left', 'bottom_left', 'top_right', 'bottom_right']
    
    def spawn_egg(self):
        lane = random.choice(self.lanes)
        self.eggs.append(Egg(lane))
    
    def check_catch(self, egg):
        if egg.lane == self.wolf.current_position:
            egg.caught = True
            self.score += 1
            # Increase speed every 10 eggs
            if self.score % SPEED_INCREASE_INTERVAL == 0:
                self.egg_speed += SPEED_INCREMENT
                self.spawn_interval = max(60, self.spawn_interval - 5)
            return True
        return False
    
    def update(self):
        if self.game_over:
            return
        
        # Spawn eggs
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_egg()
            self.spawn_timer = 0
        
        # Update eggs
        eggs_to_remove = []
        for egg in self.eggs:
            if egg.update(self.egg_speed):
                if not self.check_catch(egg):
                    egg.broken = True
                    self.misses += 1
                    if self.misses >= self.max_misses:
                        self.game_over = True
                eggs_to_remove.append(egg)
        
        # Remove caught/broken eggs
        for egg in eggs_to_remove:
            self.eggs.remove(egg)
    
    def draw(self, surface):
        surface.fill(GRAY)
        
        # Draw chutes
        for lane_name, (sx, sy, ex, ey) in self.eggs[0].lanes.items() if self.eggs else []:
            pass
        
        # Draw simple chutes
        pygame.draw.line(surface, BLACK, (100, 50), (150, 200), 3)
        pygame.draw.line(surface, BLACK, (100, 50), (150, 400), 3)
        pygame.draw.line(surface, BLACK, (700, 50), (650, 200), 3)
        pygame.draw.line(surface, BLACK, (700, 50), (650, 400), 3)
        
        # Draw eggs
        for egg in self.eggs:
            egg.draw(surface)
        
        # Draw wolf
        self.wolf.draw(surface)
        
        # Draw UI
        score_text = font_medium.render(f"Score: {self.score}", True, BLACK)
        surface.blit(score_text, (WIDTH // 2 - 100, 20))
        
        # Draw misses
        for i in range(self.max_misses):
            color = RED if i < self.misses else WHITE
            pygame.draw.circle(surface, color, (50 + i * 40, 30), 15)
            pygame.draw.circle(surface, BLACK, (50 + i * 40, 30), 15, 2)
        
        if self.game_over:
            game_over_text = font_large.render("GAME OVER", True, RED)
            restart_text = font_small.render("Press SPACE to restart", True, BLACK)
            surface.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
            surface.blit(restart_text, (WIDTH // 2 - 180, HEIGHT // 2 + 20))
    
    def reset(self):
        self.__init__()

# Main game loop
def main():
    game = Game()
    running = True
    
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if game.game_over and event.key == pygame.K_SPACE:
                    game.reset()
                elif not game.game_over:
                    if event.key == pygame.K_q or event.key == pygame.K_1:
                        game.wolf.move('top_left')
                    elif event.key == pygame.K_a or event.key == pygame.K_2:
                        game.wolf.move('bottom_left')
                    elif event.key == pygame.K_p or event.key == pygame.K_9:
                        game.wolf.move('top_right')
                    elif event.key == pygame.K_l or event.key == pygame.K_0:
                        game.wolf.move('bottom_right')
        
        game.update()
        game.draw(screen)
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
