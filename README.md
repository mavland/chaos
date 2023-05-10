# chaos
Chaos codes, currently including a model of the Malkus chaotic waterwheel and the general form of the Lorenz equations. Supports a parameter sweep through several variables including step size, Prandtl number, Rayleigh number, and unnamed parameter b. 

Entering - into the Rayleigh number box will result in the program calculating a Rayleigh number based on the other parameters to support stable fixed points in the plot.

Entries in N MUST be integer values. There cannot be a decimal valued step number.

One of the models must be chosen for the program to return a plot.

Notes on interesting parameter options:

-Setting the initial position to the origin will result in no motion.
-For a Rayleigh number greater than 24.74, the plot exhibits the characteristics of a strange attractor due to the subcritical Hopf bifurcation that occurs here. For Rayleigh numbers greater than 1 and less than this, there should exist two stable fixed points in the system.
