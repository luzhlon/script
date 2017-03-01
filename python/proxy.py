import socket, sys, re, os, time
from threading import Thread, Lock
from collections import deque
# TODO:
#       错误使用日志记录

# Proxy用于单独开一个线程监听端口，保存Accept的连接到一个队列里，供其它线程获取并处理
class Proxy(Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self._work = 1          # is working
        self._lock = Lock()     # 
        self._quene = deque()   # quene of unhandled connection
        self.host = host
        self.port = port
        self.start()
# 结束监听线程
    def endWork(self):
        self._lock.acquire()
        self._work = 0
        self._lock.release()
#
    def isWorking(self):
        self._lock.acquire()
        ret = self._work
        self._lock.release()
        return ret
# 添加一个连接到队列里
    def putConn(self, conn):
        print('[new connection]', conn)
        self._quene.append(conn)
# 从队列里获取一个连接
    def getConn(self):
        try:
            return self._quene.popleft()
        except IndexError:
            return 0
# 类方法:从HTTP请求头里解析出连接信息：地址、端口
    def parseConn(header):
        if not header:
            return 0
        m = re.search('\r\nHost:([^\r\n]+)\r\n', header, re.I)
        l = m.group(1).split(':')
        host = l[0].strip()
        port = 80 if len(l) < 2 else int(l[1])
        return (host, port)
    def run(self):
        proxy_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            proxy_sock.bind((self.host, self.port))
        except:
            print('[bind error]')
        proxy_sock.listen(5)
        while 1:
            if not self.isWorking():
                proxy_sock.close()
                return
            self.putConn(proxy_sock.accept())

p = Proxy('0.0.0.0', 8000)
MAX = 2**30
while 1:
    conn = p.getConn()
    if not conn:
        time.sleep(0.1)
        continue
    sock, addr = conn
    print("[client connent] {0}:{1}".format(addr[0], addr[1]))
    #统计访问记录
    #print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    #接收数据
    client_data = sock.recv(MAX).decode()
    if not client_data:
        continue
    print(client_data)
    conn = Proxy.parseConn(client_data)
    #建立连接
    http_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_sock.connect(conn)
    http_sock.sendall(client_data.encode())
    n = 100     # 尝试重新建立连接的次数
    while n:
        try:
            http_data = http_sock.recv(1024)
        except ConnectionResetError:
            print('[reset error] reconnectting...')
            n -= 1
            # 网络不稳定，尝试重新建立连接
            http_sock.close()
            http_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            http_sock.connect(conn)
            http_sock.sendall(client_data.encode())
            continue
        if not http_data:
            break
        sock.send(http_data)            # 转发给浏览器服务器回复的数据
    http_sock.close()

