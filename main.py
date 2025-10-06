import pygame
from game.game_engine import GameEngine

# Initialize pygame/Start application
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT)

# ... (Existing imports and setup)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT)
game_over_time = None # NEW: Timer variable for post-game delay

# ... (Existing imports and setup)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT)
# REMOVE: game_over_time = None 
# The main function logic must be updated:

def main():
    running = True
    while running:
        SCREEN.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # --- NEW CODE FOR TASK 3: Menu Input Handling ---
            if not engine.game_active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    engine.reset_game(3)
                elif event.key == pygame.K_5:
                    engine.reset_game(5)
                elif event.key == pygame.K_7:
                    engine.reset_game(7)
                elif event.key == pygame.K_ESCAPE:
                    running = False
            # -----------------------------------------------

        # Check for regular game input only if the game is active
        if engine.game_active:
            engine.handle_input()
        
        engine.update()
        engine.render(SCREEN)

        # REMOVE ALL OLD DELAY LOGIC HERE:
        # if not engine.game_active and game_over_time is None:
        #     game_over_time = pygame.time.get_ticks() + 3000 
        # if game_over_time and pygame.time.get_ticks() > game_over_time:
        #     running = False 

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()