# room1.py

from room_base import BaseRoom
import pygame
from gameobject import Blob


ROOM12_TILE_MAP = [
    
            ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'],
            ['a', 'a', 'c', 'a', 'c', 'a', 'c', 'a', 'c', 'c', 'c', 'a'],
            ['a', 'a', 'a', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'c', 'a', 'c', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'c', 'c', 'a', 'a', 'c', 'c', 'a', 'a', 'c', 'c'],
            ['a', 'a', 'c', 'c', 'a', 'a', 'c', 'c', 'a', 'a', 'c', 'c'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'c', 'c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'],
        ]



class Room12(BaseRoom):
     def __init__(self, game):

        super().__init__(ROOM12_TILE_MAP)
        self.room_name = "12"
        blob_sprite = pygame.image.load("blob1.png")
        self.blob = Blob(300, 300, blob_sprite)
        self.game_objects = [self.blob]


        # Add any specific objects or attributes for Room1 here, if necessary.
        # For example, you might have a key in Room1 that the player can pick up:
        # self.add_object(Key(x, y))
