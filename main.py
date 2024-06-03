import pygame
from pikachu import Pikachu
from charzard import Charzard
from gengar import Gengar
from mewtwo import Mewtwo

pygame.init()
pygame.font.init()
my_font = pygame.font.Font("fonts/PixeloidMono-d94EV.ttf", 16)
pygame.mixer.init()
pygame.mixer.music.load("Pokémon Red, Blue and Yellow - Battle! Trainer Red Music [4bit].mp3")
p = False
# pygame.display.setCaption("Coin Collector!")

# Set up variables for the display
SCREEN_HEIGHT = 960
SCREEN_WIDTH = 1280
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

character_selection_bg = pygame.image.load( "wallhaven-g8jj5q.png")

start_message = "Chose your character!"
message = "Type the number or a letter to choose your character!"
rule = "1:Pikachu 2:Charzard 3:Gengar 4:Mewtwo"
rule_2 = "7:Pikachu 8:Charzard 9:Gengar 0:Mewtwo"
ready = "Press SPACE when ready!"
pregame_prompt = "PRESS SPACE TO GET READY FOR ATTACK PHASE!"
help_message = "Press ESC to see what each character's attacks are!"
player_1_message = "Player 1, it is your turn! Press 1,2,3,4 to attack! Press ESC to see the description of each attack."
player_2_message = "Player 2, it is your turn! Press 7,8,9,0 to attack! Press ESC to see the description of each attack."
miss_message = "THE ATTACK MISSED, IT DEALT 0 DAMAGE!"

player_1_winning_message = "PLAYER 1 HAS WON!"
player_2_winning_message = "PLAYER 2 HAS WON!"

r = 50
g = 0
b = 100

player_1_health = 100
player_2_health = 100

display_start_message = my_font.render(start_message, True, (0, 0, 0))
display_message = my_font.render(message, True, (0, 0, 0))
display_rule = my_font.render(rule, True, (0, 0, 0))
display_rule2 = my_font.render(rule_2, True, (0, 0, 0))
ready_display = my_font.render(ready, True, (0, 0, 0))
display_help = my_font.render(help_message, True, (0, 0, 0))
display_attackmessage_1 = my_font.render(player_1_message, True, (0, 0, 0))
display_attackmessage_2 = my_font.render(player_2_message, True, (0, 0, 0))
display_player_1_health = my_font.render("HP: " + str(player_1_health), True, (0, 0, 0))
display_player_2_health = my_font.render("HP: " + str(player_2_health), True, (0, 0, 0))
show_pregame_prompt = my_font.render(str(pregame_prompt), True, (0, 0, 0))
display_1_win = my_font.render(player_1_winning_message, True, (0,0,0))
display_2_win = my_font.render(player_2_winning_message, True, (0,0,0))
display_miss = my_font.render(miss_message, True, (0,0,0))


# Initialize Pokemon objects
p = Pikachu(800, 60)
p.image = pygame.transform.flip(p.image, True , False)
c = Charzard(750, 560)
ge = Gengar(100, 450)
m = Mewtwo(100, 60)
p2 = Pikachu(800, 60)
c2 = Charzard(750, 560)
ge2 = Gengar(100, 450)
m2 = Mewtwo(100, 60)
e = False
bg = pygame.image.load("d4o49yb-f6ce0e46-18c7-4b95-8604-dfc301eb506b.png")

# Character selection flags and variables
player_1_character = None
player_2_character = None
player_1_pokemon = None
player_2_pokemon = None

miss = False

character_selection = True
battle_ready_mode = False

player_1_turn = False
player_2_turn = False
game_phase = False

flip = False

player_1_win = False
player_2_win = False

damage = 0

run = True

