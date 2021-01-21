'''
Credits to VPython team and their documentation: https://vpython.org/contents/docs/
'''
from vpython import *

scene.width = scene.height = 600
scene.range = 1.8
scene.title = "Lisajous Pendulum"

def display_instructions():
    s = """In GlowScript programs:
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
    scene.caption = s

# Display text below the 3D graphics
display_instructions()

# --- Pendulum Properties ---
H1 = 15
H2 = 20

support_length = 30
support_pad = support_length * 0.2
ball_radius = 0.8

# Starting conditions
theta0 = 0
omega1 = 1.7  

phi0 = 0
omega2 = 2

# Friction coefficient
alpha = 0.01

# Simulation refresh rate
dt = 0.0002
t = 0

# --- Static drawing ---

support_origin = vec(0, H1 + H2, 0)

support = box(
    pos = support_origin,
    size = vec(support_length + support_pad, support_pad/10, support_pad/10),
    color = vector(0.5, 0.5, 0.5)
)

anchor1 = sphere(
    pos = support_origin + vec(-support_length/2, 0, 0),
    radius = ball_radius,
    color = vec(0.7, 0.7, 0.7))

anchor2 = sphere(
    pos = support_origin + vec(support_length/2, 0, 0),
    radius = ball_radius,
    color = vec(0.7, 0.7, 0.7))

ball1 = sphere(
    pos = support_origin + vec(0, -H1, 0),
    radius = ball_radius,
    color = vec(0.7, 0.7, 0.7))

ball2 = sphere(
    pos = support_origin + vec(0, -(H1 + H2), 0),
    radius = ball_radius * 1.5,
    color = vec(1, 1, 1),
)

string1 = cylinder(
    pos = anchor1.pos,
    axis = ball1.pos - anchor1.pos, 
    radius = ball_radius * 0.3,
    color = vec(0.4, 0.4, 0.4))

string2 = cylinder(
    pos = anchor2.pos,
    axis = ball1.pos - anchor2.pos, 
    radius = ball_radius * 0.3,
    color = vec(0.4, 0.4, 0.4))

string3 = cylinder(
    pos = ball1.pos,
    axis = ball2.pos - ball1.pos, 
    radius = ball_radius * 0.3,
    color = vec(0.4, 0.4, 0.4))

drawer = None

# --- Dynamics ---

theta = theta0
phi = phi0

while True:
    rate(1/dt) 

    # Aplying the general oscialtion equation
    theta = theta0 * cos(omega1 * t) * exp(-alpha * t)
    phi = phi0 * cos(omega2 * t) * exp(-alpha * t)
    
    # Position delta for the first ball
    dx1 = 0
    dy1 = -H1 * cos(theta)
    dz1 = H1 * sin(theta)
    ball1.pos = support_origin + vec(dx1, dy1, dz1)

    # Rotation of the first 2 strings
    string1.axis = ball1.pos - anchor1.pos
    string2.axis = ball1.pos - anchor2.pos
    
    # Position delta for the second ball
    dx2 = H2 * sin(phi)
    dy2 = dy1 - H2 * cos(phi) * cos(theta)
    dz2 = (H1 + H2) * sin(theta)
    ball2.pos = support_origin + vec(dx2, dy2, dz2)

    # Rotation for the third string
    string3.pos = ball1.pos
    string3.axis = ball2.pos - ball1.pos
    
    # Drawer leaves off the pattern

    
    if drawer == None:
        drawer = sphere(
            pos = vec(ball2.pos.x, -1, ball2.pos.z),
            radius = 0.01,
            color = vec(1, 0, 0),
            make_trail=True)
    else:
        drawer.pos = vec(ball2.pos.x, -1, ball2.pos.z)
    
    t += dt
