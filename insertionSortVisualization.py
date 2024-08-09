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


def insertionSort(win, height, font):
    # start sorting using insertion sort technique
    for i in range(len(height)):
        for j in range(i - 1, -1, -1):
            if height[j] > height[j + 1]:
                t = height[j]
                height[j] = height[j + 1]
                height[j + 1] = t

            # fill the window with black color
            win.fill((0, 0, 0))

            # call show method to display the list items
            show(win, height)

            text = font.render('Insertion Sort', True, green)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, 400)
            win.blit(text, textRect)

            # create a time delay
            pygame.time.delay(100)

            # update the display
            pygame.display.update()