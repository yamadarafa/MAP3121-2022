
import math
import numpy as np

def testeciclico(a1, c1):
    
    if a1[0] == 0 or c1[c1.size - 1] == 0:
        return  0
    else: 
        return 1


def decomposicaoLU(M, n):
    global L
    L = np.identity(n)
    U = np.zeros((n,n))
   
    for i in range(0,n):
        U[0][i] = M[0][i]

    for i in range(1,n):
        L[i][0] = M[i][0]/U[0][0]


    for i in range(1,n):
        U[i, i : n] = M[i, i : n] - np.dot(L[i, 0 : (i)],U[0:i, i : n])
        if i < n-1:
            L[(i + 1) : n, i] =  1/U[i,i] * (M[(i + 1) : n, i] - np.dot(L[(i + 1) : n, 0: i] , U[0 : i, i]))

    return U

def decomposicaotridiagonalLU(a1, b1, c1):

    global v
    global w
    global lv
    global uv
    global lc
    global uc
    global cv

    lv = np.zeros(b1.size)
    uv = np.zeros(b1.size)
    cv = np.zeros(b1.size)
    
    for i in range (0, b1.size): 
        cv[i] = c1[i]

    uv[0]= b1[0]
             
    for i in range(1, b1.size):
        lv[i] = a1[i]/uv[i-1]
        uv[i] = b1[i] - (lv[i]*c1[i-1])
    
    if testeciclico(a1,c1) == 1:
        
        lc = np.zeros(b1.size -1)
        uc = np.zeros(b1.size -1)
        cc = np.zeros(b1.size - 1)
        w = np.zeros(b1.size - 1)
        v = np.zeros(b1.size - 1)

        v[0] = a1[0]
        v[v.size - 1] = c1[c1.size - 2]
        w[0] = c1[c1.size - 1]
        w[w.size - 1] = a1[a1.size - 1]
    
        for i in range (0, b1.size - 1): 
            cc[i] = c1[i]

        uc[0]= b1[0]

        for i in range(1, b1.size - 1):
            lc[i] = a1[i]/uc[i-1]
            uc[i] = b1[i] - (lc[i]*c1[i-1])
   
        return cc
    return cv
            
def solucaoSL(l, u, d, p, n): 
    
    x = np.zeros(n)
    y = np.zeros(n)
    y[0] = d[0]

    for i in range(1, n):
        y[i] = d[i] - l[i]*y[i-1]
    
    x[n-1] = y[n-1]/u[n-1]

    for i in range(0, n-1):
        x[n - 2 - i] = (y[n - 2 - i] - p[n - 2 - i]*x[n - 1 - i])/u[n - 2 - i]
    
    return x

def SolucaoXn (d, w, y, b, z):

    x = (d[d.size - 1] - ( w[0] * y[0] ) - (w[w.size - 1] * y[y.size - 1]))/(b[b.size - 1] - (w[0] * z[0]) - (w[w.size - 1]  * z[z.size - 1]))
    return x

def SolucaoX (y, xn, z, n):

    xx = np.zeros(n)
    xx[n - 1] = xn
    x = y - np.dot(xn, z)
    
    for i in range (n - 1):
        xx[i] = x[i]

    return xx

def testeA (n): 
    
    at = np.zeros(n)

    for i in range (0, n - 1):
        at[i] = (2 * (i + 1) - 1 )/(4* (i + 1))

    at[n - 1] = (2 * n - 1)/(2 * n)

    return at

def testeB (n): 
    
    bt = np.zeros(n)

    for i in range (0, n):
        bt[i] = 2

    return bt

def testeC (n, ai): 
    ct = np.zeros(n)

    for i in range (0, n):
        ct[i] = 1 - ai[i]

    return ct

def testeD (n):
    d = np.zeros(n)

    for i in range(0,n): 
        d[i] = math.cos(2 * math.pi * (i + 1)**2/(n**2))

    return d


