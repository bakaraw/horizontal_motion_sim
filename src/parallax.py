import pygame
from typing import List

class Parallax:
    bg_layers = []

    def __init__(self, screen_width, image_paths: List[str]):
        for i, path in enumerate(image_paths):
            length = len(image_paths)
            image = pygame.image.load(path)
            width, height = image.get_size()
            aspect_ratio = width / height
            image = pygame.transform.scale(image, (screen_width, int(screen_width / aspect_ratio)))
            speed_multiplier = 1 / (length - i)
            y_offset = 0  # Default Y-offset for all layers
            if "trees" in path:  # Adjust Y-offset specifically for the trees
                y_offset = -220  # Raise the trees higher (tune this value as needed)
            self.bg_layers.append((image, speed_multiplier, y_offset))

    def draw(self, screen, scroll):
        for layer, speed_multiplier, y_offset in self.bg_layers:
            layer_width = layer.get_width()
            x_offset = -(scroll * 4 * speed_multiplier) % layer_width
            screen.blit(layer, (x_offset, y_offset))
            screen.blit(layer, (x_offset - layer_width, y_offset))