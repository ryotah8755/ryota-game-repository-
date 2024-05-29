import pygame
from pikachu import Pikachu
from charzard import Charzard
from gengar import Gengar
from mewtwo import Mewtwo
import random

# def draw_health_bar(health,x,y):
#     font = pygame.font.SysFont('arial', 25)
#     text = font.render(f'(health) HP: (health)', True, (0, 0, 0))
#     screen.blit(text, (x, y))

pygame.init()
pygame.font.init()
# my_font = pygame.font.SysFont('Arial', 20)
my_font = pygame.font.Font("fonts/PixeloidMono-d94EV.ttf", 16)
pygame.mixer.init()
pygame.mixer.music.load("Pokémon Red, Blue and Yellow - Battle! Trainer Red Music [4bit].mp3")
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 960
SCREEN_WIDTH = 1280
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

start_message = "Chose your character!"
message = "type the number or a letter to chose your character!"
rule = "1:Pikachu 2:Charzard 3:Gengar 4:Mewtwo"
rule_2 = "7:Pikachu 8:Charzard 9:Gengar 0:Mewtwo"
ready = "Press SPACE when ready!"
pregame_prompt = "PRESS SPACE TO GET READY FOR ATTACK PHASE!"
help_message = "press ESC to see what each characters are!"
help_character = ""
player_1_message = "Player 1, it is your turn! Press 1,2,3,4 to attack! Press ESC to see the description of each attack."
player_2_message = "Player 2, it is your turn! Press 7,8,9,0 to attack! Press ESC to see the description of each attack."
player_1_pick = ""
player_2_pick = ""


r = 50
g = 0
b = 100

player_1_health = 0
player_2_health = 0

display_start_message = my_font.render(start_message, True, (0, 0, 0))
display_message = my_font.render(message, True, (0, 0, 0))
display_rule = my_font.render(rule, True, (0, 0, 0))
display_rule2 = my_font.render(rule_2, True, (0, 0, 0))
ready_display = my_font.render(ready, True, (0, 0, 0))
display_help = my_font.render(help_message, True, (0,0,0))
display_attackmessage_1 = my_font.render(player_1_message, True, (0,0,0))
display_attackmessage_2 = my_font.render(player_2_message, True, (0,0,0))
display_player_1_health = my_font.render(str(player_1_health), True, (0,0,0))
display_player_2_health = my_font.render(str(player_2_health), True, (0,0,0))
show_pregame_prompt = my_font.render(str(pregame_prompt), True, (0, 0, 0))

p = Pikachu (800,60)
c = Charzard (750,560)
ge = Gengar (100,450)
g2 = Gengar (800,60)
p2 = Pikachu (800,60)
c2 = Charzard (800,60)
m = Mewtwo (100,60)
m2 = Mewtwo (800,60)
bg = pygame.image.load("d4o49yb-f6ce0e46-18c7-4b95-8604-dfc301eb506b.png")
character_selection_bg = pygame.image.load("wallhaven-g8jj5q.png")

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
damage_phase_1 = False
damage_phase_2 = False
help_phase_character = False
pregame_prompt_1 = False
pregame_prompt_2 = False

start_turn_1 = False
start_turn_2 = False

damage_reset_done = False

player_1_attack_done = False
player_2_attack_done = False

game_over = False
player_1_win = False
player_2_win = False

run = True
damage = 0

a = False

