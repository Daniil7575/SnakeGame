import pygame
import random


class Game:
    def __init__(self):
        self.total_score = 0
        self.width = 800
        self.height = 600
        self.fps = pygame.time.Clock()
        self.colours = {"Black": pygame.Color(0, 0, 0), "White": pygame.Color(255, 255, 255),
                        "Red": pygame.Color(255, 0, 0), "Green": pygame.Color(0, 255, 0),
                        "Blue": pygame.Color(0, 0, 255), "Yellow": pygame.Color(255, 255, 0),
                        "Grey": pygame.Color(100, 100, 100)}
        self.paused = False
        self.is_over = False

    @staticmethod
    def random_color():
        return pygame.Color(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256))

    def pause(self):
        self.paused = not self.paused

    def draw_bg(self):
        self.bg = pygame.display.set_mode((self.width, self.height))

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
                elif event.key == pygame.K_SPACE:
                    self.pause()
                elif event.key == pygame.K_q:
                    self.is_over = True
        return direction

    def __to60(self):
        return 60 if self.total_score + 10 >= 60 else self.total_score + 10

    def screen_refresh(self):
        pygame.display.flip()
        self.fps.tick(self.__to60())

    def score(self, x, y, sp):
        font = pygame.font.SysFont("arial", sp)
        surf = font.render(f"Score: {self.total_score}", True, self.colours["Red"])
        s_rect = surf.get_rect()
        s_rect.midtop = (x, y)
        self.bg.blit(surf, s_rect)

    def game_over(self):
        self.bg.fill((0, 0, 0))
        re_font = pygame.font.SysFont("arial", 40)
        re_surf = re_font.render("Press R to restart or Q to quit", True, self.colours["Red"])
        re_rect = re_surf.get_rect()
        re_rect.midtop = (400, 100)
        self.bg.blit(re_surf, re_rect)
        go_font = pygame.font.SysFont("arial", 72)
        go_surf = go_font.render("Game over", True, self.colours["Red"])
        go_rect = go_surf.get_rect()
        go_rect.midtop = (400, 15)
        self.bg.blit(go_surf, go_rect)
        self.score(400, 150, 40)
        pygame.display.flip()
        self.is_over = True
        while True:
            for end_event in pygame.event.get():
                if end_event.type == pygame.KEYDOWN:
                    return
