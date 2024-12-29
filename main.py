import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clk=pygame.time.Clock()
	dt=0
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)

	astero= pygame.sprite.Group()
	Asteroid.containers =(astero, updatable,drawable)

	AsteroidField.containers = (updatable)

	shots= pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player1=Player(x,y)
	
	asteroid_field1 = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		

		for upd in updatable:
			upd.update(dt)

		for ast in astero:
			if ast.check_collision(player1):
				print("Game over!")
				sys.exit()
			for sh in shots:
				if ast.check_collision(sh):
					ast.split()
					sh.kill()

		for dra in drawable:
			dra.draw(screen)
			
		pygame.display.flip()
		dt=clk.tick(60)/1000


if __name__=="__main__":
	main()
