import math
import numpy as np


def F(x, f ):
    
    return eval(f)


def mudanca_de_base(a,b, t):
    
    return (a+b)/2 + ((b-a)/2 * t)
#calculo de dt
def dt (a,b):

    return (b-a)/2

#quadratura gaussiana para uma integral 
def quadratura_gaussiana(n, a, b,f):
    
    integral = 0
    
    if int(n) != 6 and int(n) != 8 and int(n) != 10:
        return 0
    elif n == 6:
        for i in range (n):
                integral = integral + F(mudanca_de_base(float(a),float(b), x6[i]),f)*w6[i]
    elif n == 8:    
        for i in range (n):
                integral = integral + F(mudanca_de_base(float(a),float(b), x8[i]),f)*w8[i]
    elif n == 10:
        for i in range (n):
                integral = integral + F(mudanca_de_base(float(a),float(b), x10[i]),f)*w10[i]
                            
    return integral * dt(float(a),float(b))


def Fi_i(i,n, pos):
    h = 1/(n+1)
    xi = i*h
    if int(pos) == 0:
        #SOBE
        return str( "(x - {})/{}".format(xi,h)) 
    elif int(pos) == 1: 
        #DESCE
        return str( "({} - x)/{}".format(xi,h))
    else:
        return 0

def Derivada_Fi_i(n, pos):
    if pos == 0:
        #SOBE
        return n + 1
    elif pos == 1:
        #DESCE
        return - (n + 1)
    else:
        return 0

#retorna valor da diagonal da matriz tridiagonal


def Vetor_DiagonalttLU(n,k,q,l,f,mod):#MOD 0 = diognal inferior MOD = 1 digonal principal MOD = 2 diagonal superior
    h = l/(n+1)
    Q1 = np.zeros(n)
    Q2 = np.zeros(n+1)
    Q3 = np.zeros(n+1)
    Q4 = np.zeros(n+2)
    Q5 = np.zeros(n+1)
    Q6 = np.zeros(n+1)
    
    for i in range (0,n):
        xi = (i)*h
        xim1 = (i-1)*h
        xiM1 = (i+1)*h
        Q1[i] = (1/h)**2 *  quadratura_gaussiana(10,xi , xiM1,str("({} - x)* (x - {})* {}".format(xiM1,xi,q)))
    for i in range (0,n+1):
        xi = (i)*h
        xim1 = (i-1)*h
        Q2[i] = (1/h)**2 * quadratura_gaussiana(10,xim1 , xi,str("(x - {})**2*({})".format(xim1, q)))
    for i in range (0,n+1):
        xi = (i)*h
        xiM1 = (i+1)*h
        Q3[i] = (1/h)**2 * quadratura_gaussiana(10,xi , xiM1,str("({} - x)**2*({})".format(xiM1, q))) 
    for i in range (0,n+2):
        xi = (i)*h
        xim1 = (i-1)*h
        Q4[i] = (1/h )**2 * quadratura_gaussiana(10,xim1 , xi,str(k))
    for i in range (0,n+1):
        xi = (i)*h
        xim1 = (i-1)*h
        Q5[i] = (1/h )* quadratura_gaussiana(10,xim1 , xi,str(" (x - {})* ({})".format(xim1,f)))
    for i in range (0,n+1):
        xi = (i)*h
        xiM1 = (i+1)*h
        Q6[i] =( 1/h )* quadratura_gaussiana(10,xi , xiM1,str("({} - x)* ({})".format(xiM1,f)))


    if mod == 0:
        a = np.zeros(n)
        a[0] = 0
        for i in range(1,n):
            a[i] = -Q4[i+1] + Q1[i]
        return a
    if mod == 1:
        b = np.zeros(n)
        for i in range(0,n):
            b[i] = Q4[i+1] + Q4[i+2] + Q2[i+1] + Q3[i+1]
        return b
    if mod == 2:
        c = np.zeros(n)
        c[c.size-1] = 0
        for i in range(0,n-1):
            c[i] = -Q4[i+2] + Q1[i+1]
        return c
    if mod == 3:
        d = np.zeros(n)
        for i in range(0,n):
            d[i] = Q5[i+1] + Q6[i+1]
        return d

