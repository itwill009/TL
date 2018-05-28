from random import *
import sys

def freivald(X, Y, Z, k) :
     
    r = [0] * k     
    for i in range(k) :
        r[i] = (randrange(2))

    Zr = [0] * k
     
    for i in range(k) :
        for j in range(k) :
            Zr[i] = Zr[i] + Z[i][j] * r[j]
    
    XZr = [0] * k
    for i in range(k) :
        for j in range(k) :
            XZr[i] = XZr[i] + X[i][j] * Zr[j]
    
    Yr = [0] * k
    
    for i in range(k) :
        for j in range(k) :
            Yr[i] = Yr[i] + Y[i][j] * r[j]
            
    for i in range(k) :
        if (XZr[i] - Yr[i] != 0) :
            return False
    
    return True


def isProduct(X, Y, R, loop_cnt, k) :
     
    for i in range(loop_cnt) :
        if (freivald(X, Y, R, k) == False) :
            return False
    return True


def value_input_method(lines):
    n,m,k = list(map(int,lines.pop(0).split()))
    X, Y, R = [], [] ,[]
        
    # X element input part
    for _ in range(k):
        X.append(list(map(int,lines.pop(0).split())))
    # Y element input part
    for _ in range(k):
        Y.append(list(map(int,lines.pop(0).split())))
    # R element input part
    for _ in range(n):
        R.append(list(map(int,lines.pop(0).split())))
        
    return X, Y, R, k

lines = sys.stdin.readlines()
        
t = int(lines.pop(0))
for _ in range(t):
    
    X,Y,R,k = value_input_method(lines)
    loop_cnt = 2**k

    answer = 0
    
    for i in range(len(R)-k+1):
        for j in range(len(R[0])-k+1):
            Rp = []
            for p in R[i:i+k]:
                Rp.append(p[j:j+k])
                
            if(isProduct(X, Y, Rp, loop_cnt , k)):
                answer += 1
                
    print(answer)
            