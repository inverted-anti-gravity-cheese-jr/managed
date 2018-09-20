import sys, pygame
from constants import gameFont, Colors
from canvas import screen, canvas, screenWidth, screenHeight
from taskListScreen import TaskListScreen

currentScreen = TaskListScreen()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    currentScreen.draw(canvas, pygame.time.get_ticks())
    screen.blit(pygame.transform.scale2x(canvas), (0, 0))
    pygame.display.flip()