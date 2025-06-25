import cv2
import curses

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

wrapper(main)

# Function to extract frames
def FrameCapture(path):

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:

        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        for i in image:
            for j in i:
                if j.any():
                    print(j,end="")
            print("ok", count)

        count += 1


# Driver Code
if __name__ == '__main__':
    pass
    # Calling the function
    # FrameCapture("Bad Apple.mp4")