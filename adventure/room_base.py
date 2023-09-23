# room_base.py
import traceback
import pygame
from gameobject import Blob 

class BaseRoom:
    def __init__(self, tile_map, objects=None):
        """
        Initialize a base room.
        
        :param tile_map: A 2D list representing the tiles in the room.
        :param objects: A list of game objects present in the room. Default is an empty list.
        """
        self.tile_map = tile_map
        self.objects = objects if objects else []

    def get_tile_at(self, tile_x, tile_y):
        if 0 <= tile_y < len(self.tile_map) and 0 <= tile_x < len(self.tile_map[0]):
            return self.tile_map[tile_y][tile_x]
        else:
            
            return None

    
    def get_tile_map(self):
        """
        Return the tile map of the room.
        """
        return self.tile_map
    
    def get_objects(self):
        """
        Return the list of objects in the room.
        """
        return self.objects
    
    def add_object(self, obj):
        """
        Add an object to the room.
        
        :param obj: The object to be added.
        """
        self.objects.append(obj)
    
    def remove_object(self, obj):
        """
        Remove an object from the room.
        
        :param obj: The object to be removed.
        """
        self.objects.remove(obj)

    # def add_blob(self, x, y):
    #     blob_sprite = pygame.image.load("blob.png")
    #     blob_object = Blob(x, y, blob_sprite)
    #     self.game_objects.append(blob_object)
    #     print("blob added")
    
    # Additional common methods for rooms can be added here.
