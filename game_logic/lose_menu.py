import pygame
from game_logic.menu import Menu


class LoseMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.title = [('YOU LOSE', self.GREEN, 40, (120, 297)),
                      ('RESTART', self.YELLOW, 20, (178, 383)),
                      ('RETURN TO MENU', self.YELLOW, 20, (128, 442)),
                      ("ZAMKADISHI", self.PINK, 10, (189, 730)),
                      ("tm", self.GREEN, 10, (284, 730))
                      ]

        self.buttons = [('RESTART', self.PINK, 20, (178, 383, 95, 28), 'game'),
                        ('RETURN TO MENU', self.PINK, 20, (128, 442, 193, 28), 'main')]

    def render_title(self):
        super().render_title()
        pygame.draw.line(self.screen, self.PINK, (41, 189), (41, 189 + 390), 15)
        pygame.draw.line(self.screen, self.PINK, (41 - 7, 181), (41 + 400, 181), 15)
        pygame.draw.line(self.screen, self.PINK, (41 + 405, 174), (41 + 405, 181 + 400), 15)
        pygame.draw.line(self.screen, self.PINK, (34, 186 + 400), (34 + 419, 186 + 400), 15)
