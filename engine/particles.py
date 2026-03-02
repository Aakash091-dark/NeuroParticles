import numpy as np

class ParticleSystem:
    def __init__(self, width, height, count=10000):
        self.width = width
        self.height = height
        self.count = count

        self.positions = np.random.rand(count, 2).astype(np.float32)
        self.positions[:, 0] *= width
        self.positions[:, 1] *= height

        self.velocities = np.zeros((count, 2), dtype=np.float32)
        self.shape_targets = None

    def update(self, target, mode):
        if mode == "shape" and self.shape_targets is not None:
            direction = self.shape_targets - self.positions
            self.velocities += direction * 0.0005

        elif target is not None:
            direction = target - self.positions
            dist = np.linalg.norm(direction, axis=1).reshape(-1, 1) + 0.1
            norm = direction / dist

            if mode == "attract":
                self.velocities += norm * 0.5
            elif mode == "repel":
                self.velocities -= norm * 0.8

        self.velocities *= 0.95
        self.positions += self.velocities
