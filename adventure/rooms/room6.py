# room1.py

from room_base import BaseRoom
from gameobject import GameObject
from gameobject import Key



import pygame

ROOM6_TILE_MAP = [
    
            ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'],
            ['c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
            ['a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'c'],
        ]




class Room6(BaseRoom):
    def __init__(self, game):

        
        #from game import Game
        super().__init__(ROOM6_TILE_MAP)
        self.room_name = "6"
        self.game_objects = [] 
        if not game.has_key:
            key_sprite = pygame.image.load("yellowkey.png")
            self.key_object = Key(350, 300, key_sprite)
            self.game_objects = [self.key_object]

        # Add any specific objects or attributes for Room1 here, if necessary.
        # For example, you might have a key in Room1 that the player can pick up:
        # self.add_object(Key(x, y))
