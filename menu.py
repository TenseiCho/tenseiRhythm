import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1600
screen_height = 800
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
        draw_text("Play", font, WHITE, screen, screen_width/2, screen_height/4)
        draw_text("Options", font, WHITE, screen, screen_width/2, screen_height/2)
        draw_text("Exit", font, WHITE, screen, screen_width/2, screen_height*3/4)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    if screen_width/2 - 100 <= mouse_x <= screen_width/2 + 100 and screen_height/2 - 20 <= mouse_y <= screen_height/2 + 20:
                        # Start the game
                        game()
                    elif screen_width/2 - 100 <= mouse_x <= screen_width/2 + 100 and screen_height*3/4 - 20 <= mouse_y <= screen_height*3/4 + 20:
                        pygame.quit()
                        sys.exit()

def game():
    # Game logic goes here
    pass

main_menu()