
import pygame
import warnings
def custom_filter(action, category, message, module, lineno, source=None):
    if "iCCP: known incorrect sRGB profile" in str(message):
        return None
    else:
        return action, category, message, module, lineno

# Register the custom filter function
warnings.showwarning = custom_filter



class GameObject:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))

class Crown(GameObject):
     pass  # Specific behaviors for Crown if any

class Key(GameObject):
    pass  # No need to override if it behaves the same way

class LockedDoor(GameObject):
    pass  # Specific behaviors for LockedDoor if any


# class Blob(GameObject):  # Assuming GameObject is a base class for game objects
#     def __init__(self, x, y):
#         # Load the two images for animation
#         self.image1 = pygame.image.load("blob1.png")
#         self.image2 = pygame.image.load("blob2.png")
        
#         # Other attributes, like current image, speed, etc.
#         ...

#     def move_towards_player(self, player):
#         # Logic to move the Blob towards the player
#         ...
    
#     def animate(self):
#         # Switch between blob1.png and blob2.png to create animation effect





class Blob(GameObject):

    def __init__(self, x, y, sprite):
        self.sprite_right = pygame.image.load("blob1.png")
        self.sprite_left = pygame.image.load("blob2.png")
        
        # Start with a default sprite (you can choose either)
        super().__init__(x, y, self.sprite_right)

    def move_towards(self, target_x, target_y):
        # Check the horizontal direction
        if self.x < target_x:  # Moving right
            self.sprite = self.sprite_right
            self.x += 1
        elif self.x > target_x:  # Moving left
            self.sprite = self.sprite_left
            self.x -= 1

        # Move vertically towards the target
        if self.y < target_y:
            self.y += 1
        elif self.y > target_y:
            self.y -= 1

            
    # def update_animation(self, delta_time):
    #     self.animation_timer += delta_time
    #     if self.animation_timer >= 1:  # Assuming delta_time is in seconds
    #         self.current_sprite_index = (self.current_sprite_index + 1) % len(self.sprites)
    #         self.sprite = self.sprites[self.current_sprite_index]
    #         self.animation_timer = 0




