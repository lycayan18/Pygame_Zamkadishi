import pygame


class Menu:
    def __init__(self):
        pass

    def set_view(self, screen):
        title_label = pygame.font.Font('fff-forward.regular.ttf', 50)
        label = title_label.render("SNAKE", False, '#0FEF91')
        screen.blit(label, (60, 50))
        label = title_label.render("THE", False, '#FFFF00')
        screen.blit(label, (300, 50))
        label = title_label.render("GAME", False, '#F8359E')
        screen.blit(label, (150, 130))

        title_label = pygame.font.Font('fff-forward.regular.ttf', 20)
        label1 = title_label.render("PLAY", False, '#FFFF00')
        screen.blit(label1, (210, 300))
        label2 = title_label.render("STATISTICS", False, '#FFFF00')
        screen.blit(label2, (170, 350))
        label3 = title_label.render("OPTIONS", False, '#FFFF00')
        screen.blit(label3, (190, 400))
        label4 = title_label.render("NICKNAME", False, '#FFFF00')
        screen.blit(label4, (175, 450))

    def get_move(self, mouse_pos):
        title_label = pygame.font.Font('fff-forward.regular.ttf', 20)
        x, y = mouse_pos
        self.set_view(screen)
        if 210 < x < 280 and 300 < y < 330:
            label1 = title_label.render("PLAY", False, '#F8359E')
            screen.blit(label1, (210, 300))
        if 170 < x < 330 and 350 < y < 380:
            label2 = title_label.render("STATISTICS", False, '#F8359E')
            screen.blit(label2, (170, 350))
        if 190 < x < 310 and 400 < y < 430:
            label3 = title_label.render("OPTIONS", False, '#F8359E')
            screen.blit(label3, (190, 400))

    def get_click(self, mouse_pos):
        x, y = mouse_pos
        if 210 < x < 280 and 300 < y < 330:
            print('Нажата "PLAY"')
        if 170 < x < 330 and 350 < y < 380:
            print('Нажата "STATISTICS"')
        if 190 < x < 310 and 400 < y < 430:
            print('Нажата "OPTIONS"')


if __name__ == '__main__':
    pygame.init()
    size = width, height = 488, 768
    screen = pygame.display.set_mode(size)

    board = Menu()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.set_view(screen)
        board.get_move(pygame.mouse.get_pos())
        pygame.display.flip()
