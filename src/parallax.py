import pygame
from typing import List

class Parallax:
    bg_layers = []

    def __init__(self, screen_width, screen_height, image_paths: List[str]):
        for i, path in enumerate(image_paths):
            length = len(image_paths)
            image = pygame.image.load(path)
            width, height = image.get_size()
            aspect_ratio = width / height
            image = pygame.transform.scale(image, (screen_width, float(screen_width / aspect_ratio)))
            speed_multiplier = 1 / (length - i)
            self.bg_layers.append((image, speed_multiplier))

    def draw(self, screen, scroll):
        for layer, speed_multiplier in self.bg_layers:
            layer_width = layer.get_width()
            x_offset = -(scroll * speed_multiplier) % layer_width
            screen.blit(layer, (x_offset, 0))
            screen.blit(layer, (x_offset - layer_width, 0))
