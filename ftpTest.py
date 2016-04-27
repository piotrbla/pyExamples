import ftptool
from ftptool import FTPHost
#
passwd = input("podawaj: ")
ahost = FTPHost.connect("ftp.pl", user="anon", password=passwd)
ahost.current_directory = ""
#
for (dirname, subdirs, files) in ahost.walk("."):
    print (dirname, "has file(s)", ", ".join(files))