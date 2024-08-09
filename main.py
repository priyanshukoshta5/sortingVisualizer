import pygame
import button
from bubbleSortVisualization import bubbleSort
from selectionSortVisualization import selectionSort
from insertionSortVisualization import insertionSort
from mergeSortVisualization import mergeSort
from quickSortVisualization import quickSort

# create display window
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 660

# initializing the pygame window
pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

# load button images
start_img = pygame.image.load('start_image.png').convert_alpha()
reset_img = pygame.image.load('reset_image.png').convert_alpha()
exit_img = pygame.image.load('exit_image.png').convert_alpha()
bubble_img = pygame.image.load('bubble_sort_image.png').convert_alpha()
selection_img = pygame.image.load('selection_sort_image.png').convert_alpha()
insertion_img = pygame.image.load('insertion_sort_image.png').convert_alpha()
merge_img = pygame.image.load('merge_sort_image.png').convert_alpha()
quick_img = pygame.image.load('quick_sort_image.png').convert_alpha()

# create button instances
start_button = button.Button(SCREEN_WIDTH // 2 - 200, 500, start_img, 0.5)
reset_button = button.Button(SCREEN_WIDTH // 2 - 50, 500, reset_img, 0.5)
exit_button = button.Button(SCREEN_WIDTH // 2 + 100, 500, exit_img, 0.5)
bubble_button = button.Button(SCREEN_WIDTH // 2 - 300, 550, bubble_img, 0.5)
selection_button = button.Button(SCREEN_WIDTH // 2 - 175, 550, selection_img, 0.5)
insertion_button = button.Button(SCREEN_WIDTH // 2 - 50, 550, insertion_img, 0.5)
merge_button = button.Button(SCREEN_WIDTH // 2 + 75, 550, merge_img, 0.5)
quick_button = button.Button(SCREEN_WIDTH // 2 + 200, 550, quick_img, 0.5)

# height of each bar (data to be sorted)
height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20, 5, 70, 170, 18, 190, 40]

font = pygame.font.Font('freesansbold.ttf', 32)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# initial position
x = 40
y = 40

# width of each bar
width = 20

def show(height):
    for i in range(len(height)):
        pygame.draw.rect(win, (255, 0, 0), (x + 30 * i, y, width, height[i]))

run = True

while run:

    # time delay
    pygame.time.delay(10)

    show(height)
    pygame.display.update()

    # getting keys pressed
    keys = pygame.key.get_pressed()

    # iterating events
    for event in pygame.event.get():
        # if event is to quit
        if event.type == pygame.QUIT:
            # making run = false so break the while loop
            run = False

    # if 'q' is pressed so QUIT
    if keys[pygame.K_q]:
        run = False

    if start_button.draw(win):
        print('START')

    elif reset_button.draw(win):
        print("RESET")
        height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20, 5, 70, 170, 18, 190, 40]
        win.fill((0, 0, 0))

    elif exit_button.draw(win):
        print('EXIT')
        run = False

    elif bubble_button.draw(win):
        print('BUBBLE')
        bubbleSort(win, height, font)

    elif selection_button.draw(win):
        print('SELECTION')
        selectionSort(win, height, font)

    elif insertion_button.draw(win):
        print('INSERTION')
        insertionSort(win, height, font)

    elif merge_button.draw(win):
        print('MERGE')
        mergeSort(win, height, font)

    elif quick_button.draw(win):
        print('QUICK')
        quickSort(win, height, font)

    pygame.display.update()


pygame.quit()