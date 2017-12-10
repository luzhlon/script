import ctypes, win32con, ctypes.wintypes, win32gui,threading, time, sys
EXIT = False #用来传递退出的参数
class Hotkey(threading.Thread):  #创建一个Thread.threading的扩展类
    def run(self):
        global EXIT  #定义全局变量，这个可以在不同线程见共用。
        user32 = ctypes.windll.user32  #加载user32.dll
        if not user32.RegisterHotKey(None, 99, win32con.MOD_ALT, win32con.VK_F3):   # 注册快捷键 alt + f3 并判断是否成功。
            raise                                                                   # 返回一个错误信息
	#以下为判断快捷键冲突，释放快捷键
        try:
            msg = ctypes.wintypes.MSG()
            print(msg)
            while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    if msg.wParam == 99:
                        EXIT = True
                        return
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 1)

#以下用于测试，再当作模块使用的时候，不会运行
if __name__ == "__main__":
    hotkey = Hotkey()
    hotkey.start()
    n = 1
    while 1:
        time.sleep(1)
        print(n)
        n += 1
        if EXIT:
            sys.exit()
