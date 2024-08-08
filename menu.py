import game as game_module
import options
import pygame
from pygame import mixer
import sys
import logging

# Initialize logging
logging.basicConfig(filename='game_log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Pygame
try:
    pygame.init()
    mixer.init()
except pygame.error as e:
    logging.error(f"Failed to initialize Pygame: {e}")
    print("Failed to initialize Pygame. Check game_log.txt for details.")
    sys.exit(1)

# Set up the display
screen_width = 1600
screen_height = 800
try:
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Main Menu")
except pygame.error as e:
    logging.error(f"Failed to set up display: {e}")
    print("Failed to set up display. Check game_log.txt for details.")
    sys.exit(1)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
try:
    font = pygame.font.Font(None, 36)
except pygame.error as e:
    logging.error(f"Failed to load font: {e}")
    print("Failed to load font. Using system default.")
    font = pygame.font.SysFont(None, 36)

def draw_text(text, font, color, surface, x, y):
    try:
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.centerx = x
        text_rect.centery = y
        surface.blit(text_obj, text_rect)
    except pygame.error as e:
        logging.error(f"Failed to draw text: {e}")

def is_point_inside_rect(point, rect_center, rect_size):
    x, y = point
    cx, cy = rect_center
    width, height = rect_size
    return cx - width/2 <= x <= cx + width/2 and cy - height/2 <= y <= cy + height/2

def handle_menu_click(mouse_pos, items):
    for item in items:
        if is_point_inside_rect(mouse_pos, item['center'], item['size']):
            return item['action']
    return None

def main_menu():
    # Load the background image
    try:
        background_image = pygame.image.load('images/menu_background.png')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    except pygame.error as e:
        logging.error(f"Failed to load background image: {e}")
        background_image = pygame.Surface((screen_width, screen_height))
        background_image.fill(BLACK)

    # Load the exit sound
    try:
        exit_sound = mixer.Sound('sounds/exit_sound.wav')
    except pygame.error as e:
        logging.error(f"Failed to load exit sound: {e}")
        exit_sound = None

    menu_items = [
        {'text': "Play", 'center': (screen_width/2, screen_height/4), 'size': (200, 40), 'action': game},
        {'text': "Options", 'center': (screen_width/2, screen_height/2), 'size': (200, 40), 'action': lambda: options.options_menu(screen, font)},
        {'text': "Exit", 'center': (screen_width/2, screen_height*3/4), 'size': (200, 40), 'action': 'exit'}
    ]

    while True:
        screen.blit(background_image, (0, 0))
        
        for item in menu_items:
            draw_text(item['text'], font, WHITE, screen, *item['center'])
        
        try:
            pygame.display.update()
        except pygame.error as e:
            logging.error(f"Failed to update display: {e}")
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    action = handle_menu_click(event.pos, menu_items)
                    if action:
                        if action == 'exit':
                            if exit_sound:
                                exit_sound.play()
                                while mixer.get_busy():
                                    pygame.time.delay(100)
                            return
                        elif callable(action):
                            try:
                                result = action()
                                if result is False:  # For options menu
                                    return
                            except Exception as e:
                                logging.error(f"Error in menu action: {e}")
                        else:
                            try:
                                action()
                            except Exception as e:
                                logging.error(f"Error in menu action: {e}")

def game():
    try:
        game_module.main()
    except Exception as e:
        logging.error(f"Error in game module: {e}")

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        logging.error(f"Unexpected error in main menu: {e}")
    finally:
        pygame.quit()
        sys.exit()