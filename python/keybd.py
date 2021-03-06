
import win32con, win32api

kt = {
    'LBUTTON'             : win32con.VK_LBUTTON,
    'RBUTTON'             : win32con.VK_RBUTTON,
    'CANCEL'              : win32con.VK_CANCEL,
    'MBUTTON'             : win32con.VK_MBUTTON,
    'XBUTTON1'            : win32con.VK_XBUTTON1,
    'XBUTTON2'            : win32con.VK_XBUTTON2,
    'BACK'                : win32con.VK_BACK,
    'TAB'                 : win32con.VK_TAB,
    'CLEAR'               : win32con.VK_CLEAR,
    'RETURN'              : win32con.VK_RETURN,
    'ENTER'               : win32con.VK_RETURN,
    'SHIFT'               : win32con.VK_SHIFT,
    'CONTROL'             : win32con.VK_CONTROL,
    'CTRL'                : win32con.VK_CONTROL,
    'MENU'                : win32con.VK_MENU,
    'PAUSE'               : win32con.VK_PAUSE,
    'CAPITAL'             : win32con.VK_CAPITAL,
    'KANA'                : win32con.VK_KANA,
    # 'HANGUEL'             : win32con.VK_HANGUEL,
    'HANGUL'              : win32con.VK_HANGUL,
    'JUNJA'               : win32con.VK_JUNJA,
    'FINAL'               : win32con.VK_FINAL,
    'HANJA'               : win32con.VK_HANJA,
    'KANJI'               : win32con.VK_KANJI,
    'ESCAPE'              : win32con.VK_ESCAPE,
    'CONVERT'             : win32con.VK_CONVERT,
    'NONCONVERT'          : win32con.VK_NONCONVERT,
    'ACCEPT'              : win32con.VK_ACCEPT,
    'MODECHANGE'          : win32con.VK_MODECHANGE,
    'SPACE'               : win32con.VK_SPACE,
    'PRIOR'               : win32con.VK_PRIOR,
    'NEXT'                : win32con.VK_NEXT,
    'END'                 : win32con.VK_END,
    'HOME'                : win32con.VK_HOME,
    'LEFT'                : win32con.VK_LEFT,
    'UP'                  : win32con.VK_UP,
    'RIGHT'               : win32con.VK_RIGHT,
    'DOWN'                : win32con.VK_DOWN,
    'SELECT'              : win32con.VK_SELECT,
    'PRINT'               : win32con.VK_PRINT,
    'EXECUTE'             : win32con.VK_EXECUTE,
    'SNAPSHOT'            : win32con.VK_SNAPSHOT,
    'INSERT'              : win32con.VK_INSERT,
    'DELETE'              : win32con.VK_DELETE,
    'HELP'                : win32con.VK_HELP,
    'LWIN'                : win32con.VK_LWIN,
    'RWIN'                : win32con.VK_RWIN,
    'APPS'                : win32con.VK_APPS,
    # 'SLEEP'               : win32con.VK_SLEEP,
    'NUMPAD0'             : win32con.VK_NUMPAD0,
    'NUMPAD1'             : win32con.VK_NUMPAD1,
    'NUMPAD2'             : win32con.VK_NUMPAD2,
    'NUMPAD3'             : win32con.VK_NUMPAD3,
    'NUMPAD4'             : win32con.VK_NUMPAD4,
    'NUMPAD5'             : win32con.VK_NUMPAD5,
    'NUMPAD6'             : win32con.VK_NUMPAD6,
    'NUMPAD7'             : win32con.VK_NUMPAD7,
    'NUMPAD8'             : win32con.VK_NUMPAD8,
    'NUMPAD9'             : win32con.VK_NUMPAD9,
    'MULTIPLY'            : win32con.VK_MULTIPLY,
    '*'                   : win32con.VK_MULTIPLY,
    'ADD'                 : win32con.VK_ADD,
    '+'                   : win32con.VK_ADD,
    'SEPARATOR'           : win32con.VK_SEPARATOR,
    'SUBTRACT'            : win32con.VK_SUBTRACT,
    'DECIMAL'             : win32con.VK_DECIMAL,
    'DIVIDE'              : win32con.VK_DIVIDE,
    '/'                   : win32con.VK_DIVIDE,
    'F1'                  : win32con.VK_F1,
    'F2'                  : win32con.VK_F2,
    'F3'                  : win32con.VK_F3,
    'F4'                  : win32con.VK_F4,
    'F5'                  : win32con.VK_F5,
    'F6'                  : win32con.VK_F6,
    'F7'                  : win32con.VK_F7,
    'F8'                  : win32con.VK_F8,
    'F9'                  : win32con.VK_F9,
    'F10'                 : win32con.VK_F10,
    'F11'                 : win32con.VK_F11,
    'F12'                 : win32con.VK_F12,
    'F13'                 : win32con.VK_F13,
    'F14'                 : win32con.VK_F14,
    'F15'                 : win32con.VK_F15,
    'F16'                 : win32con.VK_F16,
    'F17'                 : win32con.VK_F17,
    'F18'                 : win32con.VK_F18,
    'F19'                 : win32con.VK_F19,
    'F20'                 : win32con.VK_F20,
    'F21'                 : win32con.VK_F21,
    'F22'                 : win32con.VK_F22,
    'F23'                 : win32con.VK_F23,
    'F24'                 : win32con.VK_F24,
    'NUMLOCK'             : win32con.VK_NUMLOCK,
    'SCROLL'              : win32con.VK_SCROLL,
    'LSHIFT'              : win32con.VK_LSHIFT,
    'RSHIFT'              : win32con.VK_RSHIFT,
    'LCONTROL'            : win32con.VK_LCONTROL,
    'CTRL'                : win32con.VK_LCONTROL,
    'RCONTROL'            : win32con.VK_RCONTROL,
    'LMENU'               : win32con.VK_LMENU,
    'RMENU'               : win32con.VK_RMENU,
    'BROWSER_BACK'        : win32con.VK_BROWSER_BACK,
    'BROWSER_FORWARD'     : win32con.VK_BROWSER_FORWARD,
    # 'BROWSER_REFRESH'     : win32con.VK_BROWSER_REFRESH,
    # 'BROWSER_STOP'        : win32con.VK_BROWSER_STOP,
    # 'BROWSER_SEARCH'      : win32con.VK_BROWSER_SEARCH,
    # 'BROWSER_FAVORITES'   : win32con.VK_BROWSER_FAVORITES,
    # 'BROWSER_HOME'        : win32con.VK_BROWSER_HOME,
    'VOLUME_MUTE'         : win32con.VK_VOLUME_MUTE,
    'VOLUME_DOWN'         : win32con.VK_VOLUME_DOWN,
    'VOLUME_UP'           : win32con.VK_VOLUME_UP,
    'MEDIA_NEXT_TRACK'    : win32con.VK_MEDIA_NEXT_TRACK,
    'MEDIA_PREV_TRACK'    : win32con.VK_MEDIA_PREV_TRACK,
    # 'MEDIA_STOP'          : win32con.VK_MEDIA_STOP,
    'MEDIA_PLAY_PAUSE'    : win32con.VK_MEDIA_PLAY_PAUSE,
    # 'LAUNCH_MAIL'         : win32con.VK_LAUNCH_MAIL,
    # 'LAUNCH_MEDIA_SELECT' : win32con.VK_LAUNCH_MEDIA_SELECT,
    # 'LAUNCH_APP1'         : win32con.VK_LAUNCH_APP1,
    # 'LAUNCH_APP2'         : win32con.VK_LAUNCH_APP2,
    # 'OEM_1'               : win32con.VK_OEM_1,
    # 'OEM_PLUS'            : win32con.VK_OEM_PLUS,
    # 'OEM_COMMA'           : win32con.VK_OEM_COMMA,
    # 'OEM_MINUS'           : win32con.VK_OEM_MINUS,
    # 'OEM_PERIOD'          : win32con.VK_OEM_PERIOD,
    # 'OEM_2'               : win32con.VK_OEM_2,
    # 'OEM_3'               : win32con.VK_OEM_3,
    # 'OEM_4'               : win32con.VK_OEM_4,
    # 'OEM_5'               : win32con.VK_OEM_5,
    # 'OEM_6'               : win32con.VK_OEM_6,
    # 'OEM_7'               : win32con.VK_OEM_7,
    # 'OEM_8'               : win32con.VK_OEM_8,
    # 'OEM_102'             : win32con.VK_OEM_102,
    'PROCESSKEY'          : win32con.VK_PROCESSKEY,
    # 'PACKET'              : win32con.VK_PACKET,
    'ATTN'                : win32con.VK_ATTN,
    'CRSEL'               : win32con.VK_CRSEL,
    'EXSEL'               : win32con.VK_EXSEL,
    'EREOF'               : win32con.VK_EREOF,
    'PLAY'                : win32con.VK_PLAY,
    'ZOOM'                : win32con.VK_ZOOM,
    'NONAME'              : win32con.VK_NONAME,
    'PA1'                 : win32con.VK_PA1,
    'OEM_CLEAR'           : win32con.VK_OEM_CLEAR,
}
for i in range(0x30, 0x3A):
    kt[chr(i)] = i
for i in range(0x41, 0x5B):
    kt[chr(i)] = i

def KeyDown(k):
    k = k.upper()
    if k in kt:
        code = kt[k]
        win32api.keybd_event(code,
            win32api.MapVirtualKey(code, 0), 0, 0)
def KeyUp(k):
    k = k.upper()
    if k in kt:
        code = kt[k]
        win32api.keybd_event(code,
            win32api.MapVirtualKey(code, 0),
            win32con.KEYEVENTF_KEYUP, 0)
def KeyClick(ks):
    if not type(ks) is tuple:
        ks = (ks,)
    for i in range(0, len(ks)):
        KeyDown(ks[i])
    for i in range(len(ks)-1, -1, -1):
        KeyUp(ks[i])

if __name__ == "__main__":
    import time
    time.sleep(2)
    for i in '12345678':
        KeyClick(i)
