import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1100, 700
DOG_WIDTH, DOG_HEIGHT = 50, 50
SPEED = 3
FRAME_DELAY = 5  # Number of frames to wait before changing GIF frame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load GIF frames (Make sure you add all the frames here)
dog_frames = [
    pygame.image.load('assets/frame1.png'),
    pygame.image.load('assets/frame2.png'),
    pygame.image.load('assets/frame3.png')
    # Add more frames as needed
]

# Resize the frames to the desired size
dog_frames = [pygame.transform.scale(frame, (DOG_WIDTH, DOG_HEIGHT)) for frame in dog_frames]

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dog Chase Game")

def main():
    clock = pygame.time.Clock()
    dog_x, dog_y = WIDTH // 2, HEIGHT // 2  # Start position of the dog
    score = 0
    current_frame = 0  # Start with the first frame of the GIF
    frame_counter = 0  # Keep track of when to change the frame

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Move the dog towards the mouse cursor
        if dog_x < mouse_x:
            dog_x += SPEED
        elif dog_x > mouse_x:
            dog_x -= SPEED

        if dog_y < mouse_y:
            dog_y += SPEED
        elif dog_y > mouse_y:
            dog_y -= SPEED

        # Check for collision
        if abs(dog_x - mouse_x) < DOG_WIDTH and abs(dog_y - mouse_y) < DOG_HEIGHT:
            print(f"Game Over! The dog caught you!\nYour Score: {score}")
            pygame.quit()
            sys.exit()

        # Update score
        score += 1  # Increase score as long as the game is running

        # Cycle through GIF frames
        frame_counter += 1
        if frame_counter >= FRAME_DELAY:
            current_frame = (current_frame + 1) % len(dog_frames)
            frame_counter = 0

        # Clear the screen
        screen.fill(WHITE)

        # Draw the current frame of the dog
        screen.blit(dog_frames[current_frame], (dog_x, dog_y))

        # Display the score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
