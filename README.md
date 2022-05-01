# newton-raphson
Routine that calculates roots using simple multivariate Newton-Raphson method. The input and output is similar to scipy.optimize root. Example of use is

```python
  solution = newton_raphson(func, x0, args=(), jac=jacobian, tol=10**-10, maxiter=10)
```

Where
- func is the objective function
- x0 is an array with initial values
- args (optional) is a tuple with arguments
- jac is a function that returns the Jacobian matrix of the objective function
- tol (optional) is the tolerance level
- maxiter (optional) is the maximum number of iterations
- solution is a dictionary containing
  - 'x' the value from the last iteration
  - 'fun' the objective function value from the last iteration
  - 'success' a boolean indication whether the solution converged or not

solution is a dictionary with keys 'x' which is an array with the last iteration, 'fun' which is an array with the function value from the last iteration, and 'success' which is a boolean indicating whether the solution converged.

The method is the simple Newton-Raphson algoithm, where the i+1'st iteration is given by

![Figure](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;x_{i+1}=x_i-J(x_i,z)f(x_i,z),)

where x and f are vectors and J is a matrix. The method runs until the maximum of the absolute values of the objective function is less than or equal to tol, or maxiter is reached.
