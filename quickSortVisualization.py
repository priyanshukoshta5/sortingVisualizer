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


def quickSort(win, height, font):

    def partition(low, high):
        # choose the rightmost element as pivot
        pivot = height[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if height[j] <= pivot:
                # if element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # swapping element at i with element at j
                (height[i], height[j]) = (height[j], height[i])

        # swap the pivot element with the greater element specified by i
        (height[i + 1], height[high]) = (height[high], height[i + 1])

        # return the position from where partition is done
        return i + 1


    def quickSorting(low, high):
        if low < high:
            # find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = partition(low, high)

            # recursive call on the left of pivot
            quickSorting(low, pi - 1)

            # recursive call on the right of pivot
            quickSorting(pi + 1, high)

            # fill the window with black color
            win.fill((0, 0, 0))
            # call show method to display the list items
            show(win, height)

            text = font.render('Quick Sort', True, green)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, 400)
            win.blit(text, textRect)

            # create a time delay
            pygame.time.delay(500)
            # update the display
            pygame.display.update()

    quickSorting(0, len(height) - 1)