from distutils.core import setup
import py2exe

setup(console=['matplot.py'], requires=['requests', 'bs4'])