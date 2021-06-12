from Snake import *


class SuperFood():
    def __init__(self, super_color, screen_width, screen_height):
        self.super_color = super_color
        self.size_x = 10
        self.size_y = 10
        self.supfood_position = [random.randrange(1, screen_width / 10) * 10,
                              random.randrange(1, screen_height / 10) * 10]

    def super_position(self, play_surface):
        pygame.draw.rect(play_surface, self.super_color, pygame.Rect(self.supfood_position[0], self.supfood_position[1],
                                                                    self.size_x, self.size_y))