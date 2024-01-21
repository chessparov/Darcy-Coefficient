# Darcy Coefficient
A program for evaluating the Darcy coefficient given the Reynolds number, the relative roughness and the dimensions of a pipe, factoring also different pipe geometry.

**Coolebrok equation**

Whilst for laminar flow it uses some simple approximated formulae, for turbulent flow the coefficient is calculated through the more complex Coolebrok equation:

$$<math>\frac{1}{\sqrt{\lambda}} = - 2 \log \left( \frac {2{,}51} {Re \, \sqrt{\lambda}} +\frac { \varepsilon/D} {3{,}71}\right)</math>$$

where $\lambda$ is the Darcy coefficient, $Re$ is the Reynolds number, $D$ is the pipe diameter and $\epsilon$ is the relative roughness.

Since it's an implicit equation, it can't be solved analytically, at least in a reasonable time span. The solution is calculated iteratively with the help of the "scipy.optimize.fsolve" function from the scipy library.
