
from winreg import *
import regaux

if __name__ == "__main__":
    k = OpenKeyEx(HKEY_LOCAL_MACHINE, 'SOFTWARE\\classes\\clsid')
    for i in regaux.keys(k):
        try:
            sk = OpenKeyEx(k, i + '\\progid')
            print(QueryValueEx(sk, ''))
        except:
            pass
