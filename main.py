import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 500, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space move")

BG = pygame.transform.scale(pygame.image.load("bg-image.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 50
PLAYER_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)

# Game asset view
def draw(player, elapsed_time):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")

    pygame.draw.rect(WIN, "red", player)

    pygame.display.update()


# Main script defining the game
def main():
    run = True

    # Player element (A Small rectangle and its position on the screen)
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    # Conditions for game to run
    while run:
        # Allowed frames in one second
        clock.tick(60)
        # Time Counter
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()

        # Left and right movement
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        # Up and down movement
        if keys[pygame.K_w] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_s] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL


        draw(player, elapsed_time)
        
    pygame.quit()

if __name__ == "__main__":
    main()