def triangularSL(a1, b1, c1, d, n):
    
    cn = np.zeros(n - 1)
    y = np.zeros(n)
    z = np.zeros(n - 1)
    x = np.zeros(n)
    y = np.zeros(n - 1)

    if testeciclico(a1,c1) == 0:
        cn = decomposicaotridiagonalLU(a1,b1,c1)
        y = solucaoSL(lv,uv,d,cn, n )
        return y
    
    cn = decomposicaotridiagonalLU(a1,b1,c1)
    y = solucaoSL(lv,uv,d,cn, n - 1)
    z = solucaoSL(lv, uv, v, cn, n - 1)
    xn = SolucaoXn(d,w,y,b1,z)
    x = SolucaoX(y, xn, z, n)
    return x



opcao = 1

while int (opcao) != 5:   
    print("\n1 - Decompor matriz M que eh triangularizavel pelo Metodo de Gauss sem trocas de linhas em LU  ")
    print("2 - Decompor matriz tridiagonal M em LU " )
    print("3 - Resolver sistema linear tridiagonal ")  
    print("4 - Rodar teste de sistema linear tridiagonal ciclico sugerido no enunciado ")
    print("5 - sair \n")
    opcao = input ("Digite sua opcao ")
    if int(opcao) > 5 or int(opcao) < 1:
        print("\n------------ OPCAO INVALIDA ------------")
    if int(opcao) == 1:
        print("------------ OPCAO 1 ------------")
        n = int(input("\nDigite o tamanho da matriz: "))
        M = np.zeros((n,n))
        for i in range(int(n)):
            for j in range(int(n)):
                M[i][j] = input("Elemento da linha %d , coluna %d : " %(i+1,j+1))
        print("A decomposicao da matriz M  = \n", M)
        print("U = \n", decomposicaoLU(M, n))
        print("L = \n", L)

    if int(opcao) == 2:
        print("------------ OPCAO 2 ------------")
        n = int(input("\nDigite o tamanho da matriz: "))
        a = np.zeros(n)
        b = np.zeros(n)
        c = np.zeros(n)
        for i in range(int(n)):
            a[i] = input("digite %do. valor de a " %(i+1))
        for i in range(int(n)):
            b[i] = input("digite %do. valor de b " %(i+1))
        for i in range(int(n)):
            c[i] = input("digite %do. valor de c " %(i+1))
        decomposicaotridiagonalLU(a, b, c)
        print("decomposicao LU da matriz tridiagona M = \n")
        print("L = \n", lv)
        print("U = \n", uv)
    if int(opcao) == 3:
        print("------------ OPCAO 3 ------------")
        n = int(input("\nDigite o tamanho da matriz: "))
        a = np.zeros(n)
        b = np.zeros(n)
        c = np.zeros(n)
        d = np.zeros(n)
        for i in range(int(n)):
            a[i] = input("digite %do. valor de a " %(i+1))
        for i in range(int(n)):
            b[i] = input("digite %do. valor de b " %(i+1))
        for i in range(int(n)):
            c[i] = input("digite %do. valor de c " %(i+1))
        for i in range(int(n)):
            d[i] = input("digite %do. valor de d " %(i+1))
        decomposicaotridiagonalLU(a, b, c)
        if testeciclico(a,c) == 1:
            print("sistema tridiagonal eh ciclico")
            print("solucao = ",triangularSL(a,b,c,d,n))
        print("\nSistema tridiagonal nao eh ciclico")
        print("solucao = ",triangularSL(a,b,c,d,n))
    if int(opcao) == 4:
        print("------------ OPCAO 4 ------------")
        n = input("\nDigite o tamanho da matriz (sugestao do enunciado n = 20): ")
        print("Vetor A = ", testeA(int(n)))
        print("Vetor B = ", testeB(int(n)))
        print("Vetor C = ", testeC(int(n), testeA(int(n))))
        print("Vetor D = ", testeD(int(n)))
        print("solucao = ",triangularSL(testeA(int(n)),testeB(int(n)),testeC(int(n), testeA(int(n))),testeD(int(n)),int(n)))
          
print("fim do progama ")

#print("aaa == ", triangularSL(testeA(20),testeB(20),testeC(20, testeA(20)),testeD(20),20))



#print("SL = ", solucaoSL(lv, uv, d, triangularvet(b1,a1,c1), b1.size -1))




#print(solucaoSL(l,u,d,c, 4))
#triangulaciclica(G,5,d)

#print(v)
#print(w)



