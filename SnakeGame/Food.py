from Snake import *


class Food():
    def __init__(self, food_color, screen_width, screen_height):
        self.food_color = food_color
        self.size_x = 10
        self.size_y = 10
        self.food_position = [random.randrange(1, screen_width/10)*10,
                              random.randrange(1, screen_height/10)*10]

    def show_food(self, play_surface):
        pygame.draw.rect(play_surface, self.food_color, pygame.Rect(self.food_position[0], self.food_position[1],
                                                                    self.size_x, self.size_y))