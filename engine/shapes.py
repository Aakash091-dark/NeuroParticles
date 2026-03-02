import numpy as np

def circle(count, width, height):
    center = np.array([width/2, height/2])
    radius = 250
    angles = np.linspace(0, 2*np.pi, count)

    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)

    return np.column_stack((x, y))

def square(count, width, height):
    targets = np.zeros((count, 2), dtype=np.float32)
    size = 400
    start = np.array([width/2 - size/2, height/2 - size/2])

    for i in range(count):
        side = i % 4
        t = (i / count) * size

        if side == 0:
            targets[i] = [start[0] + t, start[1]]
        elif side == 1:
            targets[i] = [start[0] + size, start[1] + t]
        elif side == 2:
            targets[i] = [start[0] + size - t, start[1] + size]
        else:
            targets[i] = [start[0], start[1] + size - t]

    return targets
