# room1.py

from room_base import BaseRoom

import pygame

ROOM14_TILE_MAP = [
    
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c'],
            ['c', 'a', 'a', 'a', 'c', 'c', 'a', 'a', 'a', 'a', 'c', 'c'],
            ['c', 'a', 'a', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'c', 'c'],
            ['c', 'a', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c'],
            ['c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c'],
            ['c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c'],
            ['c', 'c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'c'],
        ]




class Room14(BaseRoom):
    def __init__(self, game):

        super().__init__(ROOM14_TILE_MAP)
        self.room_name = "14"
        self.game_objects = [] 
        # key_sprite = pygame.image.load("yellowkey.png")
        # self.key_object = Key(300, 300, key_sprite)
        # self.game_objects = [self.key_object]

        # Add any specific objects or attributes for Room1 here, if necessary.
        # For example, you might have a key in Room1 that the player can pick up:
        # self.add_object(Key(x, y))
