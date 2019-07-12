"""
Author: Esther Hung             Date: 12/07/2019

Solving d^2(psi)/dx^2 = f(x) * psi from x0 to x1 with boundary condition
psi(x0) = psi_0 and d(psi(x_0))/dx = dpsi_0
Input: 
    f: The function to be called on the right hand side of the equation
    x: array of the integration, the first element is the lower bound, x0, and the last element is the upper bound, x1.
    psi0: the value of \psi at x0, i.e. \psi(x0)
    dpsi0: the value of \psi derivative at x0, i.e. d\psi(x0)/dx
Output:
    psi: array of values of \psi with each element in the array corresponding to the same element in x


solutions of Schrodinger’s equation by numerical integration


find numerical solutions to the time-independent Schrodinger equation for ¨
the quantum harmonic oscillator. This problem illustrates the solution of a stiff differential equation.

we can try boundary conditions x_0 = 0 and x_1 = 23402394


We want to solve d^2\phi/dx^2 = f(x_hat)* phi

Program takes 4 inputs:

\delta :
\x_hat_1:
\n :
\ E hat:
"""
