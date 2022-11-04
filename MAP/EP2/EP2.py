
import math
import numpy as np

#limite superior de x
def Fb(y):                         

    return eval(fb)
#limite inferior de x
def Fa(y):                          
    
    return eval(fa)
#funcao a ser integrada
def F(x,y, f ):
    
    return eval(f)

#funcao mudanca de variavel
def mudanca_de_base(a,b, t):
    
    return (a+b)/2 + ((b-a)/2 * t)
#calculo de dt
def dt (a,b):

    return (b-a)/2

#quadratura gaussiana para uma integral (sem o calculo de dt para mudanca de base)
def quadratura_gaussiana(n, a, b, x,f):
    
    integral = 0
    
    if int(n) != 6 and int(n) != 8 and int(n) != 10:
        return 0


    elif n == 6:
        for i in range (n):
                integral = integral + F(x,mudanca_de_base(float(a),float(b), x6[i]),f)*w6[i]
    elif n == 8:    
        for i in range (n):
                integral = integral + F(x,mudanca_de_base(float(a),float(b), x8[i]),f)*w8[i]
    elif n == 10:
        for i in range (n):
                integral = integral + F(x,mudanca_de_base(float(a),float(b), x10[i]),f)*w10[i]
                            
    return integral 

#quadratura gaussiana para integral dupla
def quadratura_gaussiana_2d(n, a, b,f):
    
    integral = 0
    if int(n) != 6 and int(n) != 8 and int(n) != 10:
        return 0    
    elif n == 6:
        for i in range (n):
            integral = integral + quadratura_gaussiana(int(n), Fa(mudanca_de_base(float(a),float(b), x6[i])), Fb(mudanca_de_base(float(a),float(b), x6[i])), mudanca_de_base(float(a),float(b), x6[i]),f)*(dt(Fa(mudanca_de_base(float(a),float(b), x6[i])),Fb(mudanca_de_base(float(a),float(b), x6[i]))))*w6[i]
    elif n == 8:
        for i in range (n):
            integral = integral + quadratura_gaussiana(int(n), Fa(mudanca_de_base(float(a),float(b), x8[i])), Fb(mudanca_de_base(float(a),float(b), x8[i])), mudanca_de_base(float(a),float(b), x8[i]),f)*(dt(Fa(mudanca_de_base(float(a),float(b), x8[i])),Fb(mudanca_de_base(float(a),float(b), x8[i]))))*w8[i]
    elif n == 10:
        for i in range (n):
            integral = integral + quadratura_gaussiana(int(n), Fa(mudanca_de_base(float(a),float(b), x10[i])), Fb(mudanca_de_base(float(a),float(b), x10[i])), mudanca_de_base(float(a),float(b), x10[i]),f)*(dt(Fa(mudanca_de_base(float(a),float(b), x10[i])),Fb(mudanca_de_base(float(a),float(b), x10[i]))))*w10[i]        
    
    return integral * dt(float(a),float(b))



#valores dos nos e pesos
global w3 
global x3

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

global fa
global fb


