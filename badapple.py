import cv2
import curses
import time
import os
import numpy

from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # curses.nocbreak()
    curses.noecho()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

        stdscr.refresh()
        stdscr.getkey()

# wrapper(main)

# Function to extract frames
def FrameCapture(path):

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:
        width  = vidObj.get(3)  # float `width`
        height = vidObj.get(4)  # float `height`
        ## print(width, height)
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        
        if True:
            for i in range(90):
                for j in range(120):
                    if not  (image[i*4][j*4] == numpy.array([0,0,0])).all():
                        print("#",end="")
                    else:
                        print(" ", end="")
                print()
            os.system("cls")
        print(type(image[0][0]))

        count += 1


# Driver Code
if __name__ == '__main__':
    pass
    # Calling the function
    FrameCapture("Bad Apple.mp4")