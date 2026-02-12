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


"""
31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista.
Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
"""

def buscar_nombre():
    entrada = input("Ingresa una lista de nombres separados por comas: ") # Pide ingresar una lista de nombres separados por comas
    nombres = [n.strip() for n in entrada.split(",")] # Crea una lista de nombres eliminando los espacios alrededor de cada nombre
    nombre_buscar = input("Ingresa el nombre que deseas buscar: ") # Pide ingresar el nombre que se desea buscar
    
    if nombre_buscar in nombres: # Comprueba si el nombre buscado está en la lista de nombres
        print(f'El nombre {nombre_buscar} está en la lista.')
    else:
        print(f'El nombre {nombre_buscar} no está en la lista.')


"""
32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto
del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
"""

def buscar_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado['nombre'] == nombre_completo: # Comprueba si el nombre del empleado coincide con el nombre buscado
            return empleado['puesto'] # Si se encuentra el empleado
    return 'La persona no trabaja aquí' # Si no se encuentra el empleado


"""
33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
"""

suma_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))


"""
34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco, 
nueva_rama, crecer_ramas, quitar_rama e info_arbol. El objetivo es implementar estos métodos para manipular la estructura del árbol.
Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las 
mismas.
"""

class Arbol:
    def __init__(self):
        # 1. Tronco de longitud 1 y lista vacía de ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # 2. Aumentar longitud del tronco en 1
        self.tronco += 1

    def nueva_rama(self):
        # 3. Agregar una nueva rama de longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # 4. Aumentar en 1 la longitud de todas las ramas
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        # 5. Eliminar una rama en una posición específica (índice humano: 1,2,3...)
        indice = posicion - 1
        if 0 <= indice < len(self.ramas):
            self.ramas.pop(indice)
        else:
            print(f"No existe la rama en la posición {posicion}")

    def info_arbol(self):
        # 6. Devolver información del árbol
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

"""
Caso de uso:
"""

# 1. Crear un árbol.
arbol = Arbol()

# 2. Hacer crecer el tronco del árbol una unidad.
arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol.
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad.
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol.
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2.
arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol.
info = arbol.info_arbol()
print(info)


"""
35. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
"""

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        # 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        # 2. Retirar dinero del saldo del usuario
        if cantidad > self.saldo:
            print("Saldo insuficiente para retirar esa cantidad")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        # 3. Realizar una transferencia desde otro usuario al usuario actual
        if not self.cuenta_corriente or not otro_usuario.cuenta_corriente:
            print("Ambos usuarios deben tener cuenta corriente para realizar la transferencia")
        if cantidad > otro_usuario.saldo:
            print("El otro usuario no tiene suficiente saldo para transferir esa cantidad")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        # 4. Agregar dinero al saldo del usuario
        self.saldo += cantidad

"""
Caso de uso:
"""
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
alicia = UsuarioBanco("Alicia", 100, True)  
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo de "Bob".
bob.agregar_dinero(20)

# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
alicia.transferir_dinero(bob, 80)

# 4. Retirar 50 unidades de saldo a "Alicia".
alicia.retirar_dinero(50)


"""
36. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras,
eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto. 
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva. Tiene que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
4. Crear la función procesar_texto que tome un texto, una opción (entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
"""

# 1. Función para contar el número de veces que aparece cada palabra en el texto
def contar_palabras(texto):
    palabras = texto.split() # Divide el texto en palabras
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1 # Si la palabra ya está en el diccionario, incrementa el contador
        else:
            frecuencia[palabra] = 1 # Si la palabra no está en el diccionario, la añade con un contador de 1
    return frecuencia

# 2. Función para reemplazar una palabra_original del texto por una palabra_nueva
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    palabras = texto.split()
    palabras = [palabra_nueva if p == palabra_original else p for p in palabras]
    return " ".join(palabras)

# 3. Función para eliminar una palabra del texto
def eliminar_palabra(texto, palabra_eliminar):
    palabras = texto.split()
    palabras = [p for p in palabras if p != palabra_eliminar]
    return " ".join(palabras)

