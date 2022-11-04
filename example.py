import pygame

def main():

    # Define Variables
    width = 900
    height = 500
    name = 'cse210-04'
    background = (255, 255, 255)
    FPS = 60
    score = 0

    # Player Variables
    player_path = 'player.png'
    player_height = 100
    player_width = 100
    player_x = 450
    player_y = 400
    speed = 10

    # Rock Variables
    rock_coords = [(40,50)]
    rock_path = 'rock.png'
    rock_height = 100
    rock_width = 100
    rock_speed = 5

    # Gem Variables


    # Load in the player
    player_image = pygame.image.load(player_path)
    player = pygame.transform.scale(player_image, (player_width, player_height))
    player_hitbox = pygame.Rect(player_x, player_y, player_width, player_height)

    # Load in Rock
    rock_image = pygame.image.load(rock_path)
    rock = pygame.transform.scale(rock_image, (rock_width, rock_height))

    # Load in Gem

    # Define Game Window
    WIN = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)

    # Setup the game clock (FPS)
    clock = pygame.time.Clock()

    # Start the game loop
    run = True
    while run:

        # Make sure Frame Rate doesn't go over FPS
        clock.tick(FPS)

        # Keep track of the in game events
        for event in pygame.event.get():

            # Event: Quit game
            if event.type == pygame.QUIT:
                run = False

        # Find all keys pressed
        keys_pressed = pygame.key.get_pressed()

        # Move player left
        if keys_pressed[pygame.K_LEFT]:
            player_hitbox.x -= speed

        # Move player right
        if keys_pressed[pygame.K_RIGHT]:
            player_hitbox.x += speed

        # Update window
        draw_window(WIN, background, player, player_hitbox)
    pygame.quit()

def draw_window(WIN, background, player, player_hitbox):
    # This has to be in order from bottom layer to top layer. 
    # Other wise the back ground will just draw over the scene

    # Background Color
    WIN.fill(background)

    # Draw player
    WIN.blit(player, (player_hitbox.x, player_hitbox.y))

    # Change the screen
    pygame.display.update()


class Objects():
    def __init__(self, path):
        self.path = path







if __name__ == '__main__':
    main()

# Field
# Noah
# Need to have an area to play the game
# have borders
# falling physics

# Objects
# Paul
# control gravity

    # Player
    # Noah
        # controls 
        # allow you to move with arrow keys rather than typing 'left' or 'right'


    # Rocks
    # Edward
    # will subtract points if they touch player
    # removes object after collision

    # Gems
    # Edward
    # will add points if they touch player
    # removes object after collision

# Spawn
# David
# randomly generate rocks and gems at the top of the screen

# Collision
# Paul
# 