import pygame
from person import Person
import warnings
import sys
import importlib
from pygame.locals import QUIT
from gameobject import GameObject, Key, Crown, LockedDoor, Blob
import traceback
#from rooms import room6 as roommodule
from rooms.room6 import Room6
import random


# Custom filter function to ignore the specific warning message
def custom_filter(action, category, message, module, lineno, source=None):
    if "iCCP: known incorrect sRGB profile" in str(message):
        return None
    else:
        return action, category, message, module, lineno

# Register the custom filter function
warnings.showwarning = custom_filter

warnings.simplefilter("ignore")

# Screen Dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()
global font
font = pygame.font.SysFont(None, 55)

# Tile types
WALKABLE_TILE = 0
NON_WALKABLE_TILE = 1
WALL_TILE = 2
WALL_IMAGE_PATH = "wall.jpg"
DOOR = 3
DOOR2 = 4


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Image paths
all_sprites = pygame.sprite.Group()
PERSON_IMAGE_PATH = "person.png"
PERSON_IMAGE_RIGHT_PATH = "personright.png"
TILE_IMAGE_PATH = "tile.png"
WATER_IMAGE_PATH = "water.jpg"
DOOR_IMAGE_PATH = "door.png"
DOOR2_IMAGE_PATH = "door2.png"
won = False

# Tile Mapping
TILE_DICT = {
    'a': WALKABLE_TILE,
    'b': NON_WALKABLE_TILE,
    'c': WALL_TILE,
    'd': DOOR,
    'e': DOOR2
}

pygame.mixer.init()
key_sound = pygame.mixer.Sound('sounds/key.wav')
win_sound = pygame.mixer.Sound('sounds/win.wav')
open = pygame.mixer.Sound('sounds/thud.mp3')
pop = pygame.mixer.Sound('sounds/pop.mp3')




def load_room(room_name, game):
    # Dynamically import the room module.
    
    room_module = importlib.import_module(f"rooms.{room_name}")
    room_class_name = room_name[0].upper() + room_name[1:]
    room_class = getattr(room_module, room_class_name)
    # Instantiate the class and return the room object.
    return room_class(game)



def get_room_by_name(name, game):
    room_module = importlib.import_module(f"rooms.{name}")
    room_class_name = name.capitalize() 
    room_class = getattr(room_module, room_class_name)
    return room_class()  # Note: this creates a new instance, adjust if necessary


all_room_names = [f"room{i}" for i in range(1, 15)]
ROOMS_WITHOUT_BLOBS = ["room1", "room2", "room6"]
rooms_with_blobs_names = random.sample([name for name in all_room_names if name not in ROOMS_WITHOUT_BLOBS], 3)


def get_room_by_name(room_name, game):
    room_module = importlib.import_module(f"rooms.{room_name}")
    room_class_name = room_name[0].upper() + room_name[1:]
    room_class = getattr(room_module, room_class_name)
    return room_class(game)

   

def check_object_collision(obj1, obj2):
    if isinstance(obj1, Person):
        obj1_sprite_width = obj1.image_left.get_width()
        obj1_sprite_height = obj1.image_left.get_height()
    else:
        obj1_sprite_width = obj1.sprite.get_width()
        obj1_sprite_height = obj1.sprite.get_height()

    return (obj1.x < obj2.x + obj2.sprite.get_width() and
            obj1.x + obj1_sprite_width > obj2.x and
            obj1.y < obj2.y + obj2.sprite.get_height() and
            obj1.y + obj1_sprite_height > obj2.y)



def change_door_to_walkable(self):

    new_tile_map = []
    for row in self.get_current_room().get_tile_map():  # Access the current room through the Game class method
        new_row = [tile if tile not in ['d', 'e'] else 'a' for tile in row]
        new_tile_map.append(new_row)
    self.get_current_room().set_tile_map(new_tile_map)  # Access the current room through the Game class method

class Game:
    def __init__(self):
        pygame.init()
        self.game_over = False
        self.countdown_started = None
        self.countdown_started2 = None
        
        self.blob_sprites = [pygame.image.load("blob1.png"), pygame.image.load("blob2.png")]

        x, y = 100, 100  # Or whatever starting coordinates you want for the blob
        self.blob = Blob(x, y, self.blob_sprites)

        
        self.SPEED = 8
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Game')
        
        self.background_image = pygame.image.load(TILE_IMAGE_PATH).convert_alpha()
        self.water_image = pygame.image.load(WATER_IMAGE_PATH).convert_alpha()
        self.door_image = pygame.image.load(DOOR_IMAGE_PATH).convert_alpha()
        self.door2_image = pygame.image.load(DOOR2_IMAGE_PATH).convert_alpha()
        self.wall_image = pygame.image.load(WALL_IMAGE_PATH).convert_alpha()
        self.walkable_characters = ['a']
        self.tile_width = self.background_image.get_width()
        self.tile_height = self.background_image.get_height()
        self.current_room = load_room('room1', self)
        self.current_room_name = load_room('room1', self)
        self.has_key= False
        self.played_crown_sound = False
        
      #  self.current_room = load_room(self.current_room_name)  # Set the current room using current_room_name

        self.person_image_left = pygame.image.load(PERSON_IMAGE_PATH).convert_alpha()
        self.person_image_right = pygame.image.load(PERSON_IMAGE_RIGHT_PATH).convert_alpha()
        self.person = Person(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, self.person_image_left, self.person_image_right)

        self.person_moving_up = False
        self.person_moving_down = False
        self.person_moving_left = False
        self.person_moving_right = False



        self.WORLD_MAP = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '5', '7', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '4', '8', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '3', '2', '1', '6', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '9', '0', '0', '14', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '10', '11', '12', '13', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
]
    def get_tile_at(self, x, y):
        return self.current_room.get_tile_at(x, y)
    
    def get_current_room(self):
        
        return self.current_room


    def get_adjacent_room(self, current_room_name, direction):
       

        for y, row in enumerate(self.WORLD_MAP):
            for x, room in enumerate(row):
                if room == current_room_name:  
                    
                    if direction == "left" and x - 1 >= 0:
                        return self.WORLD_MAP[y][x-1]
                    elif direction == "right" and x + 1 < len(row):
                        return self.WORLD_MAP[y][x+1]
                    elif direction == "up" and y - 1 >= 0:
                        return self.WORLD_MAP[y-1][x]
                    elif direction == "down" and y + 1 < len(self.WORLD_MAP):
                        return self.WORLD_MAP[y+1][x]
        
        return '0'


    def is_tile_walkable(self, x, y):
        tile_x = x // self.tile_width
        tile_y = y // self.tile_height
            
        # Check if the coordinates are within bounds
        if tile_x < 0 or tile_x >= len(self.current_room.get_tile_map()[0]) or \
        tile_y < 0 or tile_y >= len(self.current_room.get_tile_map()):
            return False

        # Get the tile character from the map
        tile_char = self.current_room.get_tile_map()[tile_y][tile_x]

        # Get the tile type
        tile_type = TILE_DICT.get(tile_char, WALKABLE_TILE)
        result = tile_type = TILE_DICT.get(tile_char, WALKABLE_TILE)

        return tile_type == WALKABLE_TILE



    def is_tile_walkable_in_room(self, room_name, x, y, width=0, height=0):
        temp_room = load_room(f"room{room_name}", self)


        # Convert the top-left and bottom-right pixel coordinates to tile coordinates
        tile_x1 = x // self.tile_width
        tile_y1 = y // self.tile_height
        tile_x2 = (x + width) // self.tile_width
        tile_y2 = (y + height) // self.tile_height

        # Check if the sprite coordinates are within bounds
        if (tile_x1 < 0 or tile_x2 >= len(temp_room.get_tile_map()[0]) or
            tile_y1 < 0 or tile_y2 >= len(temp_room.get_tile_map())):
            return False

        # Check all tiles the sprite occupies
        for check_y in range(tile_y1, tile_y2 + 1):
            for check_x in range(tile_x1, tile_x2 + 1):
                tile_char = temp_room.get_tile_map()[check_y][check_x]
                if tile_char not in self.walkable_characters:
                    return False

        return True


    
    def run(self):
        running = True
        clock = pygame.time.Clock()
        


        while running:
            font = pygame.font.SysFont(None, 55)
            clock.tick(60)

            if self.countdown_started:
                elapsed_time = pygame.time.get_ticks() - self.countdown_started
                if elapsed_time >= 2000:  # 2000 milliseconds = 2 seconds
                    sys.exit()


            if won == True:
                screen.fill(BLACK)
                text = font.render("YOU WON!", True, WHITE)
                screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))



            for game_object in self.current_room.game_objects:
                if isinstance(game_object, Key):
                    if self.has_key == False:
                        if check_object_collision(self.person, game_object):
                            self.person.has_key = True
                            self.has_key = True
                            key_sound.play()
                            self.current_room.game_objects.remove(game_object)
                            break
                
                
                if isinstance(game_object, Crown):
                    if check_object_collision(self.person, game_object):
                        if not self.played_crown_sound:
                            self.played_crown_sound = True
                            win_sound.play()
                        self.countdown_started = pygame.time.get_ticks()
                        game_state = won
                        game_over = True

                if isinstance(game_object, LockedDoor):
                    if check_object_collision(self.person, game_object):
                        if self.has_key == True:
                            open.play()
                            self.current_room.game_objects.remove(game_object)
                        

                if isinstance(game_object, Blob):
                    game_object.move_towards(self.person.x, self.person.y)
                    if check_object_collision(self.person, game_object):
                
                        if not self.countdown_started2:
                            pop_sound = pygame.mixer.Sound("sounds/pop.mp3")
                            pop_sound.play()
                            self.countdown_started2 = pygame.time.get_ticks()
                        
                        elapsed_time2 = pygame.time.get_ticks() - self.countdown_started2

                        if elapsed_time2 >= 500:  
                                # For now, you're exiting the game immediately
                            sys.exit()
                       
   

                
                        
                

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    elif e.key == pygame.K_UP:
                        if not self.game_over:
                            self.person_moving_up = True
                    elif e.key == pygame.K_DOWN:
                        if not self.game_over:
                            self.person_moving_down = True
                    elif e.key == pygame.K_LEFT:
                        if not self.game_over:
                            self.person_moving_left = True
                       # self.facingleft = True
                    elif e.key == pygame.K_RIGHT:
                        if not self.game_over:
                            self.person_moving_right = True
                      #  self.facingleft = False

                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        self.person_moving_up = False
                    elif e.key == pygame.K_DOWN:
                        self.person_moving_down = False
                    elif e.key == pygame.K_LEFT:
                        self.person_moving_left = False
                    elif e.key == pygame.K_RIGHT:
                        self.person_moving_right = False

            if not self.game_over:
                if self.person_moving_up:
                    
                    if self.person.y - self.SPEED <= 0:  # About to move out of screen
                        next_room = self.get_adjacent_room(self.current_room.room_name, "up")
                        
                        new_x = self.person.x
                        new_y = SCREEN_HEIGHT - self.person_image_left.get_height()
                        if next_room != '0' and self.is_tile_walkable_in_room(next_room, new_x, new_y):
                            
                            self.current_room = load_room(f"room{next_room}", self)
                            self.current_room_name = f"room{next_room}"
                            self.current_room = load_room(self.current_room_name, self)


                            self.person.y = SCREEN_HEIGHT - self.person_image_left.get_height() - self.SPEED
                    elif self.is_tile_walkable(self.person.x, self.person.y - self.SPEED):
                        self.person.move(0, -self.SPEED, self)

            if not self.game_over:
                if self.person_moving_down:
                    if self.person.y + self.person_image_left.get_height() + self.SPEED >= SCREEN_HEIGHT:
                        next_room = self.get_adjacent_room(self.current_room.room_name, "down")
                        new_x = self.person.x
                        new_y = 0
                        if next_room != '0' and self.is_tile_walkable_in_room(next_room, new_x, new_y):
                            self.current_room = load_room(f"room{next_room}", self)
                            self.person.y = 0 + self.SPEED  # Place the person at the top of the new room, and add the speed to account for the movement
                    
            
                    elif self.is_tile_walkable(self.person.x, self.person.y + self.SPEED):
                        self.person.move(0, self.SPEED, self)

    

            if not self.game_over:
                if self.person_moving_left:
                    if self.person.x - self.SPEED <= 0:
                        next_room = self.get_adjacent_room(self.current_room.room_name, "left")
                        # Calculate new position in the new room
                        new_x = SCREEN_WIDTH - self.person_image_left.get_width()
                        new_y = self.person.y
                        if next_room != '0' and self.is_tile_walkable_in_room(next_room, new_x, new_y):
                            self.current_room = load_room(f"room{next_room}", self)
                            self.person.x = SCREEN_WIDTH - self.person_image_left.get_width() - self.SPEED
                    elif self.is_tile_walkable(self.person.x - self.SPEED, self.person.y):
                        self.person.move(-self.SPEED, 0, self)


            if not self.game_over:
                if self.person_moving_right:
    
                    for game_object in self.current_room.game_objects:
                        if isinstance(game_object, Key):
                    
                            break
                    if self.person.x + self.person_image_left.get_width() + self.SPEED >= SCREEN_WIDTH:
                        next_room = self.get_adjacent_room(self.current_room.room_name, "right")
                        new_x = 0 
                        new_y = self.person.y
                        if next_room != '0' and self.is_tile_walkable_in_room(next_room, new_x, new_y):
                            self.current_room = load_room(f"room{next_room}", self)
                            self.person.x = 0 + self.SPEED
                    elif self.is_tile_walkable(self.person.x + self.SPEED, self.person.y):
                            self.person.move(self.SPEED, 0, self)



            # Drawing
            self._draw_background()
            self.person.draw(self.surface)
            for obj in self.current_room.game_objects:
                obj.draw(self.surface)
            pygame.display.flip()

        pygame.quit()
    


    def _draw_background(self):
        for tile_x in range(len(self.current_room.get_tile_map()[0])):
            for tile_y in range(len(self.current_room.get_tile_map())):
                x = tile_x * self.tile_width
                y = tile_y * self.tile_height

                tile_char = self.current_room.get_tile_map()[tile_y][tile_x]
                tile_type = TILE_DICT.get(tile_char, WALKABLE_TILE)
                if tile_type == WALKABLE_TILE:
                    self.surface.blit(self.background_image, (x, y))
                elif tile_type == NON_WALKABLE_TILE:
                    self.surface.blit(self.water_image, (x, y))
                elif tile_type == WALL_TILE:
                    self.surface.blit(self.wall_image, (x, y))
                elif tile_type == DOOR:
                    self.surface.blit(self.door_image, (x, y))
                elif tile_type == DOOR2:
                    self.surface.blit(self.door2_image, (x, y))


# To run the game
if __name__ == "__main__":
    game = Game()
    game.run()
