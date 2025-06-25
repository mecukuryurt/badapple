import cv2
import curses
import time
import os
import numpy
from datetime import datetime

from curses import wrapper

# brscl = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
brscl = " -:=;><+!rc/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
bl = len(brscl) - 1
def main():
    print("START")
    
    play = True

    if play: stdscr = curses.initscr()
    # Clear screen
    if play: stdscr.clear()

    # curses.nocbreak()
    if play: curses.noecho()

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

    st = datetime.now()

    while success:
        
        if play: stdscr.refresh()
        ## print(width, height)
        # vidObj object calls read
        # function extract frames
        
        success, image = vidObj.read()

        # Saves the frames with frame-count
        
        ratio = 4

        if play:
            for i in range(int(height/ratio)): # 90 120
                for j in range(int(width/ratio)):
                    """
                    if (image[i*ratio][j*ratio] == numpy.array([255,255,255])).all():
                        stdscr.addstr(i,j*2,"##")
                        
                    else:
                        stdscr.addstr(i,j*2,"  ")
                    """
                    idx = bl/255 * image[i*ratio][j*ratio][0]
                    stdscr.addstr(i,j*2,brscl[int(idx)]*2)

        # print(image[0][0][0] ,end=" ------- ")
        count += 1

        elp = datetime.now() - st
        elp = (elp.microseconds // 1000) + elp.seconds * 1000

        dft = int(count * dldef)

        diff = dft-elp

        print(dft, count, elp, diff)
        if play:  stdscr.addstr(int(height/ratio), 0, str(count))
        if play: curses.delay_output(max(0, diff))

        
        
        # print(count)
    exit()

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