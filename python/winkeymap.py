# FileName   : winkeymap.py
# Author     : luzhlon
# Function   : 向Windows注册表写入按键映射
# Note       : 以管理员权限运行，重启后生效
# LastChange : 2017/2/17

from winreg import *

map_dict = {
  'Escape'      :0x0001, 0x0001: 'Escape',
  'Tab'         :0x000F, 0x000F: 'Tab',
  'CapsLock'    :0x003A, 0x003A: 'CapsLock',
  'LeftAlt'     :0x0038, 0x0038: 'LeftAlt',
  'LeftCtrl'    :0x001D, 0x001D: 'LeftCtrl',
  'LeftShift'   :0x002A, 0x002A: 'LeftShift',
  'LeftWindows' :0xE05B, 0xE05B: 'LeftWindows',
  'RightAlt'    :0xE038, 0xE038: 'RightAlt',
  'RightCtrl'   :0xE01D, 0xE01D: 'RightCtrl',
  'RightShift'  :0x0036, 0x0036: 'RightShift',
  'RightWindows':0xE05C, 0xE05C: 'RightWindows',
  'Backspace'   :0x000E, 0x000E: 'Backspace',
  'Delete'      :0xE053, 0xE053: 'Delete',
  'Enter'       :0x001C, 0x001C: 'Enter',
  'Space'       :0x0039, 0x0039: 'Space',
  'Insert'      :0xE052, 0xE052: 'Insert',
  'Home'        :0xE047, 0xE047: 'Home',
  'End'         :0xE04F, 0xE04F: 'End',
  'NumLock'     :0x0045, 0x0045: 'NumLock',
  'PageDown'    :0xE051, 0xE051: 'PageDown',
  'PageUp'      :0xE049, 0xE049: 'PageUp',
  'ScrollLock'  :0x0046, 0x0046: 'ScrollLock'
}

def bin2map(bin):
    maps = []
    n = int.from_bytes(bin[8:12], 'little') - 1
    i = 12
    while n:
        x = int.from_bytes(bin[i:i+2], 'little')
        y = int.from_bytes(bin[i+2:i+4], 'little')
        maps.append((map_dict[x], map_dict[y]))
        i += 4; n -= 1
    return maps

def map2bin(maps):
    bin = b'\x00'*8
    bin += (len(maps)+1).to_bytes(4, 'little')
    for t in maps:
        x = map_dict[t[0]]
        y = map_dict[t[1]]
        bin += x.to_bytes(2, 'little') + y.to_bytes(2, 'little')
    bin += b'\x00'*4
    return bin

K = 'Scancode Map'
H = CreateKey(HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\Keyboard Layout')

def read_map():
    try            :
        bin = QueryValueEx(H, K)[0]
        return bin2map(bin)
    except FileNotFoundError as err:
        return []

def write_map(maps):
    try:
        SetValueEx(H, K, 0, REG_BINARY, map2bin(maps))
    except PermissionError as err:
        print(err)
#print(read_map())

write_map([('CapsLock'  , 'RightCtrl'),
           ('RightCtrl'    , 'CapsLock')])

H.Close()
