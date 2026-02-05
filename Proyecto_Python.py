"""
1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
de cada letra en la cadena. Los espacios no deben ser considerados.
"""

def frecuencias(cadena):
    dic_letras = {}
    for letra in cadena:
        if letra != ' ': # Ignorar los espacios
            if letra in dic_letras:
                dic_letras[letra] += 1 # Si la letra ya está en el diccionario, incrementa el contador
            else:
                dic_letras[letra] = 1 # Si la letra no está en el diccionario, la añade con un contador de 1
    return dic_letras


"""
2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def duplica(numeros):
    return numeros * 2 # La función multiplica el número por 2

resultado = map(duplica, numeros)


"""
3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe 
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
"""

def lista_inlcuidas(lista_palabras, palabra_objetivo):
    resultado = []
    for palabra in lista_palabras:
        if palabra_objetivo in palabra: # Comprueba si la palabra objetivo está en la palabra actual
            resultado.append(palabra) # Si se cumple la condición, se añade la palabra a la lista de resultados
    return resultado


"""
4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

"""

def diferencia(x, y):
    return x - y

resultado = map(diferencia, lista1, lista2)


"""
5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
una tupla que contenga la media y el estado.
"""

def evaluacion(lista_notas, aprobado=5):
    media = sum(lista_notas) / len(lista_notas) # Cálculo de la nota media
    if media >= aprobado: # Comprueba si la media es mayor o igual al aprobado
        estado = 'aprobado'
    else:
        estado = 'suspenso'
    return media, estado # Devuelve una tupla con la media y el estado


"""
6. Escribe una función que calcule el factorial de un número de manera recursiva.
"""

def factorial(n):
    if n == 0 or n == 1: # El factorial de 0 u de 1 es 1
        return 1
    else:
        return n * factorial(n - 1) # Calculo del factorial


"""
7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
"""

def tuplas_a_strings(lista_tupla):
    return list(map(str, lista_tupla)) # Convierte cada tupla a string y devuelve una lista


"""
8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
indicando si la división fue exitosa o no.
"""

def division():
    try:
        num1 = float(input('Dame el primer número: '))
        num2 = float(input('Dame el segundo número: '))
        resultado = num1 / num2
        print(f'El resultado de la división es: {resultado}')
    
    except ValueError:
        print('Debes introducir un número válido') # Si el usuario introduce un valor no numérico
    
    except ZeroDivisionError:
        print('No se puede dividir por cero') # Si el usuario intenta dividir por cero
    
    else:
        print('La división se realizó con éxito') # Si la división se realiza sin errores

division()


"""
9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas
mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
Usa la función filter().
"""

def filtro_mascotas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    def mascota_permitida(mascota):
        return mascota not in mascotas_prohibidas # Devuelve True si la mascota no está en la lista de mascotas prohibidas
    
    return list(filter(mascota_permitida, lista_mascotas)) # Filtra la lista de mascotas permitidas


"""
10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción
personalizada y maneja el error adecuadamente.
"""

def promedio(lista_numeros):
    if len(lista_numeros) == 0:
        print('La lista está vacía y no se puede calcular el promedio') # Si la lista está vacía muestra un mensaje de error
    else:
        return sum(lista_numeros) / len(lista_numeros) # Calcula el promedio


"""
11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera
del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
"""

def edad_usuario():
    try:
        edad = int(input('Introduce tu edad: '))
        if edad < 0 or edad > 120:
            print('La edad debe estar entre 0 y 120 años') # Si la edad introducida está fuera del rango
        else:
            print(f'Tu edad es: {edad}')
    
    except ValueError:
        print('Debes introducir un número válido') # Si el usuario introduce un valor no numérico


"""
12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map().
"""

def longitud_palabras(frase):
    palabras = frase.split() # Divide la frase en palabras
    return list(map(len, palabras)) # Devuelve una lista con la longitud de cada palabra


"""
13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y
minúsculas. Las letras no pueden estar repetidas. Usa la función map().
"""

def mayus_minus(caracteres):
    unicas = []
    for c in caracteres:
        if c not in unicas:
            unicas.append(c) # Añade el carácter a la lista unicas si no está repetido
    
    caracteres_may = list(map(str.upper, unicas)) # Convierte cada carácter a mayúscula
    caracteres_min = list(map(str.lower, unicas)) # Convierte cada caracter a minúscula

    return list(zip(caracteres_may, caracteres_min)) # Devuelve una lista con las letras en mayúsculas y minúsculas como tuplas


"""
14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la 
función filter().
"""

