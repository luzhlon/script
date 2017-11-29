# FileName    : traits-lib.py
# Author      : luzhlon
# Description : Traits .lib from .dll
# LastChange  : 2017-11-29

import platform, os
import glob, json
from subprocess import Popen, PIPE

def QuerySoftware(key, val = ''):
    import winreg as wr

    key = ('SOFTWARE\\Wow6432Node\\'
            if platform.architecture()[0] == '64bit'
            else 'SOFTWARE\\')  + key
    try:
        k = wr.OpenKeyEx(wr.HKEY_LOCAL_MACHINE, key, access=wr.KEY_QUERY_VALUE)
        return wr.QueryValueEx(k, val)[0] if val else wr.QueryValue(k, val)
    except Exception:
        return ''
    finally:
        wr.CloseKey(k)

def get_msvc_shell(arch):
    def find_vcvarsall(version = None):
        vs_vers = {
            '15.0' : 'VS150COMNTOOLS',
            '14.0' : 'VS140COMNTOOLS',
            '12.0' : 'VS120COMNTOOLS',
            '11.0' : 'VS110COMNTOOLS',
            '10.0' : 'VS100COMNTOOLS',
            '9.0'  : 'VS90COMNTOOLS',
            '8.0'  : 'VS80COMNTOOLS',
            '7.1'  : 'VS71COMNTOOLS',
            '7.0'  : 'VS70COMNTOOLS',
            '6.0'  : 'VS60COMNTOOLS',
            '5.0'  : 'VS50COMNTOOLS',
            '4.2'  : 'VS42COMNTOOLS'
        }
        # return the path of vcvarsall.bat firstly be found
        if not version:
            vers = list(vs_vers.keys())
            # sort the versions from large to small
            vers.sort(key = lambda x: float(x), reverse = True)
            for version in vers:
                path = find_vcvarsall(version)
                if path:
                    return path
        # return the path of vcvarsall.bat whoes version is version
        for path in [vspath + subpath \
                     for vspath in [os.environ.get(vs_vers.get(version), ''), \
                                    QuerySoftware('Microsoft\VisualStudio\SxS\VS7', version)]
                     for subpath in ['\\VC\\vcvarsall.bat', '\\VC\\Auxiliary\\Build\\vcvarsall.bat']]:
            if os.path.exists(path):
                return path
        return ''

    vv = find_vcvarsall()
    if not vv:
        print('Can not find the vcvarsall.bat')
        return None

    print('Found vcvarsall.bat', vv)

    return Popen(['cmd', '/k', 'call', vv, arch],
            stdin = PIPE, stdout = PIPE, stderr = PIPE)

def traits_lib(dll_path, lib_path = None, arch = None):
    import pefile, tempfile

    base_name, ext = os.path.splitext(os.path.basename(dll_path))
    def_path = os.path.join(tempfile.gettempdir(), base_name + '.def')
    lib_path = os.path.join(os.getcwd(), base_name + '.lib')
    def_file = open(def_path, 'w')

    pe = pefile.PE(dll_path)
    if not hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
        return print('There is no exports in', dll_path)

    print('Generating def file:', def_path)
    def_file.write('LIBRARY %s\n' % base_name)
    def_file.write('EXPORTS\n')

    n = 1
    for e in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        def_file.write(
                '%s\t@%d\n' % (e.name.decode() if e.name else e.name, n)
                )
        n += 1
    def_file.close()

    if not arch:
        arch = 'x86' if pe.FILE_HEADER.Machine == 0x014c else 'x64'
    print('Use architecture', arch)
    
    if not lib_path:
        lib_path = base_name + '.lib'
    print('Generating lib file:', lib_path)

    env = get_msvc_shell(arch)
    if not env:
        return print('MSVC Tools not found')

    cmd = '\r\n'.join(['@echo off', 'lib.exe /def:"%s" /out:"%s"' % (def_path, lib_path), ''])
    out_, err_ = env.communicate(cmd.encode('gbk'))
    print(out_.decode('gbk'))
    print(err_.decode('gbk'))

def main():
    print('Operating system:', platform.system(),
            platform.architecture()[0], platform.version(), platform.node())

    assert platform.system() == 'Windows'

    traits_lib("libmp4v2.dll")

if __name__ == '__main__':
    main()