def Vetor_DiagonalttLU_NH(n,k,q,l,f,mod):#MOD 0 = diognal inferior MOD = 1 digonal principal MOD = 2 diagonal superior
    h = l/(n+1)
    Q1 = np.zeros(n)
    Q2 = np.zeros(n+1)
    Q3 = np.zeros(n+1)
    Q4 = np.zeros(n+2)
    Q5 = np.zeros(n+1)
    Q6 = np.zeros(n+1)
    
    for i in range (0,n):
        xi = (i)*h
        xim1 = (i-1)*h
        xiM1 = (i+1)*h
        Q1[i] = (1/h)**2 *  quadratura_gaussiana(10,xi , xiM1,str("({} - x)* (x - {})* {}".format(xiM1,xi,q)))
    for i in range (0,n+1):
        xi = (i)*h
        xim1 = (i-1)*h
        Q2[i] = (1/h)**2 * quadratura_gaussiana(10,xim1 , xi,str("(x - {})**2*({})".format(xim1, q)))
    for i in range (0,n+1):
        xi = (i)*h
        xiM1 = (i+1)*h
        Q3[i] = (1/h)**2 * quadratura_gaussiana(10,xi , xiM1,str("({} - x)**2*({})".format(xiM1, q))) 
    for i in range (0,n+2):
        xi = (i)*h
        xim1 = (i-1)*h
        Q4[i] = (1/h )**2 * quadratura_gaussiana(10,xim1 , xi,str(k))
    for i in range (0,n+1):
        xi = (i)*h
        xim1 = (i-1)*h
        Q5[i] = (1/h )* quadratura_gaussiana(10,xim1 , xi,str(" (x - {})* ({})".format(xim1,f)))
    for i in range (0,n+1):
        xi = (i)*h
        xiM1 = (i+1)*h
        Q6[i] =( 1/h )* quadratura_gaussiana(10,xi , xiM1,str("({} - x)* ({})".format(xiM1,f)))



    if mod == 0:
        a = np.zeros(n)
        a[0] = 0
        for i in range(1,n):
            a[i] = -Q4[i+1] + Q1[i]
        return a
    if mod == 1:
        b = np.zeros(n)
        for i in range(0,n):
            b[i] = Q4[i+1] + Q4[i+2] + Q2[i+1] + Q3[i+1]
        return b
    if mod == 2:
        c = np.zeros(n)
        c[c.size-1] = 0
        for i in range(0,n-1):
            c[i] = -Q4[i+2] + Q1[i+1]
        return c
    if mod == 3:
        d = np.zeros(n)
        for i in range(0,n):
            d[i] = Q5[i+1] + Q6[i+1]
        return d    

def n_homogenio(k,q,f,a,b):
    f_= str("{} + ({} - {})*{} - ({} * ({} + ({} - {})*x))".format(f,b,a,k,q,a,b,a)) 
    return f_

def testeciclico(a1, c1):
    
        return 1
  

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


def Fx(x,f):
    return eval(f)

def funcao_teste(n,a,l):
    s = np.zeros(n)
    h = l/(n+1)
    for i in range (n):
        xi = h*(i+1)
        s[i] = Fx(xi,a)
    return s
global w3 
global x3

def fh(n,l):
    s = np.zeros(n)
    h = l/(n+1)
    for i in range (n):
        s[i] =  h*(i+1)
    return s

w3 = np.array([0.888889, 0.555556, 0.555556])
x3 = np.array([0, 0.774597, -0.774597])


global w6
global x6

w6 = np.array([0.4679139345726910473898703, 0.4679139345726910473898703, 0.3607615730481386075698335, 0.3607615730481386075698335, 0.1713244923791703450402961, 0.1713244923791703450402961])
x6 = np.array([0.2386191860831969086305017, -0.2386191860831969086305017, 0.6612093864662645136613996, -0.6612093864662645136613996, 0.9324695142031520278123016, -0.9324695142031520278123016])

global w8
global x8

w8 = np.array([0.3626837833783619829651504, 0.3626837833783619829651504, 0.3137066458778872873379622, 0.3137066458778872873379622, 0.2223810344533744705443560, 0.2223810344533744705443560, 0.1012285362903762591525314, 0.1012285362903762591525314])
x8 = np.array([0.1834346424956498049394761, -0.1834346424956498049394761, 0.5255324099163289858177390, -0.5255324099163289858177390, 0.7966664774136267395915539, -0.7966664774136267395915539, 0.9602898564975362316835609, -0.9602898564975362316835609])

global w10
global x10

w10 = np.array([0.2955242247147528701738930, 0.2955242247147528701738930, 0.2692667193099963550912269, 0.2692667193099963550912269, 0.2190863625159820439955349, 0.2190863625159820439955349, 0.1494513491505805931457763, 0.1494513491505805931457763, 0.0666713443086881375935688, 0.0666713443086881375935688])
x10 = np.array([0.1488743389816312108848260, -0.1488743389816312108848260, 0.4333953941292471907992659, -0.4333953941292471907992659, 0.6794095682990244062343274, -0.6794095682990244062343274, 0.8650633666889845107320967, -0.8650633666889845107320967, 0.9739065285171717200779640, -0.9739065285171717200779640])

opcao = 10

