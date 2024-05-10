import pygame


class Gengar:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("gengar_8bit.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1
        self.current_direction = "right"
        self.health = 80
        self.attack_1 = "a"
        self.attack_2 = "b"
        self.attack_3 = "c"
        self.attack_4 = "d"