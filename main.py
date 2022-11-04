import pygame
import random
pygame.init()

def main():
    # load Game
    game = Director()

    # Load Window
    window = Window(900, 500, 'cse210-04 DINO ROCKET!!!', (255, 255, 255), 60)

    # Load Speech
    speech = Speech()

    # load Points
    points = Points(10)

    # Load in Player
    player = Player('player.png', 100, 100, 450, 400, 10)

    # Load in Rock
    rock = Rock('rock.png', 50, 50, random.randint(0,900), -150, 20)

    # Load in Gem
    gem = Gem('gem.png', 50, 50, random.randint(0,900), -150, 9)

    game.start(player, rock, gem, window, points, speech)

class Director():
    # Manages the game (movement / collision)
    # holds the loop
    # keeps the game playing
    def __init__(self) -> None:
        self.playing = True

        # Setup the game clock (FPS)
        self.clock = pygame.time.Clock()

    def start(self, player, rock, gem, window, points, speech):
        # holds game loop aslong as self.playing is True
        while self.playing:
            # Make sure Frame Rate doesn't go over FPS
            self.clock.tick(window.FPS)

            # Keep track of the in game events
            for event in pygame.event.get():

                # Event: Quit game
                if event.type == pygame.QUIT:
                    self.playing = False

                if points.points <= 0:
                    self.playing = False

            # check collision
            gem.collision(player, points, speech)
            rock.collision(player, points, speech)

            # move player
            player.move()

            # move rock
            rock.gravity()
            rock.respawn()

            # move gem
            gem.gravity()
            gem.respawn()

            # Update window
            window.draw(player, rock, gem, points, speech)
        pygame.quit()

class Window():
    # holds the display for the game
    # updates the window every frame
    def __init__(self, width, height, name, background, FPS) -> None:
        self.width = width
        self.height = height
        self.name = name
        self.background = background 
        self.FPS = FPS


        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)

    def draw(self, player, rock, gem, points, speech):
        # This has to be in order from bottom layer to top layer. 
        # Other wise the back ground will just draw over the scene
        # Background Color
        self.display.fill(self.background)

        # Draw player
        self.display.blit(player.image,(player.x, player.y))

        # Draw rock
        self.display.blit(rock.image, (rock.x, rock.y))

        # Draw gem
        self.display.blit(gem.image, (gem.x, gem.y))

        # Update title to show points
        pygame.display.set_caption(f'{self.name} | Score: {points.points}')


        self.font = pygame.font.Font('freesansbold.ttf', 32)
        text = self.font.render(F'{speech.message}', True, (0,0,0), (255, 255, 255))
        textRect = text.get_rect()
        self.display.blit(text, textRect)
        

        # Change the screen
        pygame.display.update()

class Objects():
    # Class used for creating players, rocks and gems
    def __init__(self, path, width, height, x, y, speed):
        self.path = path
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed

        # Load in image / hitbox
        self.image_l = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image_l, (self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

class Rock(Objects):
    # objects that will damage / remove points from the player.
    def __init__(self, path, width, height, x, y, speed):
        super().__init__(path, width, height, x, y, speed)
    
    def gravity(self):
        self.y += self.speed
    
    def respawn(self):
        if self.y > 650:
            self.y = -150
            self.x = random.randint(0,900)

    def collision(self, player, points, speech):
        self.center_x = self.x + (self.width / 2)
        self.center_y = self.y + (self.height / 2)
        if self.center_x in range(player.x, player.x + player.width):
            if self.center_y in range(player.y, player.y + player.height):
                points.sub()
                self.y = -150
                self.x = random.randint(0,900)
                speech.hurt()

class Gem(Objects):
    # Objects that will give the player points. (and a full stomach)
    def __init__(self, path, width, height, x, y, speed):
        super().__init__(path, width, height, x, y, speed)

    def gravity(self):
        self.y += self.speed
    
    def respawn(self):
        if self.y > 650:
            self.y = -150
            self.x = random.randint(0,900)
    
    def collision(self, player, points, speech):
        self.center_x = self.x + (self.width / 2)
        self.center_y = self.y + (self.height / 2)
        if self.center_x in range(player.x, player.x + player.width):
            if self.center_y in range(player.y, player.y + player.height):
                points.add()
                self.y = -150
                self.x = random.randint(0,900)
                speech.eat()

class Player(Objects):
    # object that moves around collecting points
    def __init__(self, path, width, height, x, y, speed):
        super().__init__(path, width, height, x, y, speed)
    
    def move(self):
        # Find all keys pressed
        keys_pressed = pygame.key.get_pressed()

        # Move player left
        if keys_pressed[pygame.K_LEFT]:
            self.x -= self.speed

        # Move player right
        if keys_pressed[pygame.K_RIGHT]:
            self.x += self.speed

class Points():
    # score used to keep gaming playing
    def __init__(self, points) -> None:
        self.points = points

    def add(self):
        self.points += 2

    def sub(self):
        self.points -= 6

class Speech():
    # Talks for the dinosour
    def __init__(self) -> None:
        self.message = 'Welcome!'

    def eat(self):
        self.message = 'Yum!'

    def hurt(self):
        self.message = 'Ouch...'


if __name__ == '__main__':
    main()
