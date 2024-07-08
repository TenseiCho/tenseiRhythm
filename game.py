import pygame
import math
import json
from pygame import mixer  # Add this import

# Initialize Pygame and the mixer
pygame.init()
mixer.init()

# Screen setup
WIDTH, HEIGHT = 1600, 800
screen = None

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Game variables
center = (WIDTH // 2, HEIGHT // 2)
outer_radius = 350
inner_radius = 300

# Define key mappings and their positions
keys_layout = [
    ('W', -0.9), ('Q', -0.7), ('P', -0.3), ('O', -0.1),
    ('I', 0.1), ('U', 0.3), ('R', 0.7), ('E', 0.9)
]
key_positions = {key: angle for key, angle in keys_layout}
key_pressed = {key: False for key, _ in keys_layout}

current_song = None
beatmap = []
song_time = 0

def draw_dividing_lines():
    # Draw straight lines
    pygame.draw.line(screen, YELLOW, (center[0] - outer_radius, center[1]), (center[0] + outer_radius, center[1]), 2)
    pygame.draw.line(screen, YELLOW, (center[0], center[1] - outer_radius), (center[0], center[1] + outer_radius), 2)
    
    # Draw diagonal lines
    for angle in [math.pi/4, 3*math.pi/4, 5*math.pi/4, 7*math.pi/4]:
        end_x = center[0] + outer_radius * math.cos(angle)
        end_y = center[1] + outer_radius * math.sin(angle)
        pygame.draw.line(screen, YELLOW, center, (end_x, end_y), 2)

def draw_game():
    screen.fill(BLACK)
    
    # Draw outer and inner circles to create the ring
    pygame.draw.circle(screen, WHITE, center, outer_radius, 2)
    pygame.draw.circle(screen, BLACK, center, inner_radius)
    
    # Draw dividing lines
    draw_dividing_lines()
    
    # Draw keys
    font = pygame.font.Font(None, 72)
    for key, angle in key_positions.items():
        # Calculate position
        x = center[0] + math.cos(angle * math.pi) * (outer_radius + inner_radius) / 2
        y = center[1] + math.sin(angle * math.pi) * (outer_radius + inner_radius) / 2
        
        # Draw key letter
        text_surface = font.render(key, True, RED)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)
        
        # Draw yellow highlight if key is pressed
        if key_pressed[key]:
            highlight_pos = (
                int(x + math.cos(angle * math.pi) * 20),
                int(y + math.sin(angle * math.pi) * 20)
            )
            pygame.draw.circle(screen, YELLOW, highlight_pos, 10)

def handle_key_event(event):
    if event.type == pygame.KEYDOWN:
        for key in key_positions.keys():
            if event.key == pygame.key.key_code(key):
                key_pressed[key] = True
    elif event.type == pygame.KEYUP:
        for key in key_positions.keys():
            if event.key == pygame.key.key_code(key):
                key_pressed[key] = False

def load_beatmap(song_name):
    global current_song, beatmap, song_time
    current_song = song_name
    beatmap_file = f"beatmaps/{song_name}.json"
    with open(beatmap_file, 'r') as f:
        beatmap = json.load(f)
    song_time = 0  # Reset song time when loading a new beatmap

def load_and_play_song(song_name):
    global current_song
    current_song = song_name
    mixer.music.load(f"music/{song_name}.wav")
    mixer.music.play()

def main():
    global screen, song_time
    screen = pygame.display.get_surface()
    if screen is None:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    pygame.display.set_caption("WACCA-inspired Rhythm Game")
    
    clock = pygame.time.Clock()
    running = True
    
    # Load a beatmap and play the song
    load_beatmap("Chiwawa")
    load_and_play_song("Chiwawa")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            else:
                handle_key_event(event)
        
        # Update song time based on actual playback position
        song_time = pygame.mixer.music.get_pos() / 1000.0  # Convert to seconds

        # Check for notes to hit
        for note in beatmap:
            if note['time'] <= song_time < note['time'] + 0.1:  # 100ms hit window
                # Highlight the key to press
                key_pressed[note['key']] = True
            elif song_time >= note['time'] + 0.1:
                key_pressed[note['key']] = False

        draw_game()
        
        pygame.display.flip()
        clock.tick(60)

    # Stop the music when the game ends
    mixer.music.stop()

    return

if __name__ == "__main__":
    main()