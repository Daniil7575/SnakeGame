import time

import pygame
import sys


class Game:
    def __init__(self):
        self.total_score = 0
        self.weight = 800
        self.height = 600
        self.fps = pygame.time.Clock()
        self.col = [pygame.Color(0, 0, 0), pygame.Color(255, 0, 0), pygame.Color(0, 255, 0), pygame.Color(0, 0, 255)]
        self.paused = False

    def init_and_check_for_errors(self):
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')

    def pause(self):
        self.paused = not self.paused

    def draw_bg(self):
        self.bg = pygame.display.set_mode((self.weight, self.height))

    def click_listener(self, direction):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction = "UP"

                elif event.key == pygame.K_a:
                    direction = "LEFT"

                elif event.key == pygame.K_s:
                    direction = "DOWN"

                elif event.key == pygame.K_d:
                    direction = "RIGHT"

                elif event.key == pygame.K_p:
                    self.pause()

        return direction

    def screen_refresh(self):
        pygame.display.flip()
        self.fps.tick(30)

    def score(self):
        font = pygame.font.SysFont('monaco', 24)
        surf = font.render(f'Score: {self.total_score}', True, self.col[1])
        s_rect = surf.get_rect()
        s_rect.midtop = (80, 10)
        self.bg.blit(surf, s_rect)

    def exit(self):
        pygame.quit()
        sys.exit()

    def game_over(self):
        go_font = pygame.font.SysFont('monaco ', 72)
        go_surf = go_font.render('Game over', True, self.col[1])
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.bg.blit(go_surf, go_rect)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()