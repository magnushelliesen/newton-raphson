import numpy as np


def nr(f, init, args=None, jac=None, tol=10**-7, maxiter=10):
	if args is None:
		args = tuple()
	if jac is None:
		raise ValueError('Symbolic Jacobian must be specified')
	
	success = True
	status = 0
	x_i = init
	f_i = np.array(f(init.tolist(), *args))
	i = 0
	while np.max(np.abs(f_i)) > 0:
		if i == maxiter:
			success = False
			status = 1
			break
		try:
			x_i_new = x_i-np.matmul(np.linalg.inv(np.array(jac(x_i.tolist(), *args))), f_i)
			if np.max(np.abs(x_i_new-x_i)) <= tol:
				break
			x_i = x_i_new
		except np.linalg.LinAlgError:
			success = False
			status = 2
			break
		f_i = np.array(f(x_i, *args))
		i += 1

	return {'x': x_i, 'fun': f_i, 'success': success, 'status': status}
