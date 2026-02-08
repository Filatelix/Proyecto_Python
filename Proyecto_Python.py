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
    return numeros * 2

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
    return list(map(str, lista_tupla))


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

def palabras_letra(lista_palabras, letra):
    def empieza_letra(palabra):
        if palabra[0].lower() == letra.lower(): # Comprueba si la palabra empieza por la letra especificada
            return True
        else:
            return False
    return list(filter(empieza_letra, lista_palabras)) # Filtra la lista de palabras que empiezan por la letra especificada


"""
15. Crea una función lambda que sume 3 a cada número de una lista dada.
"""

suma_tres = lambda X: X + 3


"""
16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las
palabras que sean más largas que n. Usa la función filter().
"""

def palabras_longitud(cadena, n):
    palabras = cadena.split() # Divide la cadena en palabras
    
    def es_mas_larga(palabra):
        if len(palabra) > n: # Comprueba si la longitud de la palabra es mayor que n
            return True
        else:
            return False
    return list(filter(es_mas_larga, palabras)) # Filtra la lista de palabras que son más largas que n


"""
17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número
quinientos setenta y dos [572]. Usa la función reduce().
"""

from functools import reduce

def lista_a_numero(lista_digitos):
    return reduce(lambda x, y: x * 10 + y, lista_digitos)


"""
18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación)
y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter().
"""

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificación": 95},
    {"nombre": "Carlos", "edad": 22, "calificación": 85},
    {"nombre": "Elena", "edad": 19, "calificación": 92},
    {"nombre": "David", "edad": 21, "calificación": 78},
    {"nombre": "Fernanda", "edad": 23, "calificación": 97}
]

def calificacion_mayor_90(estudiante):
    
    def calificacion_alta(estudiante):
        if estudiante['calificación'] >= 90: # Comprueba si la calificación del estudiante es mayor o igual a 90
            return True
        else:
            return False
    return list(filter(calificacion_alta, estudiantes)) # Filtra la lista de estudiantes con calificación mayor o igual a 90


"""
19. Crea una función lambda que filtre los números impares de una lista dada.
"""

impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))


"""
20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter().
"""

def filtra_enteros(lista):
    def es_entero(elemento):
        if type(elemento) == int: # Comprueba si el elemento es un entero
            return True
        else:
            return False
    return list(filter(es_entero, lista)) # Filtra la lista para obtener solo los enteros


"""
21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
"""

cubo = lambda x: x ** 3


"""
22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().
"""

from functools import reduce

producto_lista = reduce(lambda x, y: x * y, lista_numeros)


"""
23. Concatena una lista de palabras. Usa la función reduce().
"""

from functools import reduce

lista_concatenada = reduce(lambda x, y: x + ' ' + y, lista_palabras)


"""
24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
"""

from functools import reduce

diferencia_lista = reduce(lambda x, y: x - y, lista_numeros)


"""
25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""

def contador_caracteres(lista_caracteres):
    
    contador = 0
    for caracter in lista_caracteres: # Recorre cada carácter en la lista de caracteres
        contador += 1
    return contador


"""
26. Crea una función lambda que calcule el resto de la división entre dos números dados.
"""

resto_division = lambda x, y: x % y


"""
27. Crea una función que calcule el promedio de una lista de números.
"""

def promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)


"""
28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""

def primer_duplicado(lista):
    vistos = set() # Crea un conjunto para almacenar los elementos vistos
    for elemento in lista:
        if elemento in vistos: # Si el elemento ya ha sido visto, es el primer duplicado
            return elemento
        vistos.add(elemento) # Agrega el elemento al conjunto de vistos
    return False # Si no se encuentra ningún duplicado, devuelve False


"""
29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#',
excepto los últimos cuatro.
"""

def enmascarar_cadena(variable):
    cadena = str(variable)
    if len(cadena) <= 4:
        return cadena
    return '#' * (len(cadena) - 4) + cadena[-4:]


"""
30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
pero en diferente orden.
"""

def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2) # Compara las palabras ordenadas alfabéticamente para determinar si son anagramas

