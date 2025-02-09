import pygame
from MODULES.init import CONFIG
from MODULES.RENDER.main import MainGameLoop
from MODULES.BEST_RESULTS.best_results import ScoreTable
from MODULES.START_SCREEN.start_screen import StartScreen
from MODULES.audio import AudioPlayer

size = (CONFIG["pygame"]["width"], CONFIG["pygame"]["height"])
f_size = (CONFIG["pygame"]["f_width"], CONFIG["pygame"]["f_height"])

if __name__ == "__main__":
    pygame.init()
    audio = AudioPlayer()

    if CONFIG["pygame"]["fullscreen"] == "Yes":
        scr = pygame.display.set_mode(
            (int(f_size[0]), int(f_size[1])), pygame.FULLSCREEN)
    else:
        scr = pygame.display.set_mode((int(size[0]), int(size[1])))

    size = scr.get_size()

    while True:
        flag = StartScreen(scr, size, audio)

        if flag is None or flag == "quit":
            break

        if flag == "main_game":
            game_flag = MainGameLoop(scr, size, audio)
            if game_flag == "quit":
                break
        elif flag == "best_results":
            flag = ScoreTable().run()
            if flag == 'quit':
                break

    audio.stop_music()
    pygame.quit()
