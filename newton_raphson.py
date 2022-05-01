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
      print('ERROR: Newton-Raphson require symbolic Jacobian matrix')
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
  iter = np.array(init)
  i = 0
  while np.max(np.abs(np.array(f(iter, *args)))) > tol:
      if i == maxiter:
          success = False
          break
      iter = np.array(iter)-np.matmul(np.linalg.inv(jac(iter, *args)), np.array(f(iter, *args)))
      i+=1
  return {'x': iter, 'fun': np.array(f(iter, *args)), 'success': success}
