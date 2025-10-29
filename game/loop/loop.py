import pygame
from ui.screen import Screen
#Création de la loop du jeu
class Game :
    def __init__(self):
        self.running = True
        self.screen = Screen()


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.update()
