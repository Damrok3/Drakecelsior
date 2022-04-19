from turtle import screensize
import pygame,sys
from settings import * #the star makes it to import everything from settings
from debug import debug
from level import Level
from ui import UI

class Game:
    def __init__(self):
        
        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Drakcelsior")

        #ui
        self.ui = UI(self.screen)


        self.coins = 0
        self.level = Level(self.change_coins)

    def change_coins(self, amount):
        self.coins += amount



    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            self.level.run()
            self.ui.show_coins(self.coins)
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()


    #7h one at 2:30:00 weapons