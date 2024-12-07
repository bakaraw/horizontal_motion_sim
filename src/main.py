import pygame
from typing import List

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_layers = []
    load_layers(
        bg_layers, [
            "assets/far_clouds.png", 
            "assets/near_clouds.png", 
            "assets/far_mountains.png",
            "assets/mountains.png",
            "assets/trees.png",
        ]
    )
    bg_position_x = 0
    velocity = 0
    accelaration = 0
    max_velocity = 200
    running = True
    clock = pygame.time.Clock()

    # Main game loop
    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            accelaration += 10
        if key[pygame.K_DOWN]:
            accelaration -= 10

        # change in time
        delta_time = clock.tick(FPS) / 1000

        # formula: (v = v0 + a * t)
        velocity += accelaration * delta_time
        velocity = max(-max_velocity, min(max_velocity, velocity))
        if velocity < 0:
            velocity = 0

        # formula: (x = x0 + v * t)
        bg_position_x += velocity * delta_time
        print(velocity)

        sky = pygame.image.load("assets/sky.png")
        width, height = sky.get_size()
        aspect_ratio = width / height
        sky = pygame.transform.scale(sky, (SCREEN_WIDTH, int(SCREEN_WIDTH / aspect_ratio)))
        screen.blit(sky, (0, 0))

        draw_layers(screen, bg_layers,  bg_position_x)
        pygame.draw.rect(screen, (44, 37, 70), (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
        van_sprite = pygame.image.load("assets/van_frames/frame000.png")
        width, height = van_sprite.get_size()
        aspect_ratio = width / height
        van_sprite = pygame.transform.scale(van_sprite, (200, 200/aspect_ratio))
        screen.blit(van_sprite, (50, SCREEN_HEIGHT - 120))
        pygame.display.flip()

    pygame.quit()


def load_layers(bg_layers, image_paths: List[str]):
    for i, path in enumerate(image_paths):
        length = len(image_paths)
        image = pygame.image.load(path)
        width, height = image.get_size()
        aspect_ratio = width / height
        image = pygame.transform.scale(image, (SCREEN_WIDTH, float(SCREEN_WIDTH / aspect_ratio)))
        speed_multiplier = 1 / (length - i)
        bg_layers.append((image, speed_multiplier))

def draw_layers(screen, bg_layers, scroll):
    for layer, speed_multiplier in bg_layers:
        layer_width = layer.get_width()
        x_offset = -(scroll * speed_multiplier) % layer_width
        screen.blit(layer, (x_offset, 0))
        screen.blit(layer, (x_offset - layer_width, 0))


if __name__ == "__main__":
    main()
