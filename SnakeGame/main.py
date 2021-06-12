import pygame
import sys
from Class_Game import Game
from Snake import Snake
from Food import Food
from SuperFood import SuperFood

pygame.font.init()
game = Game()


def start():
    # <Саша
    super = SuperFood(game.colours["Green"], game.width, game.height)
    # Саша/>
    game.total_score = 0
    game.is_over = False
    snake = Snake(game.random_color())
    food = Food(game.random_color(), game.width, game.height)
    game.draw_bg()
    while True:
        while game.paused:
            # <Саша
            pause_font = pygame.font.SysFont("comicsansms", 115)
            pause_surf = pause_font.render("Paused", True, game.colours["Grey"])
            pause_rect = pause_surf.get_rect()
            pause_rect.center = ((game.width / 2), (game.height / 2))
            game.bg.blit(pause_surf, pause_rect)
            pygame.display.update()
            # Саша/>
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
        # <Саша
        if game.total_score % 5 == 0 and game.total_score != 0:
            super.super_position(game.bg)
            game.total_score, super.supfood_position = snake.super_snake_mech(game.total_score, super.supfood_position,
                                                                              game.width, game.height)
        # Саша/>
        game.score(55, 5, 25)
        game.screen_refresh()
        if game.is_over:
            break


# <Саша
def main_menu():
    game.draw_bg()
    run = True
    while run:
        game.bg.fill((0, 0, 0))
        start_font = pygame.font.SysFont("arial", 60)
        start_surf = start_font.render("Press F to begin or Q to quit", True, game.colours["Green"])
        start_rect = start_surf.get_rect()
        start_rect.center = ((game.width / 2), (game.height / 2))
        game.bg.blit(start_surf, start_rect)

        pygame.display.update()

        for event_run in pygame.event.get():
            if event_run.type == pygame.KEYDOWN:
                if event_run.key == pygame.K_f:
                    start()
                elif event_run.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event_run.key == pygame.K_r:
                    main_menu()


main_menu()
# Саша/>
