'''OpenGL extension VERSION.GL_3_0

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_3_0 to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.VERSION.GL_3_0 import *
### END AUTOGENERATED SECTION