# game/game_engine.py

import pygame
from .paddle import Paddle
from .ball import Ball

# Game Engine

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        # ... (Existing init code)
        self.game_active = True
        self.winner = None
        
        # --- NEW CODE FOR TASK 4: Load Score Sound ---
        try:
            self.score_sound = pygame.mixer.Sound('assets/score.wav')
        except pygame.error as e:
            print(f"Warning: Could not load score sound file: {e}")
            self.score_sound = None
        # --------------------------------------------

    # ... (handle_input method)

    def update(self):
        # ... (Existing update code)

        self.ball.move(self.player, self.ai) 

        # Check for scoring (left wall)
        if self.ball.x <= 0:
            self.ai_score += 1
            self.ball.reset()
            # --- NEW CODE FOR TASK 4: Play Score Sound ---
            if self.score_sound:
                self.score_sound.play()
            # --------------------------------------------
            
        # Check for scoring (right wall)
        elif self.ball.x >= self.width:
            self.player_score += 1
            self.ball.reset()
            # --- NEW CODE FOR TASK 4: Play Score Sound ---
            if self.score_sound:
                self.score_sound.play()
            # --------------------------------------------

        # ... (rest of update method)

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