#!/usr/bin/env python
from distutils.core import setup 
import matplotlib
import py2exe 
opts = {
  'py2exe': { "includes" : ["matplotlib.backends.backend_tkagg"],

                'excludes': ['_gtkagg', '_tkagg', '_agg2', '_cairo', '_cocoaagg', "matplotlib.numerix.fft","sip", "PyQt4._qt",
                              "matplotlib.backends.backend_qt4agg",
                               "matplotlib.numerix.linear_algebra", "matplotlib.numerix.random_array",

                             '_fltkagg', '_gtk','_gtkcairo' ],
                'dll_excludes': ['libgdk-win32-2.0-0.dll',
                                 'libgobject-2.0-0.dll']
              }
       }
setup(windows=['analyWin.py'],options=opts)