import numpy as np
import cv2
import mss
import time
import mss.tools
import win32api, win32con
import mouse
import imagehash
import time
from keyboard import send
from PIL import Image


def click_win32(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def screenstream(top=0, left=0, width=1920, height=1080):
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": top, "left": left, "width": width, "height": height}
        while "Screen capturing":
            img = np.array(sct.grab(monitor))
            cv2.imshow("Stream", img)
            # Display the picture in grayscale
            # cv2.imshow('OpenCV/Numpy grayscale', cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

def screenshot(quantity=1, name='screenshot', top=0, left=0, width=1920, height=1080):
    with mss.mss() as sct:
        monitor = {"top": top, "left": left, "width": (quantity * width), "height": (quantity * height)}
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=f'{name}.png')



def screencap(top=0, left=0, width=1920, height=1080, path='sosha_screencap.avi', codec='XVID', fps=24.0):
    fourcc = cv2.VideoWriter_fourcc(*codec)
    out = cv2.VideoWriter(path, fourcc, fps, (width, height))
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": top, "left": left, "width": width, "height": height}

        while "Screen capturing":
            # Get raw pixels from the screen, save it to a Numpy array
            img = np.array(sct.grab(monitor))
            img = cv2.resize(img, (width, height))
            frame = img
            frame = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)


def map_tclicker(name='mouse.txt'):
    with open(name) as comands:
        comands = comands.readlines()
        for line in comands:
            line = line.split()
            if line[0] == 'click':
                mouse.move(int(line[1]), int(line[2]), absolute=True, duration=0.15)
                mouse.click()
                time.sleep(0.2)
            elif line[0] == 'move':
                mouse.drag(int(line[1]), int(line[2]), int(line[3]), int(line[4]), absolute=True, duration=0.5)
                time.sleep(0.2)
            else:
                send('tab')
                time.sleep(0.2)


def image_compare(qty, px_cutoff=5):
    hmonitors = win32api.EnumDisplayMonitors()
    quantity = 0

    for monitor in hmonitors:
        quantity += 1
    if quantity == qty:
        map_tclicker()
        screenshot(qty, 'test_screen')

        hash0 = imagehash.average_hash(Image.open('main_screen.png'))
        hash1 = imagehash.average_hash(Image.open('test_screen.png'))
        cutoff = px_cutoff # maximum bits that could be different

        if hash0 - hash1 < cutoff:
            return True
        else:
            return 'images are diff'

    else:
        return 'not enought displays'
