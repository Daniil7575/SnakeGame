import random
import pygame



class Snake():
    def __init__(self, color):
        self.snake_head = [100, 50]  # позиция головы змеи
        self.snake_body = [[100, 50], [90, 50], [80, 50]]  # тело змеи
        self.snake_color = color
        self.direction = "RIGHT"  # изначальное направление движения змеи
        self.change_direction = self.direction

    # изменяется направление движения змеи, если изменяемое положение не противоположно текущему
    def change_direction_and_check(self):
        if any((self.change_direction == "RIGHT" and not self.direction == "LEFT",
                self.change_direction == "LEFT" and not self.direction == "RIGHT",
                self.change_direction == "UP" and not self.direction == "DOWN",
                self.change_direction == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_direction

    def change_head_position(self):  # изменение позиции головы змеи [0] - OX, [1] - OY
        if self.direction == "RIGHT":
            self.snake_head[0] += 10
        if self.direction == "LEFT":
            self.snake_head[0] -= 10
        if self.direction == "UP":
            self.snake_head[1] -= 10
        if self.direction == "DOWN":
            self.snake_head[1] += 10

    def snake_body_mech(self, score, food_position, screen_width, screen_height):
        self.snake_body.insert(0, list(self.snake_head))
        if self.snake_head[0] == food_position[0] and self.snake_head[1] == food_position[1]:
            food_position = [random.randrange(1, screen_width / 10) * 10, random.randrange(1, screen_height / 10) * 10]
            score += 1
        else:
            self.snake_body.pop()
        return score, food_position

    def show_snake(self, play_surface, surface_color):
        play_surface.fill(surface_color)
        for positions in self.snake_body:
            pygame.draw.rect(play_surface, self.snake_color, pygame.Rect(positions[0], positions[1], 10, 10))

    def boundary_check(self, game_over, screen_width, screen_height):
        if any((self.snake_head[0] > screen_width - 10 or self.snake_head[0] < 0,
                self.snake_head[1] > screen_height - 10 or self.snake_head[1] < 0)):
            game_over()
        for block in self.snake_body[1:]:
            if block[0] == self.snake_head[0] and block[1] == self.snake_head[1]:
                game_over()
