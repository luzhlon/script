
import socket, json

class Handler:
    def __handler(self, fn):
        pass
    def __handle(self, fn, args):
    def __opened(self, session):
        pass
    def __closed(self, session):
        pass

class Session:
    def __init__(self, handler):
        self.handler = handler
        self.attrdict = {}
        self.databuf = b''

    def getAttr(self, attr):
        return self.attrdict[attr]
    def setAttr(self, attr, value):
        self.attrdict[attr] = value
    def call(self, fn, *args):
        pass
    def _ret(self, num, args):
        if not isinstance(args, list):
            args = list(args)
        args.insert(0, num)
        self.sendFrame(json.dumps(args))

    def postData(self, data):
        self.databuf += data
        self.checkFrame()
    def checkFrame(self):
        while 1:
            frame = self.getFrame()
            if not frame:
                return
            self.handlePack(frame.decode('UTF8'))
    def getFrame(self):
        if len(self.databuf) < 2:
            return None
        size = self.databuf[0] | self.databuf[1] << 8
        n = size + 2
        if len(self.databuf) < n:
            return None
        frame = self.databuf[2:n]
        self.databuf = self.databuf[n:]
    def handlePack(self, pack):
        args = json.loads(pack)
        head = args[0]
        if isinstance(head, int):
            pass
        elif isinstance(head, list):
            call_num = head[0]
            fn = head[1]
            self.handleCall(call_num, fn, args)

    def handleCall(self, num, fn, args):
        self._ret(num, self.handler.__handle(fn, args))
    def doOpen(self):
        getattr(self.handler, '__opened')(self)
    def doClose(self):
        getattr(self.handler, '__closed')(self)


class Client(Session):
    def __init__(self, handler, address = None):
        Session.__init__(self, handler)
        self.address = address
        self.sock = socket.socket()

    def connect(self, address = None):
        if address:
            self.address = address
            self.connect()
        else:
            self.sock.connect(address)
    def sendFrame(self, data):
        if isinstance(data, str):
            data = data.encode('UTF8')
        h = bytes(2)
        l = len(data)
        h[0] = l & 0xFF
        h[1] = (l >> 8) & 0xFF
        self.sendFlush(h+data)
    def sendFlush(self, data):
        return self.sock.send(data)
    def run(self):
        self.connect()
        while 1:
            data = self.sock.recv(1024)
            if not data:
                pass
            self.postData(data)
