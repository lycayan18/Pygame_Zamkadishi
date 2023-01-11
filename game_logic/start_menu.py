import pygame
from game_logic.menu import Menu


class StartMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = ''
        self.title = [(self.name, self.YELLOW, 20, (100, 400)),
                      ('ENTER NAME', self.GREEN, 30, (120, 300)),
                      ("PLAY", self.YELLOW, 20, (210, 600)),
                      ("ZAMKADISHI", self.PINK, 10, (189, 730)),
                      ("tm", self.GREEN, 10, (284, 730))
                      ]
        self.buttons = [("PLAY", self.PINK, 20, (210, 600, 67, 25), 'main')]

    def event_handler(self, event):
        res = super().event_handler(event)
        if event:
            if event.type == pygame.KEYDOWN:
                self.title[0] = (self.do_name(event), self.YELLOW, 20, (100, 400))
        return res

    def do_name(self, event):
        if event.unicode in self.ALP:
            self.name += event.unicode
        if self.name and event.key == 8 or len(self.name) > 18:
            self.name = self.name[:-1]
        return self.name

    def get_name(self):
        return self.name
