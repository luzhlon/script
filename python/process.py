from subprocess import PIPE
import subprocess
import threading
import platform as plat

if plat.system() == 'Windows':
    encoding                = 'gbk'
    startupinfo             = subprocess.STARTUPINFO()
    startupinfo.dwFlags     = subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
else:
    encoding    = 'utf-8'
    startupinfo = None
class Process(subprocess.Popen):
    bufsize = 1024
    def __init__(self, cmd, **args):
        args.update({'stdin': PIPE, 'stdout': PIPE,
            'stderr': PIPE, 'startupinfo': startupinfo})
        super(Process, self).__init__(cmd, **args)
    def _quit(self):
        if hasattr(self, 'on_quit'):
            self.on_quit(self)
    def read(self, callback):
        '''启动一个线程循环读取输出，并传递给回调函数'''
        def foo():
            while 1:
                l = self.stdout.read1(Process.bufsize)
                if not l and not self.alive():
                    self._quit()
                    break
                callback(self, l.decode(encoding=encoding, errors='replace'))
        threading.Thread(target=foo).start()
    def readline(self, callback):
        '''启动一个线程循环读取一行输出，并传递给回调函数'''
        def foo():
            while 1:
                l = self.stdout.readline()
                if not l and not self.alive():
                    self._quit()
                    break
                callback(self, l.decode(encoding=encoding, errors='replace'))
        threading.Thread(target=foo).start()
    def write(self, data):
        '''向标准输入里写入一段数据'''
        if type(data) is str:
            data = data.encode()
        self.stdin.write(data)
    def exec(self, data):
        '''向标准输入里写入一行命令'''
        self.write(data+'\n')
        self.stdin.flush()
    def alive(self):
        '''判断子进程是否存活'''
        return self.poll() == None

if __name__ == "__main__":
    Process('cmd /c dir').read(lambda p,d: print(d))
