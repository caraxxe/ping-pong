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

def main():
    global game_over_time # Need global keyword to modify the variable
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Optional: Allow user to exit immediately after game over
            if game_over_time and event.type == pygame.MOUSEBUTTONDOWN:
                running = False 

        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        # --- NEW CODE FOR TASK 2: Handle Game Over Delay ---
        if not engine.game_active and game_over_time is None:
            # Set timer 3 seconds from now
            game_over_time = pygame.time.get_ticks() + 3000 

        if game_over_time and pygame.time.get_ticks() > game_over_time:
            running = False # Exit the loop after the delay
        # ----------------------------------------------------

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()