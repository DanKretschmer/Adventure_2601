# room1.py
import pygame
from gameobject import Blob
from room_base import BaseRoom

ROOM9_TILE_MAP = [
    
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'c'],
            ['c', 'a', 'a', 'b', 'b', 'a', 'a', 'a', 'a', 'c', 'a', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'a', 'c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'c', 'c'],
            ['c', 'a', 'c', 'b', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'a', 'c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'c', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
        ]



class Room9(BaseRoom):
    def __init__(self, game):

        super().__init__(ROOM9_TILE_MAP)
        self.room_name = "9"
        blob_sprite = pygame.image.load("blob1.png")
        self.blob = Blob(250, 500, blob_sprite)
        self.game_objects = [self.blob]

        
        # Add any specific objects or attributes for Room1 here, if necessary.
        # For example, you might have a key in Room1 that the player can pick up:
        
