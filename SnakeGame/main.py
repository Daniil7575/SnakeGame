import pygame
from Class_Game import Game
from Snake import Snake
from Food import Food


pygame.font.init()
game = Game()
snake = Snake(game.col[3])
food = Food(game.col[2], game.weight, game.height)

game.draw_bg()

while True:
    snake.change_direction = game.click_listener(snake.change_direction)
    snake.change_direction_and_check()
    snake.change_head_position()
    game.total_score, food.food_position = snake.snake_body_mech(game.total_score, food.food_position,
                                                                 game.weight, game.height)
    snake.show_snake(game.bg, game.col[0])  # изменить bg

    food.show_food(game.bg)
    snake.boundary_check(game.game_over, game.weight, game.height)

    game.score()
    game.screen_refresh()
