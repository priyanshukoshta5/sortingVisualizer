import pygame

# create display window
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 660

green = (0, 255, 0)

# initial position
x = 40
y = 40

# width of each bar
width = 20

def show(win, height):
    for i in range(len(height)):
        pygame.draw.rect(win, (255, 0, 0), (x + 30 * i, y, width, height[i]))


def selectionSort(win, height, font):
    # start sorting using selection sort technique
    for i in range(len(height) - 1):
        for j in range(i + 1, len(height)):
            if height[i] > height[j]:
                t = height[i]
                height[i] = height[j]
                height[j] = t

            # fill the window with black color
            win.fill((0, 0, 0))

            # call show method to display the list items
            show(win, height)

            text = font.render('Selection Sort', True, green)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, 400)
            win.blit(text, textRect)

            # create a time delay
            pygame.time.delay(100)

            # update the display
            pygame.display.update()