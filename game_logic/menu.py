import pygame
from game_logic import sound_tools


class Menu:
    PINK = (248, 53, 158)
    YELLOW = (255, 255, 0)
    GREEN = (15, 239, 145)
    FONT = 'data/fff-forward.regular.ttf'
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
        if event:
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
                sound_tools.click.play()
                if i[4]:
                    return i[4]
                print(i[0])
