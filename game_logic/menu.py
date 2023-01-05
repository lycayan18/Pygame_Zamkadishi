import pygame
from tools import load_image
from pygame_widgets.slider import Slider


class Menu:
    PINK = (248, 53, 158)
    YELLOW = (255, 255, 0)
    GREEN = (15, 239, 145)
    FONT = 'fff-forward.regular.ttf'
    ALP = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, screen):
        self.screen = screen
        self.title = []
        self.buttons = []

    def render_title(self):
        for i in self.title:
            title = i[0]
            color = i[1]
            size_font = i[2]
            x, y = i[3]
            title_label = pygame.font.Font(self.FONT, size_font)
            label = title_label.render(title, False, color)
            self.screen.blit(label, (x, y))

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.get_click(event.pos)

    def get_move(self, mouse_pos):
        pos_x, pos_y = mouse_pos
        for i in self.buttons:
            x, y, w, h = i[3]
            if x <= pos_x <= x + w and y <= pos_y <= y + h:
                title = i[0]
                color = i[1]
                size_font = i[2]
                title_label = pygame.font.Font(self.FONT, size_font)
                label = title_label.render(title, False, color)
                self.screen.blit(label, (x, y))

    def get_click(self, mouse_pos):
        pos_x, pos_y = mouse_pos
        for i in self.buttons:
            x, y, w, h = i[3]
            if x <= pos_x <= x + w and y <= pos_y <= y + h:
                if i[4]:
                    return i[4]
                print(i[0])


class StartMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = ''
        self.title = [(self.name, self.YELLOW, 20, (100, 400)),
                      ('ENTER NAME', self.GREEN, 30, (120, 300)),
                      ("PLAY", self.YELLOW, 20, (210, 600))]
        self.buttons = [("PLAY", self.PINK, 20, (210, 600, 67, 25), 'main')]

    def event_handler(self, event):
        res = super().event_handler(event)
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

        self.buttons = [("PLAY", self.PINK, 20, (210, 300, 67, 25), None),
                        ("STATISTICS", self.PINK, 20, (170, 350, 157, 25), None),
                        ("OPTIONS", self.PINK, 20, (190, 400, 113, 25), 'option')]


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

    def get_click(self, mouse_pos):
        x, y = mouse_pos
        if 20 <= x <= 70 and 700 <= y <= 750:
            self.music_slider.hide()
            self.sound_slider.hide()
            return 'main'
        if super().get_click(mouse_pos):
            pygame.mixer.music.load(f'music/{super().get_click(mouse_pos)}.mp3')
            pygame.mixer.music.play(-1)

    def get_volume(self):
        return self.sound_slider.getValue() / 100
