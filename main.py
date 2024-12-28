import pygame
from constants import *
from player import *

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

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player1=Player(x,y)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		

		for upd in updatable:
			upd.update(dt)
		for dra in drawable:
			dra.draw(screen)
			
		pygame.display.flip()
		dt=clk.tick(60)/1000


if __name__=="__main__":
	main()
