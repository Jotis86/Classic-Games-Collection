import pygame
import sys
from snake_game import snake_game
from pong_game import pong_game
from space_invaders import space_invaders_game

pygame.init()

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
blue = (50, 153, 213)

# Dimensiones de la pantalla
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Game Collection by Jotis')

font_style = pygame.font.SysFont(None, 50)

def message(msg, color, y_displace=0):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3 + y_displace])

def game_menu():
    menu = True
    while menu:
        dis.fill(blue)
        message("Select a Game", white, -50)
        message("1. Snake Game", white, 0)
        message("2. Pong Game", white, 50)
        message("3. Space Invaders", white, 100)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snake_game()
                elif event.key == pygame.K_2:
                    pong_game()
                elif event.key == pygame.K_3:
                    space_invaders_game()

if __name__ == "__main__":
    game_menu()