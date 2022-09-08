import pygame, sys, time
from settings import *
 
 
class Game:
    def __init__(self):
        
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()
 
    def run(self):
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
            # update window
            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)
 
if __name__ == '__main__':
    game = Game()
    game.run()