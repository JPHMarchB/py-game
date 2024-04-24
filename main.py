import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 500, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space move")

BG = pygame.transform.scale(pygame.image.load("bg-image.jpg"), (WIDTH, HEIGHT))
FONT = pygame.font.SysFont("comicsans", 20)

# Player variables
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 50
PLAYER_VEL = 10

# Enemy variables
STAR_WIDTH = 5
STAR_HEIGHT = 5
STAR_VEL = 5

# Game asset view
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()



# Main script defining the game
def main():
    run = True

    # Player element (A Small rectangle and its position on the screen)
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    # Conditions for game to run
    while run:
        # Allowed frames in one second
        star_count += clock.tick(60)
        # Time Counter
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(2):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            # Frequency stars get added, slowly decreases each time stars are added 
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

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
        # if keys[pygame.K_w] and player.y - PLAYER_VEL >= 0:
        #     player.y -= PLAYER_VEL
        # if keys[pygame.K_s] and player.y + PLAYER_VEL + player.height <= HEIGHT:
        #     player.y += PLAYER_VEL
        
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break


        draw(player, elapsed_time, stars)
        
    pygame.quit()

if __name__ == "__main__":
    main()