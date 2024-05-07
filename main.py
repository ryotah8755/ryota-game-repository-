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
message = "type the number or a letter to chose your character!"
rule = "1:Pikachu 2:Charzard"
rule_2 = "A:Pikachu B:Charzard"
ready = "Press SPACE when ready!"
r = 50
g = 0
b = 100

display_start_message = my_font.render(start_message, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
display_rule = my_font.render(rule, True, (255, 255, 255))
ready_display = my_font.render(ready, True, (255, 255, 255))


p = Pikachu (800,60)
c = Charzard (800,600)
p2 = Pikachu (800,60)
c2 = Charzard (800,60)
player_1_character = 0
player_2_character = 0

character_selection = True
battle_ready_mode = False

player_1_pikachu = False
player_1_charzard = False
player_2_pikachu = False
player_2_charzard = False

player_1_turn = False
player_2_turn = False
pregame_player1 = False
pregame_player2 = False
middle_phase = False
game_phase = False
run = True


while run:

    if player_2_character != 0 and player_1_character != 0:
        character_selection = False
        battle_ready_mode = True

    if battle_ready_mode is True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pregame_player1 = False
                    battle_ready_mode = False
                    game_phase = True



    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                player_1_character = 1
                player_1_pikachu = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_2:
                player_1_character = 2
                player_1_charzard = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_3:
                player_1_character = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_4:
                player_1_character = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_2_character = 1
                player_2_pikachu = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_b:
                player_2_character = 2
                player_2_charzard = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                player_2_character = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player_2_character = 4

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    if character_selection is True:
        screen.fill((r, g, b))
        screen.blit(display_start_message, (0, 0))
        screen.blit(display_message, (0, 15))
        screen.blit(display_rule, (0,30))
        screen.blit(c.image, c.rect)
        screen.blit(p.image, p.rect)

    if character_selection is False:
        screen.fill((r, g, b))
        if player_1_charzard is True:
            c = Charzard(100, 600)
            screen.blit(c.image, c.rect)
        if player_1_pikachu is True:
            screen.blit(p.image, p.rect)
            p = Pikachu(100,500)
        if player_2_charzard is True:
            screen.blit(c2.image, c2.rect)
        if player_2_pikachu is True:
            screen.blit(p2.image, p2.rect)

    if battle_ready_mode is True:
        screen.blit(ready_display, (640,480))

    if game_phase is True:
        #enable battle background
        screen.fill((r,g,b))

    #if pregame_player1 is True:
        #

    pygame.display.update()

pygame.quit()