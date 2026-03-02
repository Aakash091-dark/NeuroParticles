import glfw
from OpenGL.GL import *

class Renderer:
    def __init__(self, width, height, particle_system):
        self.ps = particle_system

        if not glfw.init():
            raise Exception("GLFW not initialized")

        self.window = glfw.create_window(width, height, "NeuroParticle Engine", None, None)
        glfw.make_context_current(self.window)

        glPointSize(2)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER,
                     self.ps.positions.nbytes,
                     self.ps.positions,
                     GL_DYNAMIC_DRAW)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0,
                        self.ps.positions.nbytes,
                        self.ps.positions)

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(2, GL_FLOAT, 0, None)

        glColor4f(0.2, 1.0, 1.0, 0.9)
        glDrawArrays(GL_POINTS, 0, self.ps.count)

        glDisableClientState(GL_VERTEX_ARRAY)

        glfw.swap_buffers(self.window)
        glfw.poll_events()

    def should_close(self):
        return glfw.window_should_close(self.window)

    def terminate(self):
        glfw.terminate()
