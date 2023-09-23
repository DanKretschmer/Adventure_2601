# room1.py

from room_base import BaseRoom
import pygame
from gameobject import GameObject
from gameobject import Blob

ROOM7_TILE_MAP = [
    
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'c', 'c', 'c', 'c'],
            ['a', 'a', 'a', 'b', 'b', 'a', 'a', 'a', 'a', 'c', 'c', 'c'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c', 'c'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c', 'c'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c'],
            ['b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c', 'c'],
            ['b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c'],
            ['b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c', 'c'],
            ['b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c'],
            ['b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c', 'c'],
        ]



class Room7(BaseRoom):
    def __init__(self, game):

        super().__init__(ROOM7_TILE_MAP)
        self.room_name = "7"

        
        blob_sprite = pygame.image.load("blob1.png")
        self.blob = Blob(350, 300, blob_sprite)
        self.game_objects = [self.blob]
        
        #blob_sprite = pygame.image.load("blob1.png")
       # self.blob = Blob(350, 300, blob_sprite)  # Provide the sprite here
        self.game_objects = [self.blob]

        # Add any specific objects or attributes for Room1 here, if necessary.
        # For example, you might have a key in Room1 that the player can pick up:
        # self.add_object(Key(x, y))
