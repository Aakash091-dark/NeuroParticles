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
                force = 1000 / (dist + 10)
                self.velocities += norm * force * 0.01
            elif mode == "repel":
                force = 1000 / (dist + 10)
                self.velocities -= norm * force * 0.01

        self.velocities *= 0.95
        self.positions += self.velocities

        # Bounce off walls
        self.positions[:, 0] = np.clip(self.positions[:, 0], 0, self.width)
        self.positions[:, 1] = np.clip(self.positions[:, 1], 0, self.height)

        # Reverse velocity if hitting wall
        hit_x_low = self.positions[:, 0] <= 0
        hit_x_high = self.positions[:, 0] >= self.width
        hit_y_low = self.positions[:, 1] <= 0
        hit_y_high = self.positions[:, 1] >= self.height

        self.velocities[hit_x_low | hit_x_high, 0] *= -0.8
        self.velocities[hit_y_low | hit_y_high, 1] *= -0.8
