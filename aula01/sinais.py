def impulso(n):
    d = 1*(n==0)
    return d

def degrau(n):
    d = 1*(n>=0)
    return d

def retangulo(n,N):
    d = 1*(np.abs(n) <= N)
    return d