# 4. Función procesar_texto que tome un texto, una opción y un número de argumentos variable según la opción indicada
def procesar_texto(texto, opcion, *args):
    # opciones válidas: "contar", "reemplazar", "eliminar"
    
    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        if len(args) != 2:
            return "Error: Para reemplazar se necesitan palabra_original y palabra_nueva."
        palabra_original, palabra_nueva = args
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)

    elif opcion == "eliminar":
        if len(args) != 1:
            return "Error: Para eliminar se necesita solo la palabra a eliminar."
        palabra_eliminar = args[0]
        return eliminar_palabra(texto, palabra_eliminar)

    else:
        return "Opción no válida."

"""
Caso de uso: Comprueba el funcionamiento completo de la función procesar_texto
"""

texto = "hola usuario hola usuario python"

print(procesar_texto(texto, "contar"))

print(procesar_texto(texto, "reemplazar", "usuario", "humano"))

print(procesar_texto(texto, "eliminar", "hola"))


"""
37. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
"""

def determinar_hora():
    try:
        hora = int(input("Introduce la hora (0-23): "))
        if 0 <= hora < 6:
            print("Es de noche.")
        elif 6 <= hora < 12:
            print("Es de día.")
        elif 12 <= hora < 18:
            print("Es de tarde.")
        elif 18 <= hora < 24:
            print("Es de noche.")
        else:
            print("Hora no válida. Debe estar entre 0 y 23.")
    except ValueError:
        print("Por favor, introduce un número válido para la hora.")


"""
38. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
Las reglas de calificación son:
De 0 a 69 insuficiente
De 70 a 79 bien
De 80 a 89 muy bien
De 90 a 100 excelente.
"""

def calificacion_texto(calificacion):
    if 0 <= calificacion < 70:
        return "insuficiente"
    elif 70 <= calificacion < 80:
        return "bien"
    elif 80 <= calificacion < 90:
        return "muy bien"
    elif 90 <= calificacion <= 100:
        return "excelente"
    else:
        return "Calificación no válida. Debe estar entre 0 y 100."


"""
39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y 
datos (una tupla con los datos necesarios para calcular el área de la figura).
"""

import math
def calcular_area(figura, datos):
    if figura == "rectangulo": # Cálculo del área de un rectángulo: área = base * altura
        if len(datos) != 2:
            return "Error: Para un rectángulo se necesitan dos datos (base, altura)."
        base, altura = datos
        return base * altura

    elif figura == "circulo": # Cálculo del área de un círculo: área = Pi * radio^2
        if len(datos) != 1:
            return "Error: Para un círculo se necesita un dato (radio)."
        radio = datos
        return math.pi * radio ** 2

    elif figura == "triangulo": # Cálculo del área de un triángulo: área = (base * altura) / 2
        if len(datos) != 2:
            return "Error: Para un triángulo se necesitan dos datos (base, altura)."
        base, altura = datos
        return (base * altura) / 2

    else: # Si la figura no es válida
        return "Figura no válida. Debe ser 'rectangulo', 'circulo' o 'triangulo'."


"""
40. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una
compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
programa de Python.
"""

def calcular_precio_final():
    try:
        precio_original = float(input("Ingrese el precio original del artículo: ")) # Solicita el precio original del artículo
        tiene_cupon = input("¿Tiene un cupón de descuento? (si/no): ").strip().lower() # Pregunta si tiene un cupón de descuento

        if tiene_cupon == "si": # Si el usuario tiene un cupón de descuento, solicita el valor del cupón
            valor_cupon = float(input("Ingrese el valor del cupón de descuento: "))
            if valor_cupon <= 0: # Verifica que el valor del cupón sea mayor a cero
                print("Valor del cupón no válido. El descuento debe ser mayor a cero.")
            elif valor_cupon > precio_original: # Verifica que el valor del cupón no sea mayor que el precio original
                print("Valor del cupón no válido. El descuento no puede ser mayor que el precio original.")
            else: # Aplica el descuento al precio original del artículo
                precio_final = precio_original - valor_cupon
                print(f"El precio final después de aplicar el descuento es: {precio_final:.2f}€")
        elif tiene_cupon == "no": # Si el usuario no tiene un cupón de descuento, muestra el precio original sin aplicar el descuento
            print(f"El precio final sin aplicar el descuento es: {precio_original:.2f}€")
        else: # Si la respuesta del usuario no es válida, muestra un mensaje de error
            print("Respuesta no válida. Por favor, responda con 'si' o 'no'.")
    except ValueError: # Si el usuario ingresa un valor no numérico para el precio o el valor del cupón, muestra un mensaje de error
        print("Por favor, ingrese un número válido para el precio y el valor del cupón.")
