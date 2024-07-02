import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Display
screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Options")

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)


def options_menu(screen, font):
    running = True
    while running:
        background_image = pygame.image.load('images/menu_background.png')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(background_image, (0, 0))
        draw_text("Options", font, WHITE, screen, screen.get_width()/2, screen.get_height()/4)
        draw_text("Back", font, WHITE, screen, screen.get_width()/2, screen.get_height()*3/4)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Signal to quit the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    if screen.get_width()/2 - 100 <= mouse_x <= screen.get_width()/2 + 100 and screen.get_height()*3/4 - 20 <= mouse_y <= screen.get_height()*3/4 + 20:
                        return True  # Return to main menu

    return True  # Default to returning to main menu