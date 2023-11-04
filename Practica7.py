import numpy as np
#Ejercicio 1

def pertenece1(x : set,y) -> bool:
    for i in range(0,len(x)):
        if x[i] == y:
            return True 
    else:
        return False 
    
def pertenece2(x,y) -> bool:
    n = 0
    while n != len(x):
        if x[n] == y:
            return True 
        n += 1
    else:
        return False  


def pertenece3(x,y) -> bool:
    if x == []:
        return False
    if x[0] == y:
        return True 
    else:
        x.pop(0)
        return pertenece3(x,y)
    
#b 

def dividetodos(x,e):
    if x == []:
        return True 
    if x[0]%e == 0:
        x.pop(0)
        return dividetodos(x,e)
    else:
        return False 
    
def dividetodos2(x,e):
    for i in range(0,len(x)-1):
        if x[i]%e != 0:
            return False
    else:
        return True 
    

def dividetodos3(x,e):
    n = 0 
    while n != len(x):
        if x[n] % e != 0:
            return False
        n += 1 
    else:
        return True 
    
def sumaTotal(x):
    if x == []:
        return 0
    if x != []:
        return x.pop(0) + sumaTotal(x)
    
def sumaTotal2(x):
    n = 0
    for i in range(0,len(x)):
        n += x[i]
    return n 

def ordenados(x):
    for i in range(0,len(x)-1):
        if x[i] > x[i+1]:
            return False 
    else:
        return True

def ordenados1(x):
    if len(x) == 1:
        return True 
    if x[0] <= x[1]:
        x.pop(0)
        return ordenados1(x)
    else:
        return False

def ordenados2(x):
    return sorted(x) == x 

def ordenados3(x):
    if len(x) == 1:
        return True
    if min(x) != x[0]:
        return  False
    else:
        x.pop(0)
        return ordenados3(x)
    
def mayor7(x):
    for i in range(0,len(x)):
        if len(x[i]) > 7:
            return True
    else: 
        return False
    
def palindromo(x):
    for i in range (0,len(x)):
        if x[i] != x [len(x)-i-1]:
            return False
    else:
        return True

def contraseña(x:str):
    if len(x) < 5:
        print("ROJA")
    if 8 < len(x):
        if x.upper() == x or x.lower() == x:
            print("AMARILLO")
        else:
            for i in range(0,10):
                if pertenece1(x,f"{i}"):
                    print("VERDE")
                    break
            else:
                print("AMARILLO")
    elif 5<len(x)<8:
        print("AMARILLO")


def banco(x):
    if x == []:
        return 0
    elif (x[0])[0] == "I":
        return x.pop(0)[1] + banco(x)
    elif (x[0])[0] == "R":
        return -x.pop(0)[1] + banco(x)

print(banco([(10,"I"),(12,"R"),(12,"I")]))
def tresVocales(x):
    n = 0
    vocales = ["a","e","i","o","u"]
    for i in vocales:
        if pertenece1(x,i):
            n += 1
    if n >= 3:
        print(True)
    else:
        print(False)


def chau_pares(x):
    for i in range(0,len(x)):
        if i % 2 == 0:
            x.pop(i)
            x.insert(i,0)
    print(x) 


def chau_pares2(x):
    n = []
    for i in range(0,len(x)):
        if i % 2 == 0:
            n.append(0)
        elif i % 2 != 0:
            n.append(x[i])
    print(n)


def chau_vocales(x):
    palabra = ""
    vocales = ["a","e","i","o","u"]
    vocalesM = ["A","E","I","O","U"]
    for i in range (0,len(x)):
        if not(pertenece1(vocales,x[i])) and not(pertenece1(vocalesM,x[i])):  
            palabra += x[i]
    print(palabra) 


def reemplazo_vocales(x):
    palabra = ""
    vocales = ["a","e","i","o","u"]
    vocalesM = ["A","E","I","O","U"]
    for i in range (0,len(x)):
        if not(pertenece1(vocales,x[i])) and not(pertenece1(vocalesM,x[i])):  
            palabra += x[i]
        else:
            palabra += "-"
    print(palabra) 

def davueltastr(x):
    palabra = ""
    for i in range(0,len(x)):
        palabra += x[len(x)-1-i]
    print(palabra)


def eliminarRepetidos(s):
    palabra = ""
    for i in range(0,len(s)):
        if not(pertenece1(palabra,s[i])):
            palabra += s[i]    
    print(palabra)


def aprobado(x):
    promedio = sum(x)/len(x)
    for i in range(0,len(x)):
        if x[i] < 4 or promedio < 4:
            return 3 
    if promedio < 7:
        return 2 
    else:
        return 1 

def estudiantes():
    x = []
    while not(pertenece1(x,"Listo")):
         estudiante = input("introduzca nombre del estudiante ")
         x.append(estudiante)
    x.remove("Listo")
    print(x)


def subeD():
    historial = {}
    while True:
        operacion = input("Hola! escriba C para cargar, D para descontar y X para salir: ")
        if operacion == "C" or operacion == "D":
            monto = input("indique monto porfavor: ")
            historial[operacion] = monto
        if operacion == "X":
            break
    print(historial)

def subeL():
    historial = [] 
    while True:
        operacion = input("Hola! escriba C para cargar, D para descontar y X para salir: ")
        if operacion == "C" or operacion == "D":
            monto = input("indique monto porfavor: ")
            historial.append((operacion,monto))
        if operacion == "X":
            break
    print(historial)

def perteneceACadaUno(t,s:[[int]]):
    for i in range(0,len(s)):
        if not(pertenece1(t,s[i])):
            return False 
    else:
        return True 
    

def esMatriz(s:[[int]]):
    if s == []:
        return False 
    elif pertenece1([],s):
        return False 
    for i in range(0,len(s)):
        if s[0] != s[i]:
            return False 
    else:
        return True 
    

def filasOrdenadas(s:[[int]]):
    if not(esMatriz(s)):
        return False
    for i in range(0,len(s)):
        if not(ordenados(s[i])):
            return False
    else:
        return True 

#seria algo tipo (s[i])[j]*(s[j])[i]
"""
def filaMatriz(s:list,f:int = 0):
    n = 0
    s2 = [] 
    while n != len(s):
        termino = 0
        for j in range(0,len(s)):
            termino += (s[f])[j]*(s[j])[n]
        s2.append(termino)
        n += 1
    print(s2)
"""
def multiMatriz(s:list):
    s3 = []
    for i in range(0,len(s)):
        s2 = []
        n = 0 
        while n != len(s):
            termino = 0
            for j in range(0,len(s)):
                termino += (s[i])[j]*(s[j])[n]
            s2.append(termino)
            n += 1
        s3.append(s2)
    print(s3)

def elevarMatriz(d,p):
    m = np.random.random((d, d))**2
    while p != 0:
         m = multiMatriz(m)
         p-1
    return m

