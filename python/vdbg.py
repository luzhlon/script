#! /usr/bin/python3
# FileName    : dbg.py
# Author      : luzhlon
# Description : 与gdb或者cdb进程间通信，封装一些常见的调试功能
# Note        : 试验性脚本
# LastChange  : 2017/2/17

from subprocess import *
import threading

class Debugger:
    def __init__(self, target):
        self.target(target)
        self._cmd = {}
    def exec(self, cmd):
        i = self.subp.stdin
        i.write((cmd + '\n').encode())
        i.flush()
    def _start_thread(self):
        self._should_alive = 1
        def proc():
            o = self.subp.stdout
            while self._should_alive:
                l = o.readline()
                if not l:
                    break
                print(l.decode(errors='replace'), end='')
        self.thread = threading.Thread(target=proc)
        self.thread.start()
    def _end_thread(self):
        self._should_alive = 0
    def target(self, t = 0):
        if t:
            self._target = t
        else:
            return self._target
    def start(self):
        if not self._target:
            pass                   # no target
    def quit(self):
        self.subp.kill()
        self._end_thread()

class CDB(Debugger):
    def __init__(self, t):
        Debugger.__init__(self, t)
    def start(self):
        Debugger.start(self)
        self.subp = Popen(['cdb', self._target, '-lines', '-ee c++', '-2', '-g'], stdin=PIPE, stdout=PIPE)
        self.exec('l+t')      #进入源代码模式
        self.exec('l+s')      #进入源代码模式
        self._start_thread()
    def bp_once(self, src, line):
        pass
    def bp(self, src, line):
        self.exec('bp `%s:%d`' % (src, line))
    def run(self):
        self.exec('g')
    def next(self):
        self.exec('t')
    def step(self):
        self.exec('p')
    def quit(self):
        self.exec('q')
        Debugger.quit(self)

class GDB(Debugger):
    def start(self):
        Debugger.start(self)
        self.subp = Popen(['gdb', self._target, '-q'], stdin=PIPE, stdout=PIPE)
        self.exec('set prompt')      #关闭命令提示符
        self._start_thread()
    def bp_once(self, src, line):
        pass
    def bp(self, src, line):
        self.exec('b %s:%d' % (src, line))
    def run(self):
        self.exec('r')
    def next(self):
        self.exec('n')
    def step(self):
        self.exec('s')
    def quit(self):
        self.exec('q')
        Debugger.quit(self)

d = CDB('build/test.exe')
d.start()
#d.bp('main.c', 4)
