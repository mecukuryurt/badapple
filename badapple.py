import cv2
import curses
import time
import os
import numpy
from datetime import datetime

from curses import wrapper

def main():
    print("START")
    stdscr = curses.initscr()
    # Clear screen
    stdscr.clear()

    # curses.nocbreak()
    curses.noecho()

    # This raises ZeroDivisionError when i == 10.

    vidObj = cv2.VideoCapture("Bad Apple.mp4")

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    fps = vidObj.get(cv2.CAP_PROP_FPS)
    width  = vidObj.get(3)  # float `width`
    height = vidObj.get(4)  # float `height`
    
    dldef = 1000 / fps

    remnant = 0

    while success:
        st = datetime.now()
        stdscr.refresh()
        ## print(width, height)
        # vidObj object calls read
        # function extract frames
        
        success, image = vidObj.read()

        # Saves the frames with frame-count
        
        if True:
            for i in range(90):
                for j in range(120):
                    if (image[i*4][j*4] == numpy.array([255,255,255])).all():
                        stdscr.addstr(i,j*2,"##")
                        
                    else:
                        stdscr.addstr(i,j*2,"  ")

        # print(type(image[0][0]))
        
        end = datetime.now()
        elp = end-st
        elp = elp.microseconds/1000
        if (elp > dldef): remnant += -int(dldef - elp)
        
        print(int(dldef-elp), elp, remnant)
        count += 1
        
        curses.delay_output(max(0,int(dldef-elp - 4*(remnant>0) - 2.5)))
        
        if (remnant > 0 and int(dldef-elp - 4*(remnant>0)) > 0): remnant-=4
        
        # print(count)
        

# wrapper(main)

main()
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
    # FrameCapture("Bad Apple.mp4")