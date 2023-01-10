import pygame
from pygame_widgets.slider import Slider
from random import randint

from game_logic.tools import load_image, ImageSprite
from game_logic.menu import Menu
from game_logic.lose_menu import LoseMenu


class Game(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.title = []
        self.buttons = []
        self.points = 0
        self.count = 1
        self.snake = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]
        self.snake_x, self.snake_y = 0, 1
        self.apple_x, self.apple_y = 10, 10

    def draw_rect(self, x, y, color):
        pygame.draw.rect(self.screen, color, (49 + 15 * x, 189 + 15 * y, 15, 15))

    def render_title(self):
        super().render_title()

        self.draw_rect(self.apple_x, self.apple_y, self.GREEN)

        pygame.draw.line(self.screen, self.PINK, (41, 189), (41, 189 + 390), 15)
        pygame.draw.line(self.screen, self.PINK, (41 - 7, 181), (41 + 400, 181), 15)
        pygame.draw.line(self.screen, self.PINK, (41 + 405, 174), (41 + 405, 181 + 400), 15)
        pygame.draw.line(self.screen, self.PINK, (34, 186 + 400), (34 + 419, 186 + 400), 15)

        for x, y in self.snake:
            self.draw_rect(x, y, self.YELLOW)

    def event_handler(self, event):
        self.count += 1
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
            if self.death_event():
                self.title = []
                self.buttons = []
                self.points = 0
                self.count = 1
                self.snake = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]
                self.snake_x, self.snake_y = 0, 1
                self.apple_x, self.apple_y = 10, 10

                return 'lose'

    def apple_event(self):
        if self.snake[-1][0] == self.apple_x and self.snake[-1][1] == self.apple_y:
            self.points += 1
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
