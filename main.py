import pygame
from pikachu import Pikachu
from charzard import Charzard
from gengar import Gengar
from mewtwo import Mewtwo

pygame.init()
pygame.font.init()
# my_font = pygame.font.SysFont('Arial', 20)
my_font = pygame.font.Font("fonts/PixeloidMono-d94EV.ttf", 16)

pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 960
SCREEN_WIDTH = 1280
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

start_message = "Chose your character!"
message = "type the number or a letter to chose your character!"
rule = "1:Pikachu 2:Charzard 3:Gengar 4:Mewtwo"
rule_2 = "A:Pikachu B:Charzard C:Gengar D:Mewtwo"
ready = "Press SPACE when ready!"
player_1_message = "Player 1, it is your turn! Press 1,2,3,4 to attack! Press ESC to see the description of each attack."
player_2_message = "Player 2, it is your turn! Press A,B,C,D to attack! Press ESC to see the description of each attack."
player_1_pick = ""
player_2_pick = ""


r = 50
g = 0
b = 100

display_start_message = my_font.render(start_message, True, (0, 0, 0))
display_message = my_font.render(message, True, (0, 0, 0))
display_rule = my_font.render(rule, True, (0, 0, 0))
display_rule2 = my_font.render(rule_2, True, (0, 0, 0))
ready_display = my_font.render(ready, True, (0, 0, 0))
display_attackmessage_1 = my_font.render(player_1_message, True, (0,0,0))
display_attackmessage_2 = my_font.render(player_2_message, True, (0,0,0))

p = Pikachu (800,60)
c = Charzard (800,600)
ge = Gengar (400,400)
g2 = Gengar (400,400)
p2 = Pikachu (800,60)
c2 = Charzard (800,60)
m = Mewtwo (100,200)
m2 = Mewtwo (100,200)
bg = pygame.image.load("d4o49yb-f6ce0e46-18c7-4b95-8604-dfc301eb506b.png")

player_1_character = 0
player_2_character = 0

character_selection = True
battle_ready_mode = False

player_1_pikachu = False
player_1_charzard = False
player_2_pikachu = False
player_2_charzard = False
player_1_gengar = False
player_2_gengar = False
player_1_mewtwo = False
player_2_mewtwo = False

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

    # if player_1_character == 1:
    #     player_1_pick = ""

    if battle_ready_mode is True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pregame_player1 = False
                    battle_ready_mode = False
                    game_phase = True



    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                if character_selection is True:
                    player_1_character = 1
                    player_1_pikachu = True
                    print("yay")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_2:
                if character_selection is True:
                    player_1_character = 2
                    player_1_charzard = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_3:
                if character_selection is True:
                    player_1_character = 3
                    player_1_gengar = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_4:
                if character_selection is True:
                    player_1_character = 4
                    player_1_mewtwo = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                if character_selection is True:
                    player_2_character = 1
                    player_2_pikachu = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_b:
                if character_selection is True:
                    player_2_character = 2
                    player_2_charzard = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                if character_selection is True:
                    player_2_character = 3
                    player_2_gengar = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                if character_selection is True:
                    player_2_character = 4
                    player_2_mewtwo = True




    if character_selection is True:
        screen.blit(bg , (0,0))
        screen.blit(display_start_message, (0, 0))
        screen.blit(display_message, (0, 15))
        screen.blit(display_rule, (0,30))
        screen.blit(display_rule2 , (0,45))
        screen.blit(c.image, c.rect)
        screen.blit(p.image, p.rect)
        screen.blit(ge.image, ge.rect)
        screen.blit(m.image, m.rect)

    if character_selection is False:
        screen.blit(bg, (0,0))
        if player_1_charzard is True:
            c = Charzard(100, 600)
            screen.blit(c.image, c.rect)
        if player_1_pikachu is True:
            screen.blit(p.image, p.rect)
            p = Pikachu(100,500)
        if player_1_gengar is True:
            ge = Gengar(100,500)
            screen.blit(ge.image, ge.rect)
        if player_2_charzard is True:
            screen.blit(c2.image, c2.rect)
        if player_2_pikachu is True:
            screen.blit(p2.image, p2.rect)

    if battle_ready_mode is True:
        screen.blit(ready_display, (640,480))

    if game_phase is True:
        #enable battle background
        screen.blit(bg, (0,0))
        if player_1_charzard is True:
            c = Charzard(100, 600)
            screen.blit(c.image, c.rect)
        if player_1_pikachu is True:
            screen.blit(p.image, p.rect)
            p = Pikachu(100, 500)
        if player_1_gengar is True:
            ge = Gengar(100, 500)
            screen.blit(ge.image, ge.rect)
        if player_1_mewtwo is True:
            screen.blit(m.image, m.rect)
        if player_2_charzard is True:
            screen.blit(c2.image, c2.rect)
        if player_2_pikachu is True:
            screen.blit(p2.image, p2.rect)
        if player_2_gengar is True:
            screen.blit(g2.image, g2.rect)
        if player_2_mewtwo is True:
            screen.blit(m2.image, m2.rect)
        player_1_turn = True
        if player_1_turn is True:
            pregame_player1 = True

        # player_2_turn = True
        # if player_2_turn is True:
        #     pregame_player2 = True

    if pregame_player1 is True:

        screen.blit(display_attackmessage_1, (300,300))


    if pregame_player2 is True:

        screen.blit(display_attackmessage_2, (300, 300))





    pygame.display.update()

pygame.quit()