while run:

    while True:
        if not a:
            pygame.mixer.music.play()
        a = True
        break


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
           if event.key == pygame.K_ESCAPE:
                help_phase_character = True
                print("HELP")


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
            if event.key == pygame.K_7:
                if character_selection is True:
                    player_2_character = 1
                    player_2_pikachu = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_8:
                if character_selection is True:
                    player_2_character = 2
                    player_2_charzard = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_9:
                if character_selection is True:
                    player_2_character = 3
                    player_2_gengar = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_0:
                if character_selection is True:
                    player_2_character = 4
                    player_2_mewtwo = True




    if character_selection is True:
        screen.blit(character_selection_bg , (0,0))
        screen.blit(display_start_message, (2, 0))
        screen.blit(display_message, (2, 15))
        screen.blit(display_rule, (2,30))
        screen.blit(display_rule2 , (2,45))
        screen.blit(display_help, (2,60))
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
        if player_1_mewtwo is True:
            screen.blit(m.image, m.rect)
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
            player_1_health = c.hp
        if player_1_pikachu is True:
            screen.blit(p.image, p.rect)
            p = Pikachu(100, 500)
            player_1_health = p.hp
        if player_1_gengar is True:
            ge = Gengar(100, 500)
            player_1_health = ge.hp
            screen.blit(ge.image, ge.rect)
        if player_1_mewtwo is True:
            screen.blit(m.image, m.rect)
            player_1_health = m.hp
        if player_2_charzard is True:
            screen.blit(c2.image, c2.rect)
            player_2_health = c2.hp
        if player_2_pikachu is True:
            screen.blit(p2.image, p2.rect)
            player_2_health = p2.hp
        if player_2_gengar is True:
            screen.blit(g2.image, g2.rect)
            player_2_health = g2.hp
        if player_2_mewtwo is True:
            screen.blit(m2.image, m2.rect)
            player_2_health = m2.hp
        player_1_turn = True
        if player_1_turn is True:
            pregame_player1 = True

        # player_2_turn = True
        # if player_2_turn is True:
        #     pregame_player2 = True

    if pregame_player1 is True:
        screen.blit(show_pregame_prompt, (400,400))
        if battle_ready_mode is True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        start_turn_1 = True
        if start_turn_1 is True:
            if damage_reset_done is False:
                damage = 0
                print("damage has been reset")
                damage_reset_done = True
            screen.blit(display_attackmessage_1, (100,450))
            display_player_1_health = my_font.render(str(player_1_health), True, (0, 0, 0))
            screen.blit(display_player_1_health, (5,800))
            screen.blit(display_attackmessage_2, (100, 450))
            display_player_2_health = my_font.render(str(player_2_health), True, (0, 0, 0))
            screen.blit(display_player_2_health, (300, 300))
            # print(str(player_2_health))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    if player_1_attack_done is False:
                        if player_1_character == 1:
                            damage = p.attack("Thunderbolt")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 2:
                            damage = c.attack("Dragon Claw")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 3:
                            damage = ge.attack("Shadow Ball")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 4:
                            damage = m.attack("Psycho Cut")
                            print(str(damage))
                            player_1_attack_done = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_2:
                    if player_1_attack_done is False:
                        if player_1_character == 1:
                            damage = p.attack("Quick Attack")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 2:
                            damage = c.attack("Slash")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 3:
                            damage = ge.attack("Night Shade")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 4:
                            damage = m.attack("Confusion")
                            print(str(damage))
                            player_1_attack_done = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_3:
                    if player_1_attack_done is False:
                        if player_1_character == 1:
                            damage = p.attack("Iron Tail")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 2:
                            damage = c.attack("Inferno")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 3:
                            damage = ge.attack("Dream Eater")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 4:
                            damage = m.attack("Focus Blast")
                            print(str(damage))
                            player_1_attack_done = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_4:
                    if player_1_attack_done is False:
                        if player_1_character == 1:
                            damage = p.attack("Electro Ball")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 2:
                            damage = c.attack("Overheat")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 3:
                            damage = ge.attack("Dark Pulse")
                            print(str(damage))
                            player_1_attack_done = True
                        if player_1_character == 4:
                            damage = m.attack("Psystrike")
                            print(str(damage))
                            player_1_attack_done = True

            if player_1_attack_done is True:
                if damage_phase_1 is False:
                    if player_2_character == 1:

                        p2.hp = p2.take_damage(damage)
                        print(str("player 2 health remain" + str(p2.hp)))
                        pregame_player1 = False
                        print(str("player 1 dealt " + str(damage)))
                        damage_phase_1 = True
                        pregame_player2 = True
                        print("player 2 turn ")
                        start_turn_1 = False



    if pregame_player2 is True:
        screen.blit(show_pregame_prompt, (400, 400))
    if battle_ready_mode is True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    start_turn_2 = True
            if start_turn_2 is True:
                if damage_reset_done is False:
                    damage = 0
                    print("damage has been reset")
                    damage_reset_done = True

        screen.blit(display_attackmessage_1, (100,450))
        display_player_1_health = my_font.render(str(player_1_health), True, (0, 0, 0))
        screen.blit(display_player_1_health, (5,800))
        screen.blit(display_attackmessage_2, (100, 450))
        display_player_2_health = my_font.render(str(player_2_health), True, (0, 0, 0))
        screen.blit(display_player_2_health, (300, 300))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                if player_2_attack_done is False:
                    if player_2_character == 1:
                        damage = p.attack("Thunderbolt")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 2:
                        damage = c.attack("Dragon Claw")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 3:
                        damage = ge.attack("Shadow Ball")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 4:
                        damage = m.attack("Psycho Cut")
                        print(str(damage))
                        player_2_attack_done = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_2:
                if player_2_attack_done is False:
                    if player_2_character == 1:
                        damage = p.attack("Quick Attack")
                        print(str(damage))
                        player_1_attack_done = True
                    if player_2_character == 2:
                        damage = c.attack("Slash")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 3:
                        damage = ge.attack("Night Shade")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 4:
                        damage = m.attack("Confusion")
                        print(str(damage))
                        player_2_attack_done = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_3:
                if player_2_attack_done is False:
                    if player_2_character == 1:
                        damage = p.attack("Iron Tail")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 2:
                        damage = c.attack("Inferno")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 3:
                        damage = ge.attack("Dream Eater")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 4:
                        damage = m.attack("Focus Blast")
                        print(str(damage))
                        player_2_attack_done = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_4:
                if player_2_attack_done is False:
                    if player_2_character == 1:
                        damage = p.attack("Electro Ball")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 2:
                        damage = c.attack("Overheat")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 3:
                        damage = ge.attack("Dark Pulse")
                        print(str(damage))
                        player_2_attack_done = True
                    if player_2_character == 4:
                        damage = m.attack("Psystrike")
                        print(str(damage))
                        player_2_attack_done = True

        if player_2_attack_done is True:
            if damage_phase_2 is False:
                if player_1_character == 1:

                    p.hp = p.take_damage(damage)
                    print(str("player 1 has remaing " + str(p.hp)))
                    pregame_player2 = False
                    print(str("player 2 has dealt " + str(damage)))
                    damage_phase_2 = True
                    pregame_player_1 = True
                    print("player 1 turn starts")
                    start_turn_2 = False



        screen.blit(display_attackmessage_1, (100, 450))
        display_player_1_health = my_font.render(str(player_1_health), True, (0, 0, 0))
        screen.blit(display_player_1_health, (5, 800))
        screen.blit(display_attackmessage_2, (100, 450))
        display_player_2_health = my_font.render(str(player_2_health), True, (0, 0, 0))
        screen.blit(display_player_2_health, (300, 300))



    pygame.display.update()

pygame.quit()

