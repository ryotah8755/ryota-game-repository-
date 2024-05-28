import pygame
import random

class Gengar:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("gengar_8bit.png.")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1
        self.name = "Gengar"
        self.hp = 75
        self.moves = {
            "Shadow Ball": {"damage": 25, "accuracy": 80},
            "Night Shade": {"damage": 15, "accuracy": 90},
            "Dream Eater": {"damage": 30, "accuracy": 70},
            "Dark Pulse": {"damage": 20, "accuracy": 85}
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