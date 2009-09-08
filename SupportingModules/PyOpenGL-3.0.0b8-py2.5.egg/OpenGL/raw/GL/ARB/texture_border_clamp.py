'''OpenGL extension ARB.texture_border_clamp

Overview (from the spec)
	
	The base OpenGL provides clamping such that the texture coordinates are
	limited to exactly the range [0,1].  When a texture coordinate is clamped
	using this algorithm, the texture sampling filter straddles the edge of
	the texture image, taking 1/2 its sample values from within the texture
	image, and the other 1/2 from the texture border.  It is sometimes
	desirable for a texture to be clamped to the border color, rather than to
	an average of the border and edge colors.
	
	This extension defines an additional texture clamping algorithm.
	CLAMP_TO_BORDER_ARB clamps texture coordinates at all mipmap levels such
	that NEAREST and LINEAR filters return only the color of the border
	texels.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_border_clamp.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_texture_border_clamp'
GL_CLAMP_TO_BORDER_ARB = constant.Constant( 'GL_CLAMP_TO_BORDER_ARB', 0x812D )


def glInitTextureBorderClampARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
