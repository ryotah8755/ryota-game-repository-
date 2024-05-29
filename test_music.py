import pygame

pygame.mixer.init()
pygame.mixer.music.load("Pokémon Red, Blue and Yellow - Battle! Trainer Red Music [4bit].mp3")
p = False

while True:
    if not p:
        pygame.mixer.music.play()
    p = True