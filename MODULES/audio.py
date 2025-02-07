import pygame
from MODULES.init import CONFIG

class Audio_Player:
    def __init__(self):
        pygame.mixer.init()
        self.running = True

    def load_music(self, music_file):
        print("Loading audio")
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(0.3)
    
    def play_music(self):
        print("Running audio")
        pygame.mixer.music.play(-1)             
    
    def pause_music(self):
        print("Pausing audio")
        pygame.mixer.music.pause()
    
    def unpause_music(self):
        print("Unpausing audio")
        pygame.mixer.music.unpause()
    
    def stop_music(self):
        print("Pausing audio")
        pygame.mixer.music.stop()

    def run(self, path=CONFIG["dirs"]["main_theme"]):
        print("Running audio")
        self.load_music(path)
        self.play_music()