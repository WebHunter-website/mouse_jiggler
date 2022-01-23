import time
from datetime import datetime

import pyautogui as pag

def reset_time():
    global mouse_point

    print(f'{datetime.now()} | [TIMER RESET]')

    mouse_point = pag.position()

def mouse_jiggle():
    print(f'{datetime.now()} | [JIGGLING]')
    pag.moveTo(1, 1, duration=1)
    pag.moveTo(mouse_point, duration=1)
    pag.press('ctrlleft')

def check_jiggle():
    global jiggle_every_s
    if mouse_point != pag.position():
        reset_time()
        jiggle_every_s = SHORT_JIGGLE_S 
    else:
        mouse_jiggle()
        jiggle_every_s = LONG_JIGGLE_S 

def main():
    pag.FAILSAFE = False
    print(f'{datetime.now()} | Will jiggle every {jiggle_every_s} seconds')
    while True:
        time.sleep(jiggle_every_s)
        check_jiggle()

SHORT_JIGGLE_S = 60
LONG_JIGGLE_S = 60 * 5
jiggle_every_s = SHORT_JIGGLE_S

mouse_point = pag.position()

if __name__ == '__main__':
    main()