while run:

    while True:
        if not e:
            pygame.mixer.music.play()
        e = True
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if character_selection:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    player_1_character = 1
                    player_1_pokemon = Pikachu(100, 100)
                    player_1_health = p.hp

                if event.key == pygame.K_2:
                    player_1_character = 2
                    player_1_pokemon = Charzard(100, 100)
                    player_1_health = c.hp
                if event.key == pygame.K_3:
                    player_1_character = 3
                    player_1_pokemon = Gengar(100, 100)
                    player_1_health = ge.hp
                if event.key == pygame.K_4:
                    player_1_character = 4
                    player_1_pokemon = Mewtwo(100, 100)
                    player_1_health = m.hp
                if event.key == pygame.K_7:
                    player_2_character = 1
                    player_2_pokemon = Pikachu(800, 100)
                    player_2_health = p2.hp
                if event.key == pygame.K_8:
                    player_2_character = 2
                    player_2_health = c2.hp
                    player_2_pokemon = Charzard(800, 100)
                if event.key == pygame.K_9:
                    player_2_character = 3
                    player_2_pokemon = Gengar(800, 100)
                    player_2_health = ge2.hp
                if event.key == pygame.K_0:
                    player_2_character = 4
                    player_2_pokemon = Mewtwo(800, 100)
                    player_2_health = m2.hp
                if event.key == pygame.K_SPACE and player_1_character and player_2_character:
                    character_selection = False
                    battle_ready_mode = True


        if battle_ready_mode:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    battle_ready_mode = False
                    game_phase = True
                    player_1_turn = True

        if game_phase:
            if player_1_turn:
                miss = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_1:
                        damage = player_1_pokemon.attack(
                            "Thunderbolt") if player_1_character == 1 else player_1_pokemon.attack(
                            "Dragon Claw") if player_1_character == 2 else player_1_pokemon.attack(
                            "Shadow Ball") if player_1_character == 3 else player_1_pokemon.attack("Psycho Cut")
                        player_1_turn = False
                        player_2_turn = True
                    elif event.key == pygame.K_2:
                        damage = player_1_pokemon.attack(
                            "Quick Attack") if player_1_character == 1 else player_1_pokemon.attack(
                            "Slash") if player_1_character == 2 else player_1_pokemon.attack(
                            "Night Shade") if player_1_character == 3 else player_1_pokemon.attack("Confusion")
                        player_1_turn = False
                        player_2_turn = True
                    elif event.key == pygame.K_3:
                        damage = player_1_pokemon.attack(
                            "Iron Tail") if player_1_character == 1 else player_1_pokemon.attack(
                            "Inferno") if player_1_character == 2 else player_1_pokemon.attack(
                            "Dream Eater") if player_1_character == 3 else player_1_pokemon.attack("Focus Blast")
                        player_1_turn = False
                        player_2_turn = True
                    elif event.key == pygame.K_4:
                        damage = player_1_pokemon.attack(
                            "Electro Ball") if player_1_character == 1 else player_1_pokemon.attack(
                            "Overheat") if player_1_character == 2 else player_1_pokemon.attack(
                            "Dark Pulse") if player_1_character == 3 else player_1_pokemon.attack("Psystrike")
                        player_1_turn = False
                        miss = False
                        player_2_turn = True

                    player_2_health -= damage
                    display_player_2_health = my_font.render("PLAYER 2 HP: " + str(player_2_health), True, (0, 0, 0))
                    display_player_1_health = my_font.render("PLAYER 1 HP: " + str(player_1_health), True, (0, 0, 0))
                    if damage == 0 and player_1_turn is False:
                        miss = True

            elif player_2_turn:
                miss = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_7:
                        damage = player_2_pokemon.attack(
                            "Thunderbolt") if player_2_character == 1 else player_2_pokemon.attack(
                            "Dragon Claw") if player_2_character == 2 else player_2_pokemon.attack(
                            "Shadow Ball") if player_2_character == 3 else player_2_pokemon.attack("Psycho Cut")
                        player_2_turn = False
                        player_1_turn = True
                    elif event.key == pygame.K_8:
                        damage = player_2_pokemon.attack(
                            "Quick Attack") if player_2_character == 1 else player_2_pokemon.attack(
                            "Slash") if player_2_character == 2 else player_2_pokemon.attack(
                            "Night Shade") if player_2_character == 3 else player_2_pokemon.attack("Confusion")
                        player_2_turn = False
                        player_1_turn = True
                    elif event.key == pygame.K_9:
                        damage = player_2_pokemon.attack(
                            "Iron Tail") if player_2_character == 1 else player_2_pokemon.attack(
                            "Inferno") if player_2_character == 2 else player_2_pokemon.attack(
                            "Dream Eater") if player_2_character == 3 else player_2_pokemon.attack("Focus Blast")
                        player_2_turn = False
                        player_1_turn = True
                    elif event.key == pygame.K_0:
                        damage = player_2_pokemon.attack(
                            "Electro Ball") if player_2_character == 1 else player_2_pokemon.attack(
                            "Overheat") if player_2_character == 2 else player_2_pokemon.attack(
                            "Dark Pulse") if player_2_character == 3 else player_2_pokemon.attack("Psystrike")

                        player_2_turn = False
                        miss = False
                        player_1_turn = True

                    player_1_health -= damage
                    display_player_1_health = my_font.render("PLAYER 1 HP: " + str(player_1_health), True, (0, 0, 0))
                    if damage == 0 and player_2_turn is False:
                        miss = True



            if player_1_health <= 0 or player_2_health <= 0:
                game_phase = False
                if player_1_health > player_2_health:
                    player_1_win = True
                if player_2_health > player_1_health:
                    player_2_win = True






    screen.fill((r, g, b))
    screen.blit(bg, (0, 0))
    if miss:
        screen.blit(display_miss, (640,200))

    if character_selection:
        screen.blit(character_selection_bg, (0, 0))
        screen.blit(display_start_message, (2, 0))
        screen.blit(display_message, (2, 15))
        screen.blit(display_rule, (2, 30))
        screen.blit(display_rule2, (2, 45))
        screen.blit(display_help, (2, 60))

    if player_1_pokemon:
        screen.blit(player_1_pokemon.image, (100, 300))

        if flip is False:
            player_1_pokemon.image = pygame.transform.flip(player_1_pokemon.image, True, False)
            flip = True
    if player_2_pokemon:
        screen.blit(player_2_pokemon.image, (800, 300))

    if battle_ready_mode:
        screen.blit(ready_display, (640, 200))

    if game_phase:
        if player_1_turn:
            screen.blit(display_attackmessage_1, (100,200))
        elif player_2_turn:
            screen.blit(display_attackmessage_2, (100, 200))

        screen.blit(display_player_1_health, (300, 300))
        screen.blit(display_player_2_health, (800, 300))


    if player_1_win is True:
        screen.blit(display_1_win, (640,200))
    if player_2_win is True:
        screen.blit(display_2_win, (640,200))


    pygame.display.update()




pygame.quit()



