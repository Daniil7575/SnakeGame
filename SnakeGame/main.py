import pygame
import sys
from Class_Game import Game
from Snake import Snake
from Food import Food


def start():
    pygame.font.init()
    game = Game()
    snake = Snake(game.random_color())
    food = Food(game.random_color(), game.width, game.height)

    game.draw_bg()

    while True:
        while game.paused:
            pause_font = pygame.font.SysFont("comicsansms", 115)
            pause_surf = pause_font.render("Paused", True, game.colours["Grey"])
            pause_rect = pause_surf.get_rect()
            pause_rect.center = ((game.width / 2), (game.height / 2))
            game.bg.blit(pause_surf, pause_rect)

            pygame.display.update()
            for is_pause in pygame.event.get():
                if is_pause.type == pygame.KEYDOWN:
                    if is_pause.key == pygame.K_SPACE:
                        game.pause()

        snake.change_direction = game.click_listener(snake.change_direction)
        snake.change_direction_and_check()
        snake.change_head_position()
        game.total_score, food.food_position = snake.snake_body_mech(game.total_score, food.food_position,
                                                                     game.width, game.height)
        snake.show_snake(game.bg, game.colours["Black"])  # изменить bg

        food.show_food(game.bg)
        snake.boundary_check(game.game_over, game.width, game.height)

        game.score()
        game.screen_refresh()
        if game.is_over:
            break


start()
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                start()

            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
