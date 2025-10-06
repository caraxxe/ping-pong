import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

    def move(self, player, ai):
        # 1. Store the previous X position before movement
        old_x = self.x 
        
        # 2. Move in the X direction
        self.x += self.velocity_x

        # 3. Check X-axis collision immediately after moving X
        # We must check against both paddles (player and AI)
        if self.rect().colliderect(player.rect()) or self.rect().colliderect(ai.rect()):
            # Revert the position to before the collision happened
            self.x = old_x 
            # Reverse the velocity
            self.velocity_x *= -1
            # Optional: Add randomness to Y velocity on hit (better gameplay)
            self.velocity_y = random.choice([-5, 5]) 

        # 4. Move in the Y direction
        self.y += self.velocity_y

        # 5. Check Y-axis collision (Wall Bounce)
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1

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