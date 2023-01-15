import pygame
from pygame_widgets.slider import Slider
from random import randint

from game_logic import sound_tools
from game_logic.tools import load_image, ImageSprite
from game_logic.menu import Menu
from game_logic.lose_menu import LoseMenu

from db.requests import games_data, add_user, add_game, total_record


class Game(Menu):
    def __init__(self, screen, session):
        super().__init__(screen, session)
        self.session = session

        self.name = ''
        self.max_apples, self.total_apples, self.first_total = 0, 0, 0

        self.title = [
            ('time:', self.PINK, 20, (50, 120)),
            ('0:0:0', self.YELLOW, 20, (130, 120)),
            ('x', self.PINK, 20, (101, 60)),
            ('0', self.YELLOW, 20, (132 - len('0') * 20 // 3.6, 60)),

            ('x', self.PINK, 20, (109, 630)),
            ('0', self.YELLOW, 20, (140 - len(str('0')) * 20 // 3.6, 630)),
            ('averange', self.PINK, 20, (165, 630)),
            ('0', self.YELLOW, 20, (315 - len(str('0')) * 20 // 3.6, 630)),
            ('max', self.PINK, 20, (335, 630)),
            ("ZAMKADISHI", self.PINK, 10, (189, 730)),
            ("tm", self.GREEN, 10, (284, 730))
        ]
        self.buttons = []
        self.points = 0
        self.count = 1
        self.snake = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]
        self.snake_x, self.snake_y = 0, 1
        self.apple_x, self.apple_y = 10, 10

        self.group = pygame.sprite.Group()
        apple_image = pygame.transform.scale(load_image('apple_v2.png', data_path='#source/tmp/'), (40, 40))
        apple_sprite1 = ImageSprite(apple_image, (50, 55), self.group)
        apple_sprite2 = ImageSprite(apple_image, (60, 620), self.group)

        self.Clock = pygame.time.Clock()
        self.time = 0

    def draw_rect(self, x, y, color):
        pygame.draw.rect(self.screen, color, (49 + 15 * x, 189 + 15 * y, 15, 15))

    def render_title(self):
        super().render_title()

        self.draw_rect(self.apple_x, self.apple_y, self.GREEN)

        pygame.draw.line(self.screen, self.PINK, (41, 189), (41, 189 + 390), 15)
        pygame.draw.line(self.screen, self.PINK, (41 - 7, 181), (41 + 400, 181), 15)
        pygame.draw.line(self.screen, self.PINK, (41 + 405, 174), (41 + 405, 181 + 400), 15)
        pygame.draw.line(self.screen, self.PINK, (34, 186 + 400), (34 + 419, 186 + 400), 15)

        self.update_title()

        super(Game, self).render_title()
        self.group.draw(self.screen)

        for x, y in self.snake:
            self.draw_rect(x, y, self.YELLOW)

        self.Clock.tick()

    def update_title(self):
        hours = self.count // 60 ** 3
        minutes = self.count // 60 ** 2 % 60 if self.count // 60 ** 2 != 0 else 0
        seconds = self.count // 60 if self.count != 0 else 0
        self.title[1] = (f'{hours:02}:{minutes:02}:{seconds:02}', self.YELLOW, 20, (130, 120))
        self.title[3] = (str(self.points), self.YELLOW, 20, (132 - len(str(self.points)) * 20 // 3.6, 60))

        self.title[7] = (str(self.total_apples), self.YELLOW, 20, (140 - len(str(self.total_apples)) * 20 // 3.6, 630))
        self.title[5] = (str(self.max_apples), self.YELLOW, 20, (305 - len(str(self.max_apples)) * 20 // 3.6, 630))

    def event_handler(self, event):
        self.count += 1
        # if event and event.type == pygame.MOUSEBUTTONDOWN:
        #     if self.arrow_sprite.collide_point(*event.pos):
        #         self.end_game(exn it=True)
        #         return 'main'

        return self.snake_event()

    def snake_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.snake_x != 1:
            self.snake_x = -1
            self.snake_y = 0
        elif keys[pygame.K_RIGHT] and self.snake_x != -1:
            self.snake_x = 1
            self.snake_y = 0
        elif keys[pygame.K_DOWN] and self.snake_y != -1:
            self.snake_x = 0
            self.snake_y = 1
        elif keys[pygame.K_UP] and self.snake_y != 1:
            self.snake_x = 0
            self.snake_y = -1

        if self.count % (60 // ((self.points * 0.5) + 5)) == 0:
            self.snake.append((self.snake[-1][0] + self.snake_x, self.snake[-1][1] + self.snake_y))
            del self.snake[0]
            self.apple_event()

    def apple_event(self):
        if self.snake[-1][0] == self.apple_x and self.snake[-1][1] == self.apple_y:
            self.points += 1
            if self.points > self.max_apples:
                self.max_apples += 1
            if self.points == self.first_max + 1:
                sound_tools.win.play()
            else:
                sound_tools.point.play()
            self.snake = [(self.snake[0][0], self.snake[0][1])] + self.snake

            new_apple_x, new_apple_y = randint(0, 25), randint(0, 25)
            while (new_apple_x, new_apple_y) in self.snake:
                new_apple_x, new_apple_y = randint(0, 25), randint(0, 25)

            self.apple_x, self.apple_y = new_apple_x, new_apple_y

    def death_event(self):
        head_x, head_y = self.snake[-1]
        if head_x < 0 or head_x > 25 or head_y < 0 or head_y > 25:
            return True

        for i in self.snake[:-1]:
            if i == (head_x, head_y):
                return True

    def set_name(self, name):
        if name:
            self.name = name
        else:
            self.name = 'NONAME'
        add_user(self.session, self.name)
        if not self.first_total:
            self.max_apples, self.total_apples = total_record(self.session, name)
            self.total_apples = int(self.total_apples)
            self.first_max = self.max_apples

    def end_game(self):
        self.__init__(self.screen, self.session)
