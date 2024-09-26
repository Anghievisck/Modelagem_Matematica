import numpy as np
import matplotlib.pyplot as plt

def PseudoAngle(x, y):
    return 1 - np.dot(x,y)/(np.linalg.norm(x) * np.linalg.norm(y))

def next(id,P,dir):
  V = P - P[id,:]
  n = len(V)
  A = np.zeros((n,1))
  for i in range(n):
    if i != id:
      A[i] = PseudoAngle(V[i,:],dir)
  A[id] = 2.1 # inf
  return np.argmin(A)

def jarvis_hull(P):
  CH = []
  n = len(P)
  ymin = np.argmin(P[:,1])
  CH.append(ymin)
  dir = np.array([1,0])
  CH.append(next(ymin,P,dir))
  while CH[-1] != CH[0]:
    dir = P[CH[-1],:] - P[CH[-2],:]
    CH.append(next(CH[-1],P,dir))
  return CH

n = 100
P = np.random.rand(n,2)

for i in range(n):
  P[i, 0] *= 100
  P[i, 1] *= 100

idx = jarvis_hull(P)

plt.plot(P[idx,0],P[idx,1],"#000000")
plt.scatter(P[:,0],P[:,1])
plt.show()