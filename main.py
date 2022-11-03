import pygame

class Director():
    def __init__(self):
        self.width = 900
        self.height = 500
        self.name = 'cse210-04'
        self.background = (255, 255, 255)
        self.FPS = 60

    def start(self):
        clock = pygame.time.Clock
        # Start Game loop
        run = True
        while run:

            # Make sure Frame Rate doesn't go over FPS
            clock.tick(self.FPS)

            # Event: Quit game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
    


class field():
    pass



    

        
# manage the game (keep the game playing)
# keeps track of score
# Keeps the game moving (uses time)

width = 900
height = 500
name = 'cse210-04'
background = (255, 255, 255)
FPS = 60



WIN = pygame.display.set_mode((width,height))
pygame.display.set_caption(name)

def main():
    


    # set the clock
    clock = pygame.time.Clock
    run = True

    while run:
        # Make sure Frame Rate doesn't go over FPS
        clock.tick(FPS)

        # Event: Quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()
        


    pygame.quit()

def draw_window():
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