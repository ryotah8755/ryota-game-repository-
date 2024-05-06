import pygame
from pikachu import Pikachu
from charzard import Charzard

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 960
SCREEN_WIDTH = 1280
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

start_message = "Chose your character!"
message = "type the number to chose!"
r = 50
g = 0
b = 100

display_start_message = my_font.render(start_message, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))


p = Pikachu (800,60)
c = Charzard (800,600)



run = True


while run:






    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                player_1_character = 1
                print("yay")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_2:
                player_1_character = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_3:
                player_1_character = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_4:
                player_1_character = 4

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((r, g, b))
    screen.blit(display_start_message, (0, 0))
    screen.blit(display_message, (0, 15))
    screen.blit(c.image, c.rect)
    screen.blit(p.image, p.rect)
    pygame.display.update()

pygame.quit()