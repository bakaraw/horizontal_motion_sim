import pygame
import os
from parallax import Parallax

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Horizontal Motion (Uniform Motion)")

    parallax = Parallax(SCREEN_WIDTH, [
        "assets/far_clouds.png",
        "assets/near_clouds.png",
        "assets/far_mountains.png",
        "assets/mountains.png",
        "assets/trees.png",
    ])

    # Load the road asset
    road_image = pygame.image.load("assets/road.png")
    road_width, road_height = road_image.get_size()
    road_aspect_ratio = road_width / road_height
    road_image = pygame.transform.scale(road_image, (SCREEN_WIDTH, int(SCREEN_WIDTH / road_aspect_ratio)))
    road_x_position = 0  # Initial position of the road

    # Load all frames of the van animation
    van_frames = load_van_frames("assets/van_frames/")
    current_frame_index = 0
    total_frames = len(van_frames)

    bg_position_x = 0
    velocity = 0
    accelaration = 50
    max_velocity = 80
    total_distance = 0
    running = True
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 24)

    # Main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update frame for van animation
        current_frame_index = (current_frame_index + 1) % total_frames
        van_sprite = van_frames[current_frame_index]

        # Change in time
        delta_time = clock.tick(FPS) / 1000

        # Physics calculation (velocity and position)
        velocity += accelaration * delta_time
        velocity = max(-max_velocity, min(max_velocity, velocity))
        if velocity < 0:
            velocity = 0

        bg_position_x += velocity * delta_time
        total_distance += velocity * delta_time

        # Scroll the road
        road_x_position -= velocity * delta_time
        if road_x_position <= -SCREEN_WIDTH:
            road_x_position = 0

        # Draw everything
        draw_sky(screen)
        parallax.draw(screen, bg_position_x)

        # Draw the road with looping and adjusted position
        road_y_position = SCREEN_HEIGHT - road_image.get_height() + 130  # Adjusted position
        screen.blit(road_image, (road_x_position, road_y_position))
        screen.blit(road_image, (road_x_position + SCREEN_WIDTH, road_y_position))


        draw_font(f"Acceleration: {accelaration:.2f} m^2/s^2", screen, font, 10, 10)
        draw_font(f"Velocity: {velocity:.2f} m/s", screen, font, 10, 35)
        draw_font(f"Distance Traveled: {total_distance:.2f} m", screen, font, 10, 60)

        # Draw the van
        width, height = van_sprite.get_size()
        aspect_ratio = width / height
        van_sprite = pygame.transform.scale(van_sprite, (200, int(200 / aspect_ratio)))
        screen.blit(van_sprite, (50, SCREEN_HEIGHT - 120))

        pygame.display.flip()

    pygame.quit()


def load_van_frames(path):
    frames = []
    for file_name in sorted(os.listdir(path)):
        if file_name.endswith('.png'):
            frame = pygame.image.load(os.path.join(path, file_name))
            frames.append(frame)
    return frames

def draw_sky(screen):
    sky = pygame.image.load("assets/sky.png")
    width, height = sky.get_size()
    aspect_ratio = width / height
    sky = pygame.transform.scale(sky, (SCREEN_WIDTH, int(SCREEN_WIDTH / aspect_ratio)))
    screen.blit(sky, (0, 0))

def draw_font(text, screen, font, x, y, color=(255, 255, 255)):
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

if __name__ == "__main__":
    main()
