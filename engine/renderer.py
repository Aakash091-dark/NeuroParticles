import glfw
import cv2
from OpenGL.GL import *

class Renderer:
    def __init__(self, width, height, particle_system):
        self.ps = particle_system

        if not glfw.init():
            raise Exception("GLFW not initialized")

        self.window = glfw.create_window(width, height, "NeuroParticle Engine", None, None)
        glfw.make_context_current(self.window)
        glfw.swap_interval(0)  # Disable VSync

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, height, 0, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glClearColor(0.1, 0.1, 0.1, 1)

        glPointSize(2)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER,
                     self.ps.positions.nbytes,
                     self.ps.positions,
                     GL_DYNAMIC_DRAW)

    def render(self, frame):
        glClear(GL_COLOR_BUFFER_BIT)

        # Show camera preview in a separate OpenCV window
        if frame is not None:
            cv2.imshow("Camera Preview", frame)
            cv2.waitKey(1)

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
        cv2.destroyAllWindows()
