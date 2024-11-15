import pygame
import random
import math

def space_invaders_game():
    # Inicializar Pygame
    pygame.init()

    # Crear la pantalla
    screen = pygame.display.set_mode((800, 600))

    # Título
    pygame.display.set_caption("Space Invaders")

    # Jugador
    playerX = 370
    playerY = 480
    playerX_change = 0
    player_width = 50
    player_height = 50

    # Enemigo
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 4  # Reducir el número de enemigos
    enemy_width = 50
    enemy_height = 50

    for i in range(num_of_enemies):
        enemyX.append(random.randint(0, 750))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(1)  # Reducir la velocidad de los enemigos
        enemyY_change.append(40)

    # Bala
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10  # Ajustar la velocidad de las balas
    bullet_state = "ready"
    bullet_radius = 5

    # Puntuación
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)

    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (200, 250))

    def player(x, y):
        pygame.draw.polygon(screen, (0, 0, 255), [(x, y), (x + player_width // 2, y - player_height), (x + player_width, y)])

    def enemy(x, y):
        pygame.draw.rect(screen, (255, 0, 0), (x, y, enemy_width, enemy_height))
        pygame.draw.circle(screen, (255, 0, 0), (x + enemy_width // 2, y), enemy_width // 2)

    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        pygame.draw.circle(screen, (255, 255, 0), (x + player_width // 2, y), bullet_radius)

    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX + enemy_width // 2 - bulletX, 2) + math.pow(enemyY + enemy_height // 2 - bulletY, 2))
        if distance < 27:
            return True
        else:
            return False

    # Bucle del juego
    running = True
    while running:

        # Color de fondo
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Si se presiona una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX + player_width // 2
                        bullet_state = "fire"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Movimiento del jugador
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 750:
            playerX = 750

        # Movimiento del enemigo
        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 1  # Reducir la velocidad de los enemigos
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 750:
                enemyX_change[i] = -1  # Reducir la velocidad de los enemigos
                enemyY[i] += enemyY_change[i]

            # Colisión
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 750)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i])

        # Movimiento de la bala
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    space_invaders_game()