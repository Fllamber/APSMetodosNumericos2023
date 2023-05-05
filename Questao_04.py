# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np
#from numpy import linalg as LA
#import matplotlib.pyplot as plt
#import scipy.linalg as la

# Compute the eigenvalues of a general matrix.
# A função la.eig retorna o par (autovalor, autovetor), nesta ordem. Note que os autovalores em
# geral são números complexos que no Python tem a extensão j. Já os autovetores virão em seguida
# na forma de vetores.
A = np.array([[3, 2, 7], [2, 5, 7], [7, 1, 8]])
print()
print("Matriz Pedida: ")
print('A=', A)
autovalor, autovetor = np.linalg.eig(A)
# autvals, autvecs = la.eig(A)
print()
# eigenvalues - autovalor
print("Autovalor")
print(autovalor)
print()
# eigvecs - autovetores
print("Autovetor")
print(autovetor)
print()
print("SVD", "Singular value decomposition", "Decomposição em valores singulares")
u, s, vh = np.linalg.svd(A)
print(u)
print()
print(s)
print()
print(vh)
