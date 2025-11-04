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
        
        # Draw wolf head
        pygame.draw.ellipse(surface, (160, 82, 45), 
                          (pos[0] - 25, pos[1] - 40, 50, 60))
        
        # Draw wolf ears
        ear_left = [(pos[0] - 20, pos[1] - 30), 
                    (pos[0] - 30, pos[1] - 45), 
                    (pos[0] - 15, pos[1] - 35)]
        pygame.draw.polygon(surface, BROWN, ear_left)
        
        ear_right = [(pos[0] + 20, pos[1] - 30), 
                     (pos[0] + 30, pos[1] - 45), 
                     (pos[0] + 15, pos[1] - 35)]
        pygame.draw.polygon(surface, BROWN, ear_right)
        
        # Draw wolf snout
        pygame.draw.ellipse(surface, (210, 180, 140), 
                          (pos[0] - 18, pos[1] - 15, 36, 30))
        
        # Draw wolf nose
        pygame.draw.ellipse(surface, BLACK, 
                          (pos[0] - 6, pos[1] - 13, 12, 16))
        
        # Draw eyes
        pygame.draw.circle(surface, WHITE, (pos[0] - 10, pos[1] - 25), 6)
        pygame.draw.circle(surface, WHITE, (pos[0] + 10, pos[1] - 25), 6)
        pygame.draw.circle(surface, BLACK, (pos[0] - 10, pos[1] - 25), 3)
        pygame.draw.circle(surface, BLACK, (pos[0] + 10, pos[1] - 25), 3)
        
        # Draw wolf body
        pygame.draw.ellipse(surface, (160, 82, 45), 
                          (pos[0] - 20, pos[1] + 0, 40, 50))
        
        # Draw arms
        pygame.draw.line(surface, BROWN, 
                        (pos[0] - 15, pos[1] + 5), 
                        (pos[0] - 40, pos[1] + 25), 5)
        pygame.draw.line(surface, BROWN, 
                        (pos[0] + 15, pos[1] + 5), 
                        (pos[0] + 40, pos[1] + 25), 5)
        
        # Draw basket (wicker style)
        basket_points = [
            (pos[0] - 30, pos[1] + 35),
            (pos[0] - 35, pos[1] + 60),
            (pos[0] + 35, pos[1] + 60),
            (pos[0] + 30, pos[1] + 35)
        ]
        pygame.draw.polygon(surface, (210, 105, 30), basket_points)
        pygame.draw.polygon(surface, BROWN, basket_points, 2)
        
        # Basket weave pattern
        for i in range(-30, 31, 8):
            pygame.draw.line(surface, (160, 82, 45), 
                           (pos[0] + i, pos[1] + 35), 
                           (pos[0] + i, pos[1] + 60), 2)
        
        # Basket rim
        pygame.draw.line(surface, (101, 67, 33), 
                        (pos[0] - 30, pos[1] + 35), 
                        (pos[0] + 30, pos[1] + 35), 3)

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
            # Draw egg shadow
            shadow_rect = pygame.Rect(self.x - self.size // 2 + 2, 
                                     self.y - self.size + 2, 
                                     self.size, int(self.size * 1.5))
            shadow_surf = pygame.Surface((self.size + 4, int(self.size * 1.5) + 4), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 50), 
                              (2, 2, self.size, int(self.size * 1.5)))
            surface.blit(shadow_surf, (self.x - self.size // 2, self.y - self.size))
            
            # Draw egg body
            pygame.draw.ellipse(surface, WHITE, (self.x - self.size // 2, 
                                                  self.y - self.size, 
                                                  self.size, int(self.size * 1.5)))
            pygame.draw.ellipse(surface, BLACK, (self.x - self.size // 2, 
                                                  self.y - self.size, 
                                                  self.size, int(self.size * 1.5)), 2)
            
            # Draw egg highlight (shine effect)
            highlight_surf = pygame.Surface((8, 12), pygame.SRCALPHA)
            pygame.draw.ellipse(highlight_surf, (255, 255, 255, 150), (0, 0, 8, 12))
            surface.blit(highlight_surf, (self.x - 7, self.y - self.size - 5))

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
        # Draw gradient background
        for y in range(HEIGHT):
            color_val = int(232 - (y / HEIGHT) * 40)  # Gradient from light to darker gray
            pygame.draw.line(surface, (color_val, color_val, color_val), (0, y), (WIDTH, y))
        
        # Draw decorative border
        pygame.draw.rect(surface, (102, 102, 102), (5, 5, WIDTH - 10, HEIGHT - 10), 5)
        
        # Draw henhouses at the top
        # Left henhouse
        pygame.draw.rect(surface, BROWN, (70, 20, 60, 40))
        pygame.draw.rect(surface, (101, 67, 33), (70, 20, 60, 40), 2)
        # Left roof
        roof_left = [(65, 20), (100, 0), (135, 20)]
        pygame.draw.polygon(surface, BROWN, roof_left)
        pygame.draw.polygon(surface, (101, 67, 33), roof_left, 2)
        
        # Right henhouse
        pygame.draw.rect(surface, BROWN, (670, 20, 60, 40))
        pygame.draw.rect(surface, (101, 67, 33), (670, 20, 60, 40), 2)
        # Right roof
        roof_right = [(665, 20), (700, 0), (735, 20)]
        pygame.draw.polygon(surface, BROWN, roof_right)
        pygame.draw.polygon(surface, (101, 67, 33), roof_right, 2)
        
        # Draw chutes with improved style
        pygame.draw.line(surface, (85, 85, 85), (100, 60), (150, 200), 4)
        pygame.draw.line(surface, (85, 85, 85), (100, 60), (150, 400), 4)
        pygame.draw.line(surface, (85, 85, 85), (700, 60), (650, 200), 4)
        pygame.draw.line(surface, (85, 85, 85), (700, 60), (650, 400), 4)
        
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
