# Lisajous Pendulum Simulator
![](oscillation.gif =250x)

### Modelling The Pendulum
![](pendulum_schematic.png =250x)

```theta``` models the oscillation in the z plane.
```
phi = phi0 * cos(omega2 * t) * exp(-alpha * t)
```
![](oscillation_x.gif =250x)

```phi``` models the oscillation in the x plane.
```
theta = theta0 * cos(omega1 * t) * exp(-alpha * t)
```

![](oscillation_z.gif= 250x)


```alpha``` is the friction coeficient.

### Installation
```sh
$ pip install vpython
```

