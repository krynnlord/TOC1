import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def play_music(mp3File,vol=.5):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(mp3File)
    channel = pygame.mixer.Channel(0)
    channel.play(sound, -1)
    channel.set_volume(vol)

def music_toggle():
    if pygame.mixer.Channel(0).get_busy():
        pygame.mixer.Channel(0).pause()
    else:
        pygame.mixer.Channel(0).unpause()

def play_midi(midifile,vol):
    pygame.mixer.init(44100,-16,1,1024)
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.load(midifile)
    pygame.mixer.music.play(-1)

def midi_toggle():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def music_lower():
    current_volume = pygame.mixer.music.get_volume()
    new_volume = current_volume - .1
    pygame.mixer.music.set_volume(new_volume)
    
def music_raise():
    current_volume = pygame.mixer.music.get_volume()
    new_volume = current_volume + .1
    pygame.mixer.music.set_volume(new_volume)

def play_sound(mp3File):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(mp3File)
    channel = pygame.mixer.Channel(1)
    channel.set_volume(1)
    channel.play(sound)    