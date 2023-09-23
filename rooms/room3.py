# room1.py

from room_base import BaseRoom

ROOM3_TILE_MAP = [
    
            ['c', 'a', 'a', 'a', 'a', 'c', 'c', 'c', 'c', 'c', 'c', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'c', 'a', 'c', 'a', 'c', 'c'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'c', 'c', 'c', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
        ]



class Room3(BaseRoom):
    def __init__(self, game):

        super().__init__(ROOM3_TILE_MAP)
        self.room_name = "3"
        self.game_objects = []

        # Add any specific objects or attributes for Room1 here, if necessary.
        # For example, you might have a key in Room1 that the player can pick up:
        # self.add_object(Key(x, y))
