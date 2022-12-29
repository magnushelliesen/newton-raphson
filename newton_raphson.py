import numpy as np


def newton_raphson(f, jac, init, **kwargs):
	"""
	Function that takes a function f and a jacobi matrix jac and finds a root
	"""

	# Check for any kwargs
	if 'args' in kwargs.keys():
		args = kwargs.get('args')
	else:
		args = ()
	if 'tol' in kwargs.keys():
		tol = kwargs.get('tol')
	else:
		tol = 1e-10
	if 'maxiter' in kwargs.keys():
		maxiter = kwargs.get('maxiter')
	else:
		maxiter = 10

	# Initialize loop
	x_i = init
	i = 1
	while True:
		# If maxiter reached, then break with failure
		if i > maxiter:
			success = False
			break

		# Calculate functional value at x_i
		f_i = np.array(f(x_i.tolist(), *args))

		# If function closer to zero than tolerance, then break with success
		if np.max(np.abs(f_i)) <= tol:
			success = True
			break

		# Try to calculate the next iteration, if exception is thrown break with failure
		try:
			x_i = x_i-np.matmul(np.linalg.inv(np.array(jac(x_i.tolist(), *args))), f_i)
			i += 1
		except np.linalg.LinAlgError:
			success = False
			break
	
	return {'x': x_i, 'f': f_i, 'success': success, 'iter': i}