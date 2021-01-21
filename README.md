# Lisajous Pendulum Simulator
![](oscillation.gif)

### Modelling The Pendulum
![](pendulum_schematic.png)

```theta``` models the oscillation in the z plane.
```
phi = phi0 * cos(omega2 * t) * exp(-alpha * t)
```
![](oscillation_x.gif)

```phi``` models the oscillation in the x plane.
```
theta = theta0 * cos(omega1 * t) * exp(-alpha * t)
```

![](oscillation_z.gif)


```alpha``` is the friction coeficient.

### Installation
```sh
$ pip install vpython
```

