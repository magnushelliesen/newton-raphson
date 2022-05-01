#####################################
# Written by Magnus Kvåle Helliesen #
#####################################

import numpy as np

def newton_raphson(f, init, **kwargs):
	"""
	TBA
	"""
	
	if 'args' in kwargs:
		args = kwargs['args']
	else:
		args = tuple()
	if 'jac' in kwargs:
		jac = kwargs['jac']
	else:
		print('ERROR: Newton-Raphson requires symbolic Jacobian matrix')
		return {'x': np.array(init), 'fun': np.array(f(init, *args)), 'success': False}
	if 'tol' in kwargs:
		tol = kwargs['tol']
	else:
		tol = 10**-10
	if 'maxiter' in kwargs:
		maxiter = kwargs['maxiter']
	else:
		maxiter = 10
	
	success = True
	x_i = np.array(init)
	f_i = np.array(f(x_i, *args))
	i = 0
	while np.max(np.abs(f_i)) > tol:
		J_i = np.array(jac(x_i.tolist(), *args))
		if i == maxiter:
			success = False
			break
		x_i = x_i-np.matmul(np.linalg.inv(J_i), f_i)
		f_i = np.array(f(x_i.tolist(), *args))
		i+=1
	return {'x': x_i, 'fun': f_i, 'success': success}
