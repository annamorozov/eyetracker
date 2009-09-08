'''OpenGL extension ARB.vertex_shader

Overview (from the spec)
	
	This extension adds programmable vertex level processing to OpenGL. The
	application can write vertex shaders in a high level language as defined
	in the OpenGL Shading Language specification. The language itself is not
	discussed here. A vertex shader replaces the transformation, texture
	coordinate generation and lighting parts of OpenGL, and it also adds
	texture access at the vertex level. Furthermore, management of vertex
	shader objects and loading generic attributes are discussed. A vertex
	shader object, attached to a program object, can be compiled and linked
	to produce an executable that runs on the vertex processor in OpenGL.
	This extension also defines how such an executable interacts with the
	fixed functionality vertex processing of OpenGL 1.4.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/vertex_shader.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_vertex_shader'
GL_VERTEX_SHADER_ARB = constant.Constant( 'GL_VERTEX_SHADER_ARB', 0x8B31 )
GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB = constant.Constant( 'GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB', 0x8B4A )
glget.addGLGetConstant( GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB, (1,) )
GL_MAX_VARYING_FLOATS_ARB = constant.Constant( 'GL_MAX_VARYING_FLOATS_ARB', 0x8B4B )
glget.addGLGetConstant( GL_MAX_VARYING_FLOATS_ARB, (1,) )
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB = constant.Constant( 'GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB', 0x8B4C )
glget.addGLGetConstant( GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB, (1,) )
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB = constant.Constant( 'GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB', 0x8B4D )
glget.addGLGetConstant( GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB, (1,) )
GL_OBJECT_ACTIVE_ATTRIBUTES_ARB = constant.Constant( 'GL_OBJECT_ACTIVE_ATTRIBUTES_ARB', 0x8B89 )
GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB = constant.Constant( 'GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB', 0x8B8A )
glBindAttribLocationARB = platform.createExtensionFunction( 
	'glBindAttribLocationARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLuint, arrays.GLcharARBArray,),
	doc = 'glBindAttribLocationARB( GLhandleARB(programObj), GLuint(index), GLcharARBArray(name) ) -> None',
	argNames = ('programObj', 'index', 'name',),
)

glGetActiveAttribARB = platform.createExtensionFunction( 
	'glGetActiveAttribARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLuint, constants.GLsizei, arrays.GLsizeiArray, arrays.GLintArray, arrays.GLuintArray, arrays.GLcharARBArray,),
	doc = 'glGetActiveAttribARB( GLhandleARB(programObj), GLuint(index), GLsizei(maxLength), GLsizeiArray(length), GLintArray(size), GLuintArray(type), GLcharARBArray(name) ) -> None',
	argNames = ('programObj', 'index', 'maxLength', 'length', 'size', 'type', 'name',),
)

glGetAttribLocationARB = platform.createExtensionFunction( 
	'glGetAttribLocationARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=constants.GLint, 
	argTypes=(constants.GLhandleARB, arrays.GLcharARBArray,),
	doc = 'glGetAttribLocationARB( GLhandleARB(programObj), GLcharARBArray(name) ) -> constants.GLint',
	argNames = ('programObj', 'name',),
)


def glInitVertexShaderARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
