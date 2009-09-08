'''OpenGL extension EXT.texture_array

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.texture_array to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.texture_array import *
### END AUTOGENERATED SECTION