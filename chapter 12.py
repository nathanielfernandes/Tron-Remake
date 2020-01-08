import pygame
import random 


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Rectangle():

    def __init__(self):
        
        self.x = random.randrange(0, 500)
        self.y = random.randrange(0, 500)
        self.change_x = random.randrange(-3, 3)
        self.change_y = random.randrange(-3, 3)
        self.width = random.randrange(20, 70)
        self.height = random.randrange(20, 70)
        
        self.r = random.randrange(0, 255)
        self.g = random.randrange(0, 255)
        self.b = random.randrange(0, 255)

        self.colour = (self.r, self.g, self.b)
        
    def draw(self):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height])
        
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        
class Ellipse(Rectangle):
        
        def draw(self):
            pygame.draw.ellipse(screen, self.colour,[self.x, self.y, self.width, self.height])


pygame.init()
 
# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
my_list = []

for i in range(10000):
    
    my_object = Rectangle()
    my_object = Ellipse()
 
    my_list.append(my_object)
    


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)


    for i in my_list:
        i.move()
        i.draw()
    
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
