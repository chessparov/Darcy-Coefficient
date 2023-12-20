A simple program for evaluating the Darcy coefficient given the Reynolds number, the relative roughness and the diameter of the pipe.
For laminar flows it uses some simple approximated formulas factoring different pipe geometry, while for turbulent flows the coefficient is calculated through the more complex Coolebrok equation.
Since it's an implicit equation, it can't be solved analytically, at least in a reasonable time span. The solution is calculated iteratively with the help of the "fsolve" function from the scipy.optimize library
