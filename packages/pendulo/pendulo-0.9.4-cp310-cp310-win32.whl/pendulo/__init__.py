# -*- coding: utf-8 -*-
'''pendulo integration package for PenWin32
  Most of the work is related to locating proper Penwin32.dll with _getdllinfo

  0.9.2 22.03.09 Remove ganessa dependancy and explicit numpy version check
  0.9.3 22.03.11 Refactor - move main code from init to pendulo_core

'''
# Version of the package
__version__ = '0.9.4'

from pendulo.pendulo_core import *
