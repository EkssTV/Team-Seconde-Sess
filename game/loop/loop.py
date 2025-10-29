import pygame
from ui.screen import Screen
from data.assets.fonts.banner.banner import banner

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
            self.screen.draw_text(banner.shw_banner(), 50, 50,14,(255,255,255))
            self.screen.update()
