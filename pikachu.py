import pygame
import random

class Pikachu:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("pikachu_png.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1
        self.name = "Pikachu"
        self.hp = 55
        self.moves = {
            "Thunderbolt": {"damage": 25, "accuracy": 80},
            "Quick Attack": {"damage": 15, "accuracy": 95},
            "Iron Tail": {"damage": 20, "accuracy": 75},
            "Electro Ball": {"damage": 20, "accuracy": 85}
        }

        def attack(self, move):
            if move in self.moves:
                move_info = self.moves[move]
                if random.randint(1, 100) <= move_info["accuracy"]:
                    # attack hit
                    return move_info["damage"]
                else:
                    # missed
                    return 0
            else:
                return 0
                # invalid