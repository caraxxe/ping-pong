import pygame
from .paddle import Paddle
from .ball import Ball

# Game Engine

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # ... (paddle dimensions and init)

        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)

        # --- UPDATED CODE FOR TASK 3 ---
        self.initial_max_score = 5 # Store the default score
        self.max_score = self.initial_max_score
        self.game_active = True
        self.winner = None
        # -------------------------------

# ... (rest of class)

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
        # ... (Existing code for drawing paddles, ball, divider, and scores)
        
        if not self.game_active:
            # 1. Draw Winner Text
            winner_text = ""
            if self.winner == "Player":
                winner_text = "PLAYER WINS!"
            elif self.winner == "AI":
                winner_text = "AI WINS!"
            
            game_over_font = pygame.font.SysFont("Arial", 70, bold=True)
            text_surface = game_over_font.render(winner_text, True, WHITE)
            text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2 - 50))
            screen.blit(text_surface, text_rect)
            
            # 2. Draw Replay Options
            menu_font = pygame.font.SysFont("Arial", 40)
            
            menu_options = [
                ("3: Best of 3", 3),
                ("5: Best of 5", 5),
                ("7: Best of 7", 7),
                ("ESC: Exit", 0)
            ]
            
            y_offset = self.height // 2 + 50
            for text, _ in menu_options:
                option_surface = menu_font.render(text, True, WHITE)
                option_rect = option_surface.get_rect(center=(self.width // 2, y_offset))
                screen.blit(option_surface, option_rect)
                y_offset += 50
        
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

        # Add this method to the GameEngine class
    def reset_game(self, new_max_score):
        # Update the target score
        self.max_score = new_max_score
        
        # Reset scores
        self.player_score = 0
        self.ai_score = 0
        
        # Reset game state
        self.game_active = True
        self.winner = None
        
        # Reset the ball position and direction
        self.ball.reset()