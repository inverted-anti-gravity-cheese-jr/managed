from pygame import draw
from drawable import Screen
from constants import Colors, gameFont
from gameState import state

class TaskListScreen(Screen):

    def draw(self, canvas, deltatime):
        canvas.fill(Colors.WHITE)

        draw.rect(canvas, Colors.GOJIRA_BG_ACCENT, (0, 0, 320, 16))
        draw.line(canvas, Colors.SHADOW_ACCENT, (0, 16), (320, 16))
        canvas.blit(gameFont.render("dev-Gojira", False, Colors.WHITE), (3, 2))
        canvas.blit(gameFont.render("Managed Dashboard", False, Colors.WHITE), (236, 2))

        for i, task in enumerate(state.tasks):
            canvas.blit(gameFont.render(task, False, Colors.BLACK), (3, 2 + (16 * (i + 1))))

            draw.line(canvas, Colors.SHADOW, (0, 16 * (i + 2)), (320, 16 * (i + 2)))
        
        draw.rect(canvas, Colors.GOJIRA_BG_LIGHT, (0, 224, 320, 240))
        draw.line(canvas, Colors.SHADOW_ACCENT, (0, 223), (320, 223))
        canvas.blit(gameFont.render("Score: " + str(state.score) + ", Tasks: " + str(len(state.tasks)), False, Colors.WHITE), (2, 226))

            