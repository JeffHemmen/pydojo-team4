import pygame

HEIGHT = 1000
WIDTH = 1000


black_hole = Actor('spaceship')
black_hole.pos = (500,500)

player1 = Actor('spaceship')
player1.pos = 50, 50
player1.vel = 0, 50
player1.acc = 0, 0


def update_player(p):
    p.acc = ((black_hole.pos[0] - p.pos[0]) // 100 , (black_hole.pos[1] - p.pos[1]) // 100)
    p.pos = (p.pos[0] + p.vel[0], p.pos[1] + p.vel[1])
    p.vel = ((p.vel[0] + p.acc[0]) // 2, (p.vel[1] + p.acc[1]) // 2)
    return

def my_update():
    update_player(player1)
    pygame.time.delay(10)

clock.schedule_interval(my_update, 1/30)

def draw():
    screen.fill((128, 128, 0))
    screen.draw.circle(black_hole.pos, 5, (0,0,0))
    player1.draw()