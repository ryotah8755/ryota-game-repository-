import pygame
import random

class Mewtwo:

    def __init__(self, x, y):
            self.x = x
            self.y = y
            self.image = pygame.image.load("mewtwo_png.png")
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.delta = .1
            self.name = "Pikachu"
            self.hp = 90
            self.moves = {
                "Psycho Cut": {"damage": 10, "accuracy": 100},
                "Confusion": {"damage": 20, "accuracy": 85},
                "Focus Blast": {"damage": 40, "accuracy": 55},
                "Psystrike": {"damage": 45, "accuracy": 35}
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