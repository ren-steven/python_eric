import pgzrun

from random import randint
apple = Actor("apple")
good_shots = 0
misses = 0

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
       
    
def on_mouse_down(pos):
    global good_shots
    global misses
    if apple.collidepoint(pos):
        good_shots += 1
        print("Good shot!", good_shots)
        place_apple()
    else:
        misses += 1
        print("You missed!", misses)
        place_apple()

       

place_apple()


pgzrun.go()

