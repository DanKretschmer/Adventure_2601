# room1.py
import pygame
from room_base import BaseRoom
from gameobject import GameObject
from gameobject import LockedDoor

ROOM8_TILE_MAP = [
    
            ['b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
            ['b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
            ['c', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
            ['c', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
            ['c', 'a', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
            ['c', 'a', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
            ['c', 'c', 'c', 'c', 'c', 'a', 'a', 'a', 'c', 'c', 'c', 'c'],
            ['c', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
            ['c', 'a', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
            ['c', 'b', 'a', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
            ['c', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'b'],
            ['c', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'b'],
        ]





class Room8(BaseRoom):
    def __init__(self, game):

        super().__init__(ROOM8_TILE_MAP)
        self.room_name = "8"
        
        
        # self.locked_door = LockedDoor(300, 300, "door.png")
        # self.game_objects = [self.locked_door]

        door_sprite = pygame.image.load("door.jpg")
        self.LockedDoor = LockedDoor(250, 300, door_sprite)
        self.game_objects = [self.LockedDoor]



        # door_sprite = pygame.image.load("door.png")
        # self.LockedDoor = (300, 300, door_sprite)
        # self.game_objects = [self.LockedDoor]

        # Add any specific objects or attributes for Room1 here, if necessary.
        # For example, you might have a key in Room1 that the player can pick up:
        # self.add_object(Key(x, y))
       # def set_tile_map(self, new_tile_map):
       #     self.tile_map = new_tile_map
    def set_tile_map(self, new_tile_map):
        self.tile_map = new_tile_map

