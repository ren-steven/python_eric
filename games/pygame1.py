import pygame

pygame.init()
screen=pygame.display.set_mode((400,300))

# Add this somewhere after the event pumping and before the display.flip()
pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

is_blue = True

done=False

x = 30
y = 30


while not done:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             done = True
         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
             is_blue = not is_blue

     passed = pygame.key.get_pressed()
     if(passed[pygame.K_RIGHT]): x +=3
     if(passed[pygame.K_LEFT]): x -= 3


     if is_blue:
         color = (0, 128, 255)
     else:
         color = (255, 100, 0)

     pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))


     pygame.display.flip()
