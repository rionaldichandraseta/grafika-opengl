from OpenGL.GL.shaders import *

def getFileContents(filename):
        return open(filename, 'r').read()

class Shader(object):
    def __init__(self, vertex_path, fragment_path):
        vertex_shader = compileShader(getFileContents(vertex_path))
        fragment_shader = compileShader(getFileContents(fragment_path))
        self._program_ID = glCreateProgram()
        glAttachShader(self._program_ID, vertex_shader)
        glAttachShader(self._program_ID, fragment_shader)
        glLinkProgram(ID)

        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)
    
    def use(self):
        glUseProgram(self._program_ID)

    def setBool(self, name, val):
        glUniform1i(glGetUniformLocation(self._program_ID, name), int(val))

    def setInt(self, name, val):
        glUniform1i(glGetUniformLocation(self._program_ID, name), val)

    def setFloat(self, name, val):
        glUniform1f(glGetUniformLocation(self._program_ID, name), val)