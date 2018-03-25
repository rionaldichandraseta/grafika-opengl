import ctypes
import numpy
import pygame
import time

from OpenGL.GL import *
from OpenGL.GL.shaders import *
from pygame.locals import *  

width = 640
height = 480

def getFileContents(filename):
    return open(filename, 'r').read()

def init():
    vertexShader = compileShader(getFileContents("data/shaders/triangle.vert"), GL_VERTEX_SHADER)
    fragmentShader = compileShader(getFileContents("data/shaders/triangle.frag"), GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)
    
    # Set Clear Color
    glClearColor(0.3, 0.3, 0.3, 1.0)
    return program

def drawImage(program, image):
    # Define Vertice List
    # X Y Z R G B
    vertices = numpy.array([0.0, 0.5, 0.0, 1.0, 0.0, 0.0,
                           -0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                            0.5, -0.5, 0.0, 0.0, 0.0, 1.0], numpy.float32)    
    
    # Bind Attribute
    glBindAttribLocation(program, 0, "vPosition")
    glBindAttribLocation(program, 1, "color")

    # Generate Buffers and Bind Buffers
    VBO = glGenBuffers(len(image))
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    for i in range(len(image)):
        vertices = numpy.array([],numpy.float32)
        for j in range(1,len(image[i])):
            vertices = numpy.append(vertices,image[i][j])
            vertices = numpy.append(vertices,image[i][0])
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW) # Copy data to buffer

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_TRUE, 24, ctypes.c_void_p(0))
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)

    # Draw and Run
    glViewport(0, 0, width, height)
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(program)

    for i in range(len(image)):
        glBindVertexArray(VAO)
        glBindBuffer(GL_ARRAY_BUFFER, VBO+i)
        glDrawArrays(GL_TRIANGLES, 0, len(image[i]))

    pygame.display.flip()

def draw(image):
    pygame.init()
    pygame.display.set_mode((width, height), HWSURFACE|OPENGL|DOUBLEBUF)

    program = init()

    running = True
    while running:
        drawImage(program,image)
        events = pygame.event.get()

        # wait for exit
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    running = False


if __name__ == '__main__':
    draw_triangle()
