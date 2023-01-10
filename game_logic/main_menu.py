import pygame
from game_logic.menu import Menu


class MainMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.title = [['', self.YELLOW, 10, [175, 650]],
                      ("SNAKE", self.GREEN, 50, (60, 50)),
                      ("THE", self.YELLOW, 50, (300, 50)),
                      ("GAME", self.PINK, 50, (150, 130)),
                      ("PLAY", self.YELLOW, 20, (210, 300)),
                      ("STATISTICS", self.YELLOW, 20, (170, 350)),
                      ("OPTIONS", self.YELLOW, 20, (190, 400)),
                      ("NICKNAME", self.GREEN, 20, (175, 550)),
                      ("ZAMKADISHI", self.PINK, 10, (170, 730)),
                      ("tm", self.GREEN, 10, (265, 730))]

        self.buttons = [("PLAY", self.PINK, 20, (210, 300, 67, 25), 'game'),
                        ("STATISTICS", self.PINK, 20, (170, 350, 157, 25), None),
                        ("OPTIONS", self.PINK, 20, (190, 400, 113, 25), 'option')]
