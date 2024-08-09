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


def mergeSort(win, height, font):

    def merge(l, m, r):
        temp = []
        i = l
        j = m + 1
        while i <= m and j <= r:
            if height[i] <= height[j]:
                temp.append(height[i])
                i += 1
            else:
                temp.append(height[j])
                j += 1
        while i <= m:
            temp.append(height[i])
            i += 1
        while j <= r:
            temp.append(height[j])
            j += 1

        i = l
        j = 0
        while i <= r:
            height[i] = temp[j]
            i += 1
            j += 1

    def mergeSorting(l, r):
        if l < r:
            m = (l + r) // 2
            mergeSorting(l, m)
            mergeSorting(m + 1, r);
            merge(l, m, r);

            # fill the window with black color
            win.fill((0, 0, 0))
            # call show method to display the list items
            show(win, height)

            text = font.render('Merge Sort', True, green)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, 400)
            win.blit(text, textRect)

            # create a time delay
            pygame.time.delay(500)
            # update the display
            pygame.display.update()

    mergeSorting(0, len(height) - 1)