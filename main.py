from engine.particles import ParticleSystem
from engine.renderer import Renderer
from engine.shapes import circle, square
from vision.hand_tracker import HandTracker

WIDTH, HEIGHT = 1200, 800

ps = ParticleSystem(WIDTH, HEIGHT, 10000)
renderer = Renderer(WIDTH, HEIGHT, ps)
tracker = HandTracker(WIDTH, HEIGHT)

mode = "attract"

while not renderer.should_close():
    target, fingers, frame = tracker.get_hand_data()

    if fingers == 0:
        mode = "repel"
    elif fingers == 1:
        mode = "attract"
    elif fingers == 2:
        ps.shape_targets = circle(ps.count, WIDTH, HEIGHT)
        mode = "shape"
    elif fingers == 3:
        ps.shape_targets = square(ps.count, WIDTH, HEIGHT)
        mode = "shape"

    ps.update(target, mode)
    renderer.render(frame)

renderer.terminate()
