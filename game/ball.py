# game/ball.py

import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        # ... (Existing init code)
        self.velocity_y = random.choice([-3, 3])
        
        # --- NEW CODE FOR TASK 4: Load Sounds ---
        try:
            # Load sounds assuming they are in an 'assets' folder relative to the execution path
            self.paddle_sound = pygame.mixer.Sound('assets/paddle.wav') 
            self.wall_sound = pygame.mixer.Sound('assets/wall.wav')
        except pygame.error as e:
            print(f"Warning: Could not load sound files: {e}")
            self.paddle_sound = None
            self.wall_sound = None
        # ------------------------------------------

    def move(self, player, ai):
        old_x = self.x 
        
        # 2. Move in the X direction
        self.x += self.velocity_x

        # 3. Check X-axis collision (PADDLE HIT)
        if self.rect().colliderect(player.rect()) or self.rect().colliderect(ai.rect()):
            # ... (Existing collision fix code)
            self.x = old_x 
            self.velocity_x *= -1
            self.velocity_y = random.choice([-5, 5])
            
            # --- NEW CODE FOR TASK 4: Play Paddle Sound ---
            if self.paddle_sound:
                self.paddle_sound.play()
            # -----------------------------------------------

        # 4. Move in the Y direction
        self.y += self.velocity_y

        # 5. Check Y-axis collision (WALL BOUNCE)
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            
            # --- NEW CODE FOR TASK 4: Play Wall Sound ---
            if self.wall_sound:
                self.wall_sound.play()
            # --------------------------------------------

    # ... (rest of Ball class)


    # NOTE: The separate check_collision method is now obsolete and should be removed or changed.
    def check_collision(self, player, ai):
        # This method is now only needed if the GameEngine calls it, but we moved the logic to move().
        # If GameEngine is updated (see below), this method is no longer necessary.
        pass 
        
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)