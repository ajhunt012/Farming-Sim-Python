import pygame, sys
from settings import *

class Game:
    def _init_(selfself):
        pygame.inti()
        self.screen = pygame.display.set.mode((SCREEN_WIDTH,SCREEN_HEIGTH))
        self.clock = pygame.time.Clock()

        def run(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                        dt = self.clock.tick() / 1000
                        pygame.disply.update()

                        if_name_ == '_main_':
                        game = Game()
                        game.run()


