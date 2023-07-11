'''
La empresa en la que trabajas recibe una gran cantidad de materias primas y otros productos en su inventario, 
los cuales son registrados y manejados en hojas de papel que describen nombres, cantidades, precios, tipos y 
tamaños de cada producto que entra y sale. Recientemente se perdieron algunas hojas y se tomó la decisión de 
digitalizar este proceso. Dado esto, se te pide que desarrolles un programa en Python, en el cual, la persona 
encargada de registrar entradas y salidas de inventarios, mediante la terminal del sistema operativo pueda hacer 
estos registros fácilmente.

La tarea se deberá llevar a cabo utilizando funciones para añadir nuevos artículos, actualizar cantidades y buscar 
artículos específicos basándose en varios criterios. Se deberán utilizar funciones lambda para ordenar el inventario 
en función de diferentes atributos, como ordenar los artículos por nombre, cantidad o precio. Además, se deberán 
emplear funciones anidadas para gestionar operaciones complejas, como generar informes de inventario o calcular el valor 
total del inventario. 

Se deberá subir este archivo de Python a un repositorio Github, junto con un archivo README.md que explique cómo utilizar 
el programa.

Se evaluará el uso de funciones y funciones lambda para agregar (con diferentes datos incluyendo fecha con la paquetería datetime), 
editar, leer, y borrar productos del inventario, que todo funcione correctamente y que contenga el archivo README
'''

import datetime

# Función que añade un nuevo artículo al inventario


def agregar_producto(inventario):
    # Captura de datos del nuevo producto
    # y poder añadirlo al inventario
    nombre = input("Ingrese el nombre del producto: ").lower()
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    tipo = input("Ingrese el tipo del producto: ").lower()
    tamaño = input("Ingrese el tamaño del producto: ")

    # Diccionario con los datos capturados
    nuevo_producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "tipo": tipo,
        "tamaño": tamaño
    }

    # Añadiendo el producto al inventario
    inventario.append(nuevo_producto)

    print("El producto ha sido agregado al inventario.")

# Función que actualiza la cantidad de un artículo existente


def actualizar_cantidad(inventario):
    # Busqueda de un producto existente en el inventario
    # y actualización de su cantidad
    nombre_producto = input("Ingrese el nombre del producto a buscar: ")

    # Busqueda del producto en el inventario
    producto_encontrado = None
    for producto in inventario:
        if producto["nombre"] == nombre_producto:
            producto_encontrado = producto
            break

    # Verificaión del producto en el inventario
    if producto_encontrado is not None:
        # Ingreso de la nueva cantidad del producto
        nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))

        # Actualización de la cantidad del producto encontrado
        producto_encontrado["cantidad"] = nueva_cantidad

        print("La cantidad del producto ha sido actualizada.")
    else:
        print("El producto no se encuentra en el inventario.")

# Función que buscar un artículo específico en el inventario


def buscar_producto(inventario):
    # Busqueda de un producto en el inventario
    # basado en diferentes criterios (nombre, cantidad, precio, etc.)
    criterio = input(
        "Ingrese el criterio de búsqueda (nombre, cantidad, precio, tipo o tamaño): ").lower()
    valor_buscado = input("Ingrese el valor a buscar: ")

    # Buscar el producto en el inventario basado en el criterio seleccionado
    productos_encontrados = []
    for producto in inventario:
        if producto[criterio] == valor_buscado:
            productos_encontrados.append(producto)

    # Verificacion si se encontraron productos
    if len(productos_encontrados) > 0:
        print("Productos encontrados:")
        for producto in productos_encontrados:
            print(producto)
    else:
        print("No se encontraron productos que cumplan el criterio de búsqueda.")

# Funcion que borra un producto especifico del inventario

def eliminar_producto(inventario):
    # Busqueda de un producto en el inventario
    # para su eliminacion del listado
    nombre_producto = input("Ingrese el nombre del producto que desea eliminar del inventario: ").lower()

    # Busqueda del producto en el inventario
    producto_encontrado = None
    for producto in inventario:
        if producto["nombre"] == nombre_producto:
            producto_encontrado = producto
            break

    if producto_encontrado is not None:
        inventario.remove(producto_encontrado)
        print(f"El producto {producto_encontrado} fue eliminado del inventario")


# Función que ordenar el inventario en función de diferentes atributos


def ordenar_inventario(inventario):
    # Ordenar el inventario con funciones lambda
    atributo = input(
        "Ingrese el atributo por el cual desea ordenar el inventario (nombre, cantidad, precio, tipo o tamaño): ").lower()

    # Ordenar el inventario utilizando una función lambda como clave de ordenamiento
    inventario.sort(key=lambda producto: producto[atributo])

    # Mostrar el inventario ordenado
    print("Inventario ordenado:")
    for producto in inventario:
        print(producto)

# Función que generar un informe de inventario


def generar_informe(inventario):
    # Genenerador del informe de inventario con todos los productos
    print("Informe de inventario:")
    print("---------------------")
    for producto in inventario:
        print("Nombre:", producto["nombre"])
        print("Cantidad:", producto["cantidad"])
        print("Precio:", producto["precio"])
        print("Tipo:", producto["tipo"])
        print("Tamaño:", producto["tamaño"])
        print("---------------------")

# Función que calcular el valor total del inventario


def calcular_valor_total(inventario):
    # Calculadora del valor total del inventario
    total = 0
    for producto in inventario:
        total += producto["cantidad"] * producto["precio"]

    print("Valor total del inventario:", total)

# Función principal del programa


def main():
    inventario = []  # Lista que almacenará los productos del inventario

    while True:
        # Solicitud de entradas en el inventario por parte del usuario
        opcion = input("Bien venido al sistema de inventarios, aquí podrás seleccionar la o las acciones necesarias para el control del inventario. \n\n Opción 1: Agregar un nuevo producto. \n\n Opción 2: Actualizar el inventario disponible. \n\n Opción 3: Búsqueda de productos en el inventario, puede buscarlo por los siguientes criterios, nombre, cantidad, precio, tipo o tamaño. \n\n Opción 4: Eliminar un producto del inventario, podrá seleccionar por nombre el producto que desea eliminar. \n\n Opción 5: Ordenar el inventario según su atributo, nombre, cantidad, precio, tipo o tamaño. \n\n Opción 6: Generar informe de inventario. \n\n Opción 7: Calcular el valor total del Inventario. \n\n Opción 8: Salir del programa. \n\n Elija una opción => ")

        # Llamar a la función correspondiente en base a la opción seleccionada
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            actualizar_cantidad(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            eliminar_producto(inventario)
        elif opcion == "5":
            ordenar_inventario(inventario)
        elif opcion == "6":
            generar_informe(inventario)
        elif opcion == "7":
            calcular_valor_total(inventario)           
        elif opcion == "8":
            break  # Salir del programa


# Llamar a la función principal del programa
if __name__ == "__main__":
    main()
