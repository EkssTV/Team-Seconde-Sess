import pygame
from game.loop.loop import Game
#lancement de pygame
pygame.init()
#Lancement du jeu
if __name__ == '__main__':
    game = Game()
    game.run()

