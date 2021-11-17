import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman


class GameController(object):

    def __init__(self):
        pygame.init()
        self.pacman = Pacman()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()

    def set_background(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def start_game(self):
        self.set_background()

    def update(self):
        delta_t = self.clock.tick(30) / 1000.0
        self.pacman.update(delta_t)
        self.check_events()
        self.render()

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.pacman.render(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    game = GameController()
    game.start_game()
    while True:
        game.update()
