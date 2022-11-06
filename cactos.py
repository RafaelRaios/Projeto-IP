import pygame

pygame.init()

#Classes dos cactos 
class Cacto(pygame.sprite.Sprite):
    def __init__(self, size, cx, cy):
        super().__init__()
        self.image = pygame.image.load("sprites/cacto.png")
        self.image = pygame.transform.scale(self.image, size)
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(bottomleft = (cx, cy))
        self.mask = pygame.mask.from_surface(self.image)

class Cacto_invertido(pygame.sprite.Sprite):
    def __init__(self, cx, cy):
        super().__init__()
        self.image = pygame.image.load("sprites/cacto_invertido.png")
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (cx, cy))
        self.mask = pygame.mask.from_surface(self.image)


