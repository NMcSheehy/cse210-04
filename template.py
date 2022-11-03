import pygame

class Director():
    # Manage the game / events
    # keeps track of score
    # Keeps the game moving
    def __init__(self):
        self.width = 900
        self.height = 500
        self.name = 'cse210-04'
        self.background = (255, 255, 255)
        self.FPS = 60
        self.score = 0
        
        self.WIN = pygame.display.set_mode((self.width, self.height))

    def start(self):
        def draw_window(self):
            # Background Color
            self.WIN.fill(self.background)
            pygame.display.update()

        # Sets the game window name
        pygame.display.set_caption(self.name)

        # Setup the game clock (FPS)
        clock = pygame.time.Clock()

        # Start Game loop
        run = True
        while run:

            # Make sure Frame Rate doesn't go over FPS
            clock.tick(self.FPS)

            # Keep track of the in game events
            for event in pygame.event.get():
                # Event: Quit game
                if event.type == pygame.QUIT:
                    run = False

            draw_window(self)
        pygame.quit()

class Object():
    def __init__(self):
        self.path = 'gem.png'
        

class Player(Object):
    def __init__(self):
        super().__init__()

class field():
    pass

def main():
    game = Director()
    game.start()


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