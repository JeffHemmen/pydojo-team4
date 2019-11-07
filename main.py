alien = Actor('spaceship')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = 500

SPEED = 10

def draw():
    screen.clear()
    alien.draw()
    
    
def on_key_down(key):
    if key == keys.W:
        alien.x += 1
        alien.y += 1
    elif key == keys.A:
        alien.angle -= 1
    elif key == keys.D:
        alien.angle += 1
    elif key == keys.S:
        alien.x -= 1
        alien.y -= 1
        
        
        