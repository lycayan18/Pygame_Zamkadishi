import pygame
import pygame_widgets
from game_logic.options_menu import OptionsMenu
from game_logic.main_menu import MainMenu
from game_logic.start_menu import StartMenu
from game_logic.lose_menu import LoseMenu


def main():
    pygame.init()
    size = width, height = 488, 768
    screen = pygame.display.set_mode(size)
    pygame.mixer.music.load('data/music/mario.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    all_menu = {'start': StartMenu(screen), 'main': MainMenu(screen),
                'stat': None, 'option': OptionsMenu(screen), 'lose': LoseMenu(screen)}
    board = all_menu['start']

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            result = board.event_handler(event)
            if result:
                board = all_menu[result]
                name = all_menu['start'].get_name().upper()
                all_menu['main'].title[0][0] = name
                all_menu['main'].title[0][3][0] = 244 - len(name) // 2 * 9

        screen.fill((0, 0, 0))
        board.render_title()
        board.get_move(pygame.mouse.get_pos())
        pygame_widgets.update(events)
        pygame.display.flip()


if __name__ == "__main__":
    main()