#interface
while int(opcao) != 0:
    print("----------------------DIGITE A OPCAO----------------------")
    print("1 - resultado exempolo 1 ")
    print("2 - resultado exempolo 2 ")
    print("3 - resultado exempolo 3 ")
    print("4 - resultado exempolo 4 ")
    print("5 - Integral dupla dxdy qualquer ")
    print("0 - para sair ")

    opcao = input("Digite sua opcao ")
    if int(opcao) == 5:
        funcao = input("Digite a funcao da inegral dupla dxdy ")
        fa = input("Digite o limite inferior da integral de dentro ")
        fb = input("Digite o limite superior da integral de dentro ")
        a = input("Digite o limite inferior da integral de fora ")
        b = input("Digite o limite superior da integral de fora ")
        print("Resultado para n = 6: ", quadratura_gaussiana_2d(6,a,b,funcao))
        print("Resultado para n = 8: ", quadratura_gaussiana_2d(8,a,b,funcao))
        print("Resultado para n = 10: ", quadratura_gaussiana_2d(10,a,b,funcao))

    if int(opcao) == 1:
        funcao = '1'
        fa = '0'
        fb = '1'
        a =  '0'
        b = '1'
        print("Volume do cubo para n = 6: ", quadratura_gaussiana_2d(6,a,b,funcao))
        print("Volume do cubo para  n = 8: ", quadratura_gaussiana_2d(8,a,b,funcao))
        print("Volume do cubo para n = 10: ", quadratura_gaussiana_2d(10,a,b,funcao))
        funcao = '-x - y + 1'
        fa = '0'
        fb = '-y + 1'
        a =  '0'
        b = '1'
        print("Volume do tetraedro para n = 6: ", quadratura_gaussiana_2d(6,a,b,funcao))
        print("Volume do tetraedro para n = 8: ", quadratura_gaussiana_2d(8,a,b,funcao))
        print("Volume do tetraedro para n = 10: ", quadratura_gaussiana_2d(10,a,b,funcao))
    if int(opcao) == 2:
        funcao = '1'
        fa = '0'
        fb = '1 - y**2'
        a =  '0'
        b = '1'
        print("Resulatado de A dydx para n = 6: ", quadratura_gaussiana_2d(6,a,b,funcao))
        print("Resulatado de A dydx para n = 8: ", quadratura_gaussiana_2d(8,a,b,funcao))
        print("Resulatado de A dydx para n = 10: ", quadratura_gaussiana_2d(10,a,b,funcao))
        funcao = '1'
        fa = '0'
        fb = 'math.sqrt(1 - y)'
        a =  '0'
        b = '1'
        print("Resulatado de A dxdy para n = 6: ", quadratura_gaussiana_2d(6,a,b,funcao))
        print("Resulatado de A dxdy para n = 8: ", quadratura_gaussiana_2d(8,a,b,funcao))
        print("Resulatado de A dxdy para n = 10: ", quadratura_gaussiana_2d(10,a,b,funcao))
    if int(opcao) == 3:
        funcao = 'math.e **(y/x)'
        fa = 'y**3'
        fb = 'y**2'
        a =  '0.1'
        b = '0.5'
        print("Volume da regiao abaixo da superficie para n = 6: ", quadratura_gaussiana_2d(6,a,b,funcao))
        print("Volume da regiao abaixo da superficie para n = 8: ", quadratura_gaussiana_2d(8,a,b,funcao))
        print("Volume da regiao abaixo da superficie para n = 10: ", quadratura_gaussiana_2d(10,a,b,funcao))
        funcao = 'math.sqrt((-(math.e**(y/x)* y)/x**2)**2 + (math.e**(y/x)/x)**2 + 1)'
        fa = 'y**3'
        fb = 'y**2'
        a =  '0.1'
        b = '0.5'
        print("Area da superficie para n = 6: ", quadratura_gaussiana_2d(6,a,b,funcao))
        print("Area da superficie para n = 8: ", quadratura_gaussiana_2d(8,a,b,funcao))
        print("Area da superficie para n = 10: ", quadratura_gaussiana_2d(10,a,b,funcao))
    if int(opcao) == 4:
        funcao = 'y'
        fa = '0'
        fb = 'math.sqrt(1-(y+0.75)**2)'
        a =  '0'
        b = '0.25'
        print("Volume da calota esferica para n = 6: ",  2 * math.pi *  quadratura_gaussiana_2d(6,a,b,funcao))
        print("Volume da calota esferica para n = 8: ",  2 * math.pi *  quadratura_gaussiana_2d(8,a,b,funcao))
        print("Volume da calota esferica para n = 10: ",  2 * math.pi * quadratura_gaussiana_2d(10,a,b,funcao))
        funcao = '2*math.pi*y'
        fa = '0'
        fb = 'math.e**(-y**2)'
        a =  '-1'
        b = '1'
        print("Volume do sólido de rotacao para n = 6: ", quadratura_gaussiana_2d(6,a,b,funcao))
        print("Volume do sólido de rotacao para n = 8: ", quadratura_gaussiana_2d(8,a,b,funcao))
        print("Volume do sólido de rotacao para n = 10: ", quadratura_gaussiana_2d(10,a,b,funcao))

    

  




