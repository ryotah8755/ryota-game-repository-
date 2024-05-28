import pygame
import random


class Charzard:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("charzard_png.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1
        self.name = "Pikachu"
        self.hp = 100
        self.moves = {
            "Dragon Claw": {"damage": 15, "accuracy": 100},
            "Slash": {"damage": 20, "accuracy": 65},
            "Inferno": {"damage": 30, "accuracy": 50},
            "Overheat": {"damage": 40, "accuracy": 35}
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

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return str(self.hp)