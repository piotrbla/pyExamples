from ctypes import *
print(windll.kernel32)
libName = 'msvcrt.dll'
libc = CDLL(libName)
libc.puts(b"Hello, World!")