import pygame
from pygame_widgets.slider import Slider
from game_logic.menu import Menu
from game_logic.tools import load_image
from data import sound_tools


class OptionsMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.title = [("MUSIC", self.GREEN, 20, (65, 30)),
                      ("SOUND", self.GREEN, 20, (65, 70)),
                      ("MARIO", self.YELLOW, 20, (40, 180), 'mario'),
                      ("TERMINATOR", self.YELLOW, 20, (175, 180), 'terminator'),
                      ("CAT", self.YELLOW, 20, (400, 180), 'cat'),
                      ("CREDITS", self.GREEN, 20, (190, 330)),
                      ("NIKITA SELEZNEV", self.YELLOW, 20, (130, 450)),
                      ("KIRILL SOLOVEV", self.YELLOW, 20, (140, 500)),
                      ("ARTYOM ANDRIUKHIN", self.YELLOW, 20, (100, 550)),
                      ("ZAMKADISHI", self.PINK, 10, (170, 730)),
                      ("tm", self.GREEN, 10, (265, 730))]

        self.buttons = [("MARIO", self.YELLOW, 20, (40, 180, 87, 25), 'mario'),
                        ("TERMINATOR", self.YELLOW, 20, (175, 180, 174, 25), 'terminator'),
                        ("CAT", self.YELLOW, 20, (400, 180, 50, 25), 'cat')]

        self.back = load_image('strela_neon.png', data_path='#source/tmp/')
        self.back = pygame.transform.scale(self.back, (50, 50))

        self.music_slider = Slider(screen, 180, 35, 250, 10, colour=self.PINK,
                                   handleColour=self.YELLOW, handleRadius=10)
        self.sound_slider = Slider(screen, 180, 75, 250, 10, colour=self.PINK,
                                   handleColour=self.YELLOW, handleRadius=10)

        self.music_slider.hide()
        self.sound_slider.hide()

    def render_title(self):
        super().render_title()
        self.screen.blit(self.back, (20, 700))
        self.music_slider.show()
        self.sound_slider.show()
        for i in self.buttons:
            x, y, w, h = i[3]
            pygame.draw.rect(self.screen, self.PINK, (x - 15, y - 15, w + 30, h + 30), 5)
        pygame.mixer.music.set_volume(self.music_slider.getValue() / 100)
        sound_tools.set_volume(self.sound_slider.getValue())

    def get_click(self, mouse_pos):
        x, y = mouse_pos
        if 20 <= x <= 70 and 700 <= y <= 750:
            self.music_slider.hide()
            self.sound_slider.hide()
            sound_tools.click.play()
            return 'main'
        if super().get_click(mouse_pos):
            pygame.mixer.music.load(f'data/music/{super().get_click(mouse_pos)}.mp3')
            pygame.mixer.music.play(-1)

    def get_volume(self):
        return self.sound_slider.getValue() / 100
