import pygame

pygame.init()
click = pygame.mixer.Sound('data/music/click.mp3')
point = pygame.mixer.Sound('data/music/point.mp3')
lose = pygame.mixer.Sound('data/music/lose.wav')
win = pygame.mixer.Sound('data/music/win.mp3')

all_sounds = [click, point, lose, win]

for i in all_sounds:
    i.set_volume(0.5)


def set_volume(val):
    for sound in all_sounds:
        sound.set_volume(val / 100)
