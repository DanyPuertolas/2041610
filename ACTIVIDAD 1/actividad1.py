 #EJERCICIO 1    FUNCION MAXIMA DE 2 NUMEROS

def max(num1,num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)
        
max (2,3)





#Ejercicio 2 FUNCION MÁXIMA DE 3 NUMEROS

def max_de_tres(numero1,numero2,numero3):
    if numero1 >= numero2 and numero1 >= numero3:
        return numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        return numero2
    else:
        return numero3

resultado = max_de_tres(4,5,6)
print(resultado)




#EJERCICIO 3 FUNCION QUE CALCULE LA LONGITUD DE UNA LISTA O UNA CADENA DADA 

def longitud_cadena(cadena):
    num_decaracteres = 0
    for caracter in cadena:
        num_decaracteres += 1
    return num_decaracteres
cadena = "Hola mundo"
print("Longitud de la cadena:", longitud_cadena(cadena))





#EJERCICIO 4 FUNCION QUE TOME UN CARACTER Y DEVUELVA TRUE SI ES UNA VOCAL

def vocal(caracter):
    
    vocales = "aeiou"

    return caracter in vocales

print(vocal('b'))




#EJERCICIO 5 FUNCION QUE SUME Y MULTIPLIQUE RESPECTIVAMENTE LOS NUMEROS DE UNA LISTA

def sum(lista_de_numeros):
    suma = 0  
    for numero in lista_de_numeros:
        suma+= numero
    return suma 
resultado = sum([1,2,3,4])
print(resultado)





