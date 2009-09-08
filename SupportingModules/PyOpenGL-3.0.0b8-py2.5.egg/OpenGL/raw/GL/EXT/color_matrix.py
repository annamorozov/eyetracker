'''OpenGL extension EXT.color_matrix

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/color_matrix.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes



def glInitColorMatrixEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_EXT_color_matrix' )
