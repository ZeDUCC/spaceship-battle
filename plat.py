import pygame
import os

WIDTH, HEIGHT = 900, 504
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
VEL = 5
BLOCK = pygame.image.load(os.path.join('Kenney', 'tile_0000.png'))
MAIN_BLOCK = pygame.image.load(os.path.join('Kenney', 'tile_0070.png'))

def handle_movement(keys_pressed, block):
    if keys_pressed[pygame.K_w]:
        block.y -= VEL
    if keys_pressed[pygame.K_RIGHT] and (block.x + VEL + block.width) < WIDTH + 15:
        block.x += VEL
    if keys_pressed[pygame.K_UP] and (block.y - VEL) > 0:
        block.y -= VEL
    if keys_pressed[pygame.K_DOWN] and (block.y + VEL + block.height) < HEIGHT - 15:
        block.y += VEL

def main():
    WIN.fill((0, 0, 0))
    block = pygame.Rect(20, 234, 18, 18)
    keys_pressed = pygame.key.get_pressed()
    for j in range(18):
        for i in range(50):
            WIN.blit(BLOCK, (i*18, j*14 + 252))
    
    WIN.blit(MAIN_BLOCK, (20, 234))
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    handle_movement(keys_pressed, block)

    pygame.quit()

if __name__ == "__main__":
    main()