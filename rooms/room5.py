# room1.py

from room_base import BaseRoom

ROOM5_TILE_MAP = [
    
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['c', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b'],
            ['c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b'],
        ]



class Room5(BaseRoom):
    def __init__(self, game):

        super().__init__(ROOM5_TILE_MAP)
        self.room_name = "5"
        self.game_objects = []

        # Add any specific objects or attributes for Room1 here, if necessary.
        # For example, you might have a key in Room1 that the player can pick up:
        # self.add_object(Key(x, y))
