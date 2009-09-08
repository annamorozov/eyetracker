'''OpenGL extension NV.pixel_data_range

Overview (from the spec)
	
	The vertex array range extension is intended to improve the
	efficiency of OpenGL vertex arrays.  OpenGL vertex arrays' coherency
	model and ability to access memory from arbitrary locations in memory
	prevented implementations from using DMA (Direct Memory Access)
	operations.
	
	Many image-intensive applications, such as those that use dynamically
	generated textures, face similar problems.  These applications would
	like to be able to sustain throughputs of hundreds of millions of
	pixels per second through DrawPixels and hundreds of millions of
	texels per second through TexSubImage.
	
	However, the same restrictions that limited vertex throughput also
	limit pixel throughput.
	
	By the time that any pixel operation that reads data from user memory
	returns, OpenGL requires that it must be safe for the application to
	start using that memory for a different purpose.  This coherency
	model prevents asynchronous DMA transfers directly out of the user's
	buffer.
	
	There are also no restrictions on the pointer provided to pixel
	operations or on the size of the data.  To facilitate DMA
	implementations, the driver needs to know in advance what region of
	the address space to lock down.
	
	Vertex arrays faced both of these restrictions already, but pixel
	operations have one additional complicating factor -- they are
	bidirectional.  Vertex array data is always being transfered from the
	application to the driver and the HW, whereas pixel operations
	sometimes transfer data to the application from the driver and HW.
	Note that the types of memory that are suitable for DMA for reading
	and writing purposes are often different.  For example, on many PC
	platforms, DMA pulling is best accomplished with write-combined
	(uncached) AGP memory, while pushing data should use cached memory so
	that the application can read the data efficiently once it has been
	read back over the AGP bus.
	
	This extension defines an API where an application can specify two
	pixel data ranges, which are analogous to vertex array ranges, except
	that one is for operations where the application is reading data
	(e.g. glReadPixels) and one is for operations where the application
	is writing data (e.g. glDrawPixels, glTexSubImage2D, etc.).  Each
	pixel data range has a pointer to its start and a length in bytes.
	
	When the pixel data range is enabled, and if the pointer specified
	as the argument to a pixel operation is inside the corresponding
	pixel data range, the implementation may choose to asynchronously
	pull data from the pixel data range or push data to the pixel data
	range.  Data pulled from outside the pixel data range is undefined,
	while pushing data to outside the pixel data range produces undefined
	results.
	
	The application may synchronize with the hardware in one of two ways:
	by flushing the pixel data range (or causing an implicit flush) or by
	using the NV_fence extension to insert fences in the command stream.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/NV/pixel_data_range.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_pixel_data_range'
GL_WRITE_PIXEL_DATA_RANGE_NV = constant.Constant( 'GL_WRITE_PIXEL_DATA_RANGE_NV', 0x8878 )
GL_READ_PIXEL_DATA_RANGE_NV = constant.Constant( 'GL_READ_PIXEL_DATA_RANGE_NV', 0x8879 )
GL_WRITE_PIXEL_DATA_RANGE_LENGTH_NV = constant.Constant( 'GL_WRITE_PIXEL_DATA_RANGE_LENGTH_NV', 0x887A )
glget.addGLGetConstant( GL_WRITE_PIXEL_DATA_RANGE_LENGTH_NV, (1,) )
GL_READ_PIXEL_DATA_RANGE_LENGTH_NV = constant.Constant( 'GL_READ_PIXEL_DATA_RANGE_LENGTH_NV', 0x887B )
glget.addGLGetConstant( GL_READ_PIXEL_DATA_RANGE_LENGTH_NV, (1,) )
GL_WRITE_PIXEL_DATA_RANGE_POINTER_NV = constant.Constant( 'GL_WRITE_PIXEL_DATA_RANGE_POINTER_NV', 0x887C )
GL_READ_PIXEL_DATA_RANGE_POINTER_NV = constant.Constant( 'GL_READ_PIXEL_DATA_RANGE_POINTER_NV', 0x887D )
glPixelDataRangeNV = platform.createExtensionFunction( 
	'glPixelDataRangeNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glPixelDataRangeNV( GLenum(target), GLsizei(length), c_void_p(pointer) ) -> None',
	argNames = ('target', 'length', 'pointer',),
)

glFlushPixelDataRangeNV = platform.createExtensionFunction( 
	'glFlushPixelDataRangeNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum,),
	doc = 'glFlushPixelDataRangeNV( GLenum(target) ) -> None',
	argNames = ('target',),
)


def glInitPixelDataRangeNV():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
