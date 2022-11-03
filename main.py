import pygame

class Director():
    # Manage the game / events
    # keeps track of score
    # Keeps the game moving
    def __init__(self, width, height, name, background, FPS, score):
        self.width = width
        self.height = height
        self.name = name
        self.background = background
        self.FPS = FPS
        self.score = score

    def name_window(self):
        # Sets the game window name
        pygame.display.set_caption(self.name)

class Object():
    def __init__(self, path):
        self.path = pygame.image.load(path)


class Player():

    def __init__(self):
        self.path = 'player.png'

def main():
    # Define Variables
    # Game
    width = 900
    height = 500
    name = 'cse210-04'
    background = (255, 255, 255)
    FPS = 60
    score = 0

    # Player
    player_path = 'player.png'

    # Define Classes
    game = Director(width, height, name, background, FPS, score)
    player = Object(player_path)
    
    # Define Game window
    WIN = pygame.display.set_mode((game.width, game.height))
    game.name_window()

    # Setup the game clock (FPS)
    clock = pygame.time.Clock()

    # Start the game loop
    run = True
    while run:

        # Make sure Frame Rate doesn't go over FPS
        clock.tick(game.FPS)

        # Keep track of the in game events
        for event in pygame.event.get():
            # Event: Quit game
            if event.type == pygame.QUIT:
                run = False

        draw_window(WIN, game.background, player.path)
    pygame.quit()

def draw_window(WIN, background, player):

    WIN.blit(player, (300,100))

    # Background Color
    WIN.fill(background)

    pygame.display.update()

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