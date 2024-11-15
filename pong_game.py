import pygame
import sys

def pong_game():
    pygame.init()

    # Colores
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Dimensiones de la pantalla
    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Pong Game by Jotis')

    clock = pygame.time.Clock()
    paddle_width = 10
    paddle_height = 100
    ball_size = 10
    paddle_speed = 10
    ball_speed = 5

    font_style = pygame.font.SysFont(None, 50)

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        paddle1_y = dis_height / 2 - paddle_height / 2
        paddle2_y = dis_height / 2 - paddle_height / 2
        ball_x = dis_width / 2
        ball_y = dis_height / 2
        ball_x_change = ball_speed
        ball_y_change = ball_speed

        while not game_over:

            while game_close:
                dis.fill(black)
                message("Game Over! Press C-Continue or Q-Quit", white)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and paddle1_y > 0:
                paddle1_y -= paddle_speed
            if keys[pygame.K_DOWN] and paddle1_y < dis_height - paddle_height:
                paddle1_y += paddle_speed

            # Movimiento de la IA
            if paddle2_y + paddle_height / 2 < ball_y and paddle2_y + paddle_height < dis_height:
                paddle2_y += paddle_speed / 2
            elif paddle2_y + paddle_height / 2 > ball_y and paddle2_y > 0:
                paddle2_y -= paddle_speed / 2

            ball_x += ball_x_change
            ball_y += ball_y_change

            if ball_y <= 0 or ball_y >= dis_height - ball_size:
                ball_y_change *= -1

            if ball_x <= paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height:
                ball_x_change *= -1
            elif ball_x >= dis_width - paddle_width - ball_size and paddle2_y < ball_y < paddle2_y + paddle_height:
                ball_x_change *= -1
            elif ball_x <= 0 or ball_x >= dis_width - ball_size:
                game_close = True

            dis.fill(black)
            pygame.draw.rect(dis, white, [0, paddle1_y, paddle_width, paddle_height])
            pygame.draw.rect(dis, white, [dis_width - paddle_width, paddle2_y, paddle_width, paddle_height])
            pygame.draw.rect(dis, white, [ball_x, ball_y, ball_size, ball_size])
            pygame.display.update()

            clock.tick(60)  # Ajustar la velocidad del juego

        pygame.quit()
        quit()

    gameLoop()

if __name__ == "__main__":
    pong_game()