import pygame
from pathlib import Path

ROOT = Path(__file__).parent.parent


class ImageSprite(pygame.sprite.Sprite):

    def __init__(self, image, pos, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def move(self, dx, dy):
        self.rect.x = dx
        self.rect.y = dy


def load_image(filename, data_path=None):
    if data_path is None:
        data_path = "data"
    file = ROOT.joinpath(data_path, filename)
    if not file.exists():
        print(f"File {file} does not exist!")
        exit(1)
    return pygame.image.load(file)