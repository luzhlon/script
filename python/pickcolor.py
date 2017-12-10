# Pick the color values under the cursor
# use pywin32

import win32gui as wg
import win32con as wc
import time

dc = wg.GetWindowDC(0)

def output(s):
    wg.DrawText(dc, s, -1, (0,0,1000,1000), wc.DT_LEFT)

lastpos = (-1, -1)
text = ''
while 1:
    pos = wg.GetCursorPos()
    if pos == lastpos:
        continue
    lastpos = pos
    color = wg.GetPixel(dc, pos[0], pos[1])
    r = color & 0xFF;g = color >> 8 & 0xFF
    b = color >> 16 & 0xFF;rgb = (r, g, b)
    output(' ' * len(text) + '                ')
    text = '#%02x%02x%02x   rgb(%d,%d,%d)' % (rgb*2)
    output(text)
    time.sleep(0.01)
