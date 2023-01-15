import pygame
from game_logic.menu import Menu
from game_logic.tools import load_image
from game_logic import sound_tools

from db.requests import games_data


class Statistick(Menu):
    def __init__(self, screen, session):
        self.session = session
        super().__init__(screen)
        self.title = [('NICKNAME', self.YELLOW, 17, (64, 73)),
                      ('MAX', self.YELLOW, 17, (179 + 44, 59 + 14)),
                      ('AVERAGE', self.YELLOW, 17, (309 + 14, 59 + 14)),
                      ("ZAMKADISHI", self.PINK, 10, (189, 730)),
                      ("tm", self.GREEN, 10, (284, 730))
                      ]

        self.back = load_image('strela_neon.png', data_path='data')
        self.back = pygame.transform.scale(self.back, (50, 50))

    def update(self):
        self.__init__(self.screen, self.session)
        self.res = games_data(self.session)
        if self.res:
            self.res = sorted(self.res, key=lambda x: (-x[1], -x[2]))
            self.max_score = max([i[1] // 1 for i in self.res])
            self.average_score = max([i[2] // 1 for i in self.res])

            for i, elem in enumerate(self.res):
                nickname = elem[0]
                max_sc = int(elem[1])
                ave_sc = int(elem[2])
                color = self.YELLOW
                nickname_size = 17 - (0 if len(nickname) <= 8 else len(nickname) - 8)

                self.title.append(
                    (nickname, color, nickname_size, (120 - len(nickname) * nickname_size // 3.4, 73 + (i + 1) * 55)))
                self.title.append((str(max_sc), self.GREEN if max_sc == self.max_score else color, 17,
                                   (240 - (len(str(max_sc)) * 5), 73 + (i + 1) * 55)))
                self.title.append((str(ave_sc), self.GREEN if ave_sc == self.average_score else color, 17,
                                   (370 - (len(str(ave_sc)) * 5), 73 + (i + 1) * 55)))

    def get_click(self, mouse_pos):
        x, y = mouse_pos
        if 20 <= x <= 70 and 700 <= y <= 750:
            sound_tools.click.play()
            return 'main'
        if super().get_click(mouse_pos):
            pygame.mixer.music.load(f'data/music/{super().get_click(mouse_pos)}.mp3')
            pygame.mixer.music.play(-1)

    def render_title(self):
        self.update()
        super().render_title()
        
        self.screen.blit(self.back, (20, 700))

        pygame.draw.line(self.screen, self.PINK, (46, 55), (46, 606 + 64), 5)
        pygame.draw.line(self.screen, self.PINK, (44, 56), (44 + 390 + 10, 56), 5)
        pygame.draw.line(self.screen, self.PINK, (46 + 390 + 6, 55), (46 + 390 + 6, 606 + 64), 5)
        pygame.draw.line(self.screen, self.PINK, (44, 56 + 606 + 6), (44 + 390 + 10, 56 + 606 + 6), 5)

        pygame.draw.line(self.screen, self.PINK, (44, 56 + 55), (44 + 390 + 10, 56 + 55), 5)
