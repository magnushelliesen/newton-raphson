# newton-raphson
Routine that calculates roots using simple [multivariate Newton-Raphson method](https://github.com/magnushelliesen/newton-raphson/blob/main/newton_raphson/newton_raphson.py). The input and output is similar to scipy.optimize root. Example of use is

```python
from newton_raphson.newton_raphson import newton_raphson

def f(x):
    return [x[0]**3-1, x[1]*2]

def jac(x):
    return [[3*x[0]**2, 0], [0, 2*x[1]]]

newton_raphson(f, [1,2], jac=jac)
```

Which returns {'x': [1.0, 0.0], 'fun': [0.0, 0.0], 'success': True, 'status': 0}

The function takes the following arguments:
- **func** is the objective function
- **jac** is a function that returns the Jacobian matrix of the objective function
- **x0** is an array with initial values
- **args** (optional) is a tuple with arguments
- **tol** (optional) is the tolerance level
- **maxiter** (optional) is the maximum number of iterations
- **solution** is a dictionary containing
  - *'x'* the value from the last iteration
  - *'fun'* the objective function value from the last iteration
  - *'success'* a boolean indication whether the solution converged or not

solution is a dictionary with keys *'x'* which is an array with the last iteration, *'fun'* which is an array with the function value from the last iteration, and *'success'* which is a boolean indicating whether the solution converged.

The method is the simple Newton-Raphson algoithm, where the i+1'st iteration is given by

![Figure](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;x_{i+1}=x_i-J(x_i,z)^{-1}f(x_i,z),)

where x and f is a vector and vector funciton (the objective function) and J is the Jacobian matrix. The method runs until the maximum of the absolute values of the objective function is less than or equal to tol, or **maxiter** is reached.