while int(opcao) != 0:
    print("----------------------DIGITE A OPCAO----------------------")
    print("1 - Validacao 1 ")
    print("2 - Validacao 2 ")
    print("3 - solucao para L(u(x)) := (-k(x)u(x)')' + q(x)u(x) = f(x) no intervalo L")
    print("4 - Equilibrio com forcantes de calor")
    print("0 - para sair ")
    opcao = input("Digite sua opcao ")
    if int(opcao) == 1:
        n = input("Digite valor de n: ")
        print("Solucao pelo método")
        print(triangularSL(Vetor_DiagonalttLU(int(n),1,0,1,"12*x*(1-x) - 2",0),Vetor_DiagonalttLU(int(n),1,0,1,"12*x*(1-x) - 2",1),Vetor_DiagonalttLU(int(n),1,0,1,"12*x*(1-x) -2 ",2),Vetor_DiagonalttLU(int(n),1,0,1,"12*x*(1-x) - 2",3),int(n)))
        print("Solucao exata: ")
        print(funcao_teste(int(n),"x**2*(1 - x)**2",1))
    if int(opcao) == 2:
        n = input("Digite valor de n: ")
        print("Solucao pelo método")
        print( triangularSL(Vetor_DiagonalttLU(int(n),"math.e**x",0,1,"math.e**x + 1",0),Vetor_DiagonalttLU(int(n),"math.e**x",0,1,"math.e**x + 1",1),Vetor_DiagonalttLU(int(n),"math.e**x",0,1,"math.e**x + 1",2),Vetor_DiagonalttLU(int(n),"math.e**x",0,1,"math.e**x + 1",3),int(n)))
        print("Solucao exata: ")
        print(funcao_teste(int(n),"(x-1)*(math.e**-x -1)",1))
    if int(opcao) == 3:
        print("condicoes de froteira: ")
        a = int(input("Digite valor de u(0) "))
        b = int(input("Digite valor de u(1) "))
        l = int(input("Digite o intervalo [0,L] "))
        k = input("Digite o valor de k(x) ")
        q = input("Digite o valor de q(x) ")
        f = input("Digite o valor de f(x) ")
        n = int(input("Digite valor de n "))
        f_ = n_homogenio(k,q,f,a,b)
        print(triangularSL(Vetor_DiagonalttLU(int(n),k,q,l,f_,0),Vetor_DiagonalttLU(int(n),k,q,l,f_,1),Vetor_DiagonalttLU(int(n),k,q,l,f_,2),Vetor_DiagonalttLU(int(n),k,q,l,f_,3),int(n)))
    if int(opcao) == 4:
        n = input("Digite valor de n ")
        print("Aquecimento do chip: ")
        Q0a = int(input("\nCalor maximo gerado pelo chip "))
        sigma = int(input("Valor de Sigma "))
        l = int(input("tamanho do chip "))
        print("--------------------------------------------------")
        print("resfriamento do chip: ")
        Q0r = int(input("\nconstate de resfiramento do chip "))
        teta = int(input("Teta de resfiramnto ")) 
        print("--------------------------------------------------")
        k = 30
        q = 0
        f_ = "{}*(math.e**(-((x- {}/2)**2/{}**2)))".format(Q0a,l,sigma)
        fr = "{}*(math.e**(-((x- {}/2)**2/{}**2)))".format(Q0r,l,teta)
        frb = "{}*((math.e**-((x)**2/({}**2)) + math.e**(-(x- {}/2)**2/{}**2)))".format(Q0r,teta,l,teta)
        Q1 = triangularSL(Vetor_DiagonalttLU(int(n),k,q,l,f_,0),Vetor_DiagonalttLU(int(n),k,q,l,f_,1),Vetor_DiagonalttLU(int(n),k,q,l,f_,2),Vetor_DiagonalttLU(int(n),k,q,l,f_,3),int(n)) - Q0r
        Q2 = triangularSL(Vetor_DiagonalttLU(int(n),k,q,l,f_,0),Vetor_DiagonalttLU(int(n),k,q,l,f_,1),Vetor_DiagonalttLU(int(n),k,q,l,f_,2),Vetor_DiagonalttLU(int(n),k,q,l,f_,3),int(n)) - triangularSL(Vetor_DiagonalttLU(int(n),k,q,l,fr,0),Vetor_DiagonalttLU(int(n),k,q,l,fr,1),Vetor_DiagonalttLU(int(n),k,q,l,fr,2),Vetor_DiagonalttLU(int(n),k,q,l,fr,3),int(n))
        Q3 = triangularSL(Vetor_DiagonalttLU(int(n),k,q,l,f_,0),Vetor_DiagonalttLU(int(n),k,q,l,f_,1),Vetor_DiagonalttLU(int(n),k,q,l,f_,2),Vetor_DiagonalttLU(int(n),k,q,l,f_,3),int(n)) - triangularSL(Vetor_DiagonalttLU(int(n),k,q,l,frb,0),Vetor_DiagonalttLU(int(n),k,q,l,frb,1),Vetor_DiagonalttLU(int(n),k,q,l,frb,2),Vetor_DiagonalttLU(int(n),k,q,l,frb,3),int(n)) 
        print("1 - Resfriamento constate\n", Q1)
        print("2 - Resfriamento analogo ao aquecimento\n", Q2)
        print("3 - Resfriamento mais intenso nos extremos\n", Q3)
        if int(opcao) == 0:
            opcao = 0
            

