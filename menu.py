import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Main Menu", font, WHITE, screen, screen_width/2, screen_height/4)
        draw_text("Press 'P' to Play", font, WHITE, screen, screen_width/2, screen_height/2)
        draw_text("Press 'Q' to Quit", font, WHITE, screen, screen_width/2, screen_height*3/4)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    # Start the game
                    game()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def game():
    # Game logic goes here
    pass

main_menu()