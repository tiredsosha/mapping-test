from mss import mss
from time import sleep
from mss.tools import to_png

def screenshot(quantity=1, name='screenshot', top=0, left=0, width=1920, height=1080):
    with mss() as sct:
        monitor = {"top": top, "left": left, "width": (quantity * width), "height": (quantity * height)}
        sct_img = sct.grab(monitor)
        to_png(sct_img.rgb, sct_img.size, output=f'{name}.png')


qmon = int(input('Скрин на сколько мониторов надо сделать?\n'))
print()
for i in range(5, 0, -1):
    print(i, 'до скриншота')
    sleep(1)
screenshot(qmon, 'main_screen')
print('скрин сохранен в ту же папку, откуда запущен этот скрипт')
