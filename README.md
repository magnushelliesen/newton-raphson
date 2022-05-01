# newton-raphson
Routine that calculates roots using simple multivariate Newton-Raphson method. The input and output is similar to scipy.optimize root. Example of use is

solution = newton_raphson(function, [initial values], args=tuple (optional), jac=jacobian, tol=float (optional))

solution is a dictionary with keys 'x' which is an array with the last iteration, 'fun' which is an array with the function value from the last iteration, and 'success' which is a boolean indicating whether the solution converged.
