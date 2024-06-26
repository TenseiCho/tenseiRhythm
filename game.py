import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1600, 800  # Match the menu dimensions
screen = None  # We'll set this in the main function

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Game variables
center = (WIDTH // 2, HEIGHT // 2)
radius = 350  # Increased radius for larger screen
note_speed = 2
notes = []

# Define key mappings
left_keys = [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t]
right_keys = [pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p]
all_keys = left_keys + right_keys

def create_note():
    angle = random.uniform(0, 2 * math.pi)
    return {
        'pos': [center[0] + math.cos(angle) * 20, center[1] + math.sin(angle) * 20],
        'angle': angle,
        'active': True
    }

def move_notes():
    for note in notes:
        if note['active']:
            note['pos'][0] += math.cos(note['angle']) * note_speed
            note['pos'][1] += math.sin(note['angle']) * note_speed
            
            # Check if note is out of bounds
            distance = math.sqrt((note['pos'][0] - center[0])**2 + (note['pos'][1] - center[1])**2)
            if distance > radius:
                note['active'] = False

def draw_game():
    screen.fill(BLACK)
    
    # Draw outer circle
    pygame.draw.circle(screen, WHITE, center, radius, 2)
    
    # Draw dividing lines
    for i in range(10):
        angle = i * (2 * math.pi / 10)
        end_pos = (
            int(center[0] + math.cos(angle) * radius),
            int(center[1] + math.sin(angle) * radius)
        )
        pygame.draw.line(screen, YELLOW, center, end_pos, 2)
    
    # Draw notes
    for note in notes:
        if note['active']:
            pygame.draw.circle(screen, WHITE, [int(note['pos'][0]), int(note['pos'][1])], 10)

def main():
    global screen
    screen = pygame.display.get_surface()  # Get the screen from the existing pygame instance
    if screen is None:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    pygame.display.set_caption("WACCA-inspired Rhythm Game")
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in all_keys:
                    print(f"Key pressed: {pygame.key.name(event.key)}")
                    # Here you would add logic to check if a note was hit
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Return to menu when Escape is pressed
        
        # Spawn new notes randomly
        if random.random() < 0.02:  # Adjust this value to control note frequency
            notes.append(create_note())
        
        move_notes()
        draw_game()
        
        pygame.display.flip()
        clock.tick(60)

    # Don't quit Pygame here, just return to the menu
    return

if __name__ == "__main__":
    main()