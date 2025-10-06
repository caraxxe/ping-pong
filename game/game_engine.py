import pygame
from .paddle import Paddle
from .ball import Ball

# Game Engine

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # 1. DEFINE PADDLE DIMENSIONS FIRST
        self.paddle_width = 10
        self.paddle_height = 100

        # 2. THEN INITIALIZE PADDLES (using the defined attributes)
        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height)

        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)

        # ... (rest of your new Task 2 code)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-10, self.height)
        if keys[pygame.K_s]:
            self.player.move(10, self.height)

    def update(self):
        # --- NEW CODE FOR TASK 2 ---
        if not self.game_active:
            return
        # ---------------------------

        self.ball.move(self.player, self.ai) 

        if self.ball.x <= 0:
            self.ai_score += 1
            self.ball.reset()
        elif self.ball.x >= self.width:
            self.player_score += 1
            self.ball.reset()

        # --- NEW CODE FOR TASK 2: Check for Game Over ---
        if self.player_score >= self.max_score:
            self.game_active = False
            self.winner = "Player"
        elif self.ai_score >= self.max_score:
            self.game_active = False
            self.winner = "AI"
        # ------------------------------------------------

        self.ai.auto_track(self.ball, self.height)

    def render(self, screen):
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width//2, 0), (self.width//2, self.height))

        # Draw score
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width//4, 20))
        screen.blit(ai_text, (self.width * 3//4, 20))
        
        # --- NEW CODE FOR TASK 2: Draw Game Over Screen ---
        if not self.game_active:
            winner_text = ""
            if self.winner == "Player":
                winner_text = "PLAYER WINS!"
            elif self.winner == "AI":
                winner_text = "AI WINS!"
            
            game_over_font = pygame.font.SysFont("Arial", 70, bold=True)
            text_surface = game_over_font.render(winner_text, True, WHITE)
            text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
            screen.blit(text_surface, text_rect)
        # ------------------------------------------------