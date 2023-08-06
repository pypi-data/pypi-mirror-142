import numpy as np
def sigmoid(k):
  return 1/(1+np.exp(-k))

X = np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
t = np.array([0.95,0.95,0.05,0.05])
W = np.array([0.1,0.1,0.1])

def sigmoid_complete(X,W,t):
  for i in range(X.shape[0]):
     o=sigmoid(X[i].dot(W.T))
     delta_w = 0.1*(t[i]-o)*(o)*(1-o)*X[i]
     W=W+delta_w
  return W

