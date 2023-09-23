from rooms.room8 import Room8

class Person:
    def __init__(self, x, y, image_left, image_right):
        self.x = x
        self.y = y
        self.image_left = image_left
        self.image_right = image_right
        self.current_image = self.image_left   # default image
        self.has_key = False
        # ... other properties ...


    def move(self, dx, dy, game):
       
        

        new_x = self.x + dx
        new_y = self.y + dy
        

        tile = game.get_tile_at(new_x, new_y) # assuming you have a reference to the game instance
        if tile in ['d', 'e'] and self.has_key:
            game.change_door_to_walkable()
        
    #     current_room = game.get_current_room()
    #     if not game.has_key and self.y > 248 and isinstance(game.get_current_room(), Room8):
        # if not game.has_key and self.y > 250 and game.get_current_room() == 'rooms.room8.Room8':
        #     new_y = new_y

       # if not (new_y > self.y and not game.has_key and isinstance(game.get_current_room(), Room8)):
       #     self.y = new_y

        
    #         print(f"Has key: {self.has_key}")
    #         print(f"New y: {new_y}")
    #         print(f"Current room: {game.get_current_room()}")

    #         return
    #     #     Don't allow the movement to the right beyond x=300
  
    
    # Left movement
        if dx < 0:
            if game.is_tile_walkable(new_x, self.y) and game.is_tile_walkable(new_x, self.y + self.current_image.get_height()):
                self.x = new_x
                self.current_image = self.image_left
    
    # Right movement
        elif dx > 0:
            if game.is_tile_walkable(new_x + self.current_image.get_width(), self.y) and game.is_tile_walkable(new_x + self.current_image.get_width(), self.y + self.current_image.get_height()):
                self.x = new_x
                self.current_image = self.image_right
        
        # Up movement
        if dy < 0:
            if game.is_tile_walkable(self.x, new_y) and game.is_tile_walkable(self.x + self.current_image.get_width(), new_y):
                self.y = new_y
                # If you have up and down images, you can set the appropriate image here
    
        

        # Down movement
        elif dy > 0:
            # if game.is_tile_walkable(self.x, new_y + self.current_image.get_height()) and game.is_tile_walkable(self.x + self.current_image.get_width(), new_y + self.current_image.get_height()):
            #     self.y = new_y
                # Similarly, if you have a down image, set it here
            
            if not (new_y > 248 and not game.has_key and isinstance(game.get_current_room(), Room8)):
                if game.is_tile_walkable(self.x, new_y + self.current_image.get_height()) and game.is_tile_walkable(self.x + self.current_image.get_width(), new_y + self.current_image.get_height()):
                    self.y = new_y


    def draw(self, surface):
        surface.blit(self.current_image, (self.x, self.y))
