
# NeuroParticle Engine

An interactive real-time particle simulation engine controlled using hand gestures.
The system uses computer vision to track hand movements and dynamically manipulate thousands of particles rendered with OpenGL.

## Overview

NeuroParticle Engine combines  **computer vision** ,  **GPU-accelerated rendering** , and **vectorized physics simulation** to create an interactive visual system.
Using a webcam, the application detects hand gestures and applies forces to a large particle field in real time.

The project demonstrates how AI-based gesture recognition can be integrated with graphics systems to create natural human–computer interaction.

---

## Features

* Real-time **hand gesture detection**
* **10,000+ particles** rendered using OpenGL
* Interactive physics-based particle motion
* Multiple gesture-controlled modes
* Camera feed visualization
* Modular architecture for easy extension

### Gesture Controls

| Gesture          | Action                          |
| ---------------- | ------------------------------- |
| ✊ Closed Fist   | Repel particles outward         |
| ☝ One Finger    | Attract particles to hand       |
| ✌ Two Fingers   | Arrange particles into a circle |
| 🤟 Three Fingers | Arrange particles into a square |

---

## Project Structure

```
neuroparticle/
│
├── assets/                # Future shaders, textures, configs
│
├── engine/
│   ├── particles.py       # Particle physics system
│   ├── renderer.py        # OpenGL rendering engine
│   └── shapes.py          # Shape generation logic
│
├── vision/
│   └── hand_tracker.py    # MediaPipe hand tracking
│
├── main.py                # Main application loop
├── requirements.txt       # Project dependencies
└── README.md
```

---

## Technologies Used

* **Python**
* **OpenGL (PyOpenGL)** – GPU particle rendering
* **GLFW** – Window and OpenGL context
* **NumPy** – Vectorized physics calculations
* **OpenCV** – Camera capture
* **MediaPipe** – Hand gesture recognition

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/neuroparticle-engine.git
cd neuroparticle-engine
```

### 2. Create a virtual environment (recommended)

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

```
python main.py
```

Make sure your webcam is connected and accessible.

---

## How It Works

1. The webcam captures frames in real time.
2. MediaPipe detects hand landmarks and identifies gestures.
3. The index finger position is converted into screen coordinates.
4. A vectorized physics engine updates particle positions.
5. OpenGL renders the particle system each frame.

This pipeline runs continuously to produce an interactive visual system.

---

## Possible Improvements

Future enhancements may include:

* GPU-based particle physics using shaders
* Support for **100k+ particles**
* Particle glow and shader effects
* Custom shape generation from images
* Audio-reactive particle behavior
* Multi-hand interaction

---

## License

This project is released under the [Apache-2.0 license](https://github.com/Aakash091-dark/NeuroParticles?tab=Apache-2.0-1-ov-file#).

---

## Author

Aakash Sehrawat
Computer Science Engineer | AI & Data Science Enthusiast
