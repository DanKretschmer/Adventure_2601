# room1.py
import pygame
from room_base import BaseRoom
from gameobject import GameObject
from gameobject import Crown

ROOM1_TILE_MAP = [
    
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['b', 'b', 'b', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'],
        ]





class Room1(BaseRoom):
    def __init__(self, game):
        super().__init__(ROOM1_TILE_MAP)
        self.room_name = "1"
        
        
        crown_sprite = pygame.image.load("crown.png")
        self.crown_object = Crown(100, 250, crown_sprite)
        self.game_objects = [self.crown_object]

        # Add any specific objects or attributes for Room1 here, if necessary.
        # For example, you might have a key in Room1 that the player can pick up:
        # self.add_object(Key(x, y))
