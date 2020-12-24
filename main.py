import pygame
import random

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

SIZE = [1000, 563]
bg = pygame.image.load("Sprite/bg.jpg")

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")

snow_list = []

leftSteps = []
rightSteps = []
for i in range(1, 3):
	pic = pygame.image.load('Sprite/snowpowl' + str(i) + '.png')
	rightSteps.append(pic)
	pic = pygame.transform.flip(pygame.image.load('Sprite/snowpowl' + str(i) + '.png'), True, False)
	leftSteps.append(pic)

for i in range(140):
	xsnow = random.randrange(0, 1000)
	ysnow = random.randrange(0, 563)
	snow_list.append([xsnow, ysnow])

x = 50
y = 420
width = 120
height = 150
v = 5
w = 1000
num = 0

u = 10
right = False
left = False

clock = pygame.time.Clock()

done = False
while not done:

	for event in pygame.event.get():  # Пользователь сделал что-то
		if event.type == pygame.QUIT:  # Если нажато стоп
			done = True  # выходим из цикла

	screen.blit(bg, (0, 0))

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x - v >= 0:
		x -= v
		left = True
		right = False
	elif keys[pygame.K_RIGHT] and x + width + v <= w:
		x += v
		right = True
		left = False
	else:
		left = right = False
		num = 0

	if left:
		pic = leftSteps[num % 2]
		num += 1
	elif right:
		pic = rightSteps[num % 2]
		num += 1
	screen.blit(pic, (x, y))


	for i in range(len(snow_list)):

		pygame.draw.circle(screen, WHITE, snow_list[i], random.randrange(1, 3))
		snow_list[i][1] += 2

		if snow_list[i][1] > 563:
			ysnow = random.randrange(-50, -10)
			snow_list[i][1] = ysnow
			xsnow = random.randrange(0, 1000)
			snow_list[i][0] = xsnow

	pygame.display.flip()
	clock.tick(20)
pygame.quit()


