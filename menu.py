def mostrar_menu():
    print("1: Agregar libro.")
    print("2: Mostrar libro.")
    print("3: Eliminar libros.")
    print("4: Buscar libro.")
    print("5: Salir.")

def agregar_libro(biblioteca):
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    while True:
        try:
            anio = int(input("Ingrese el año del libro: "))
            break

        except ValueError:
            print("Ingrese un numero valido.")
            continue

    libro = {
        "titulo": titulo,
        "autor": autor,
        "año": anio
    }

    biblioteca.append(libro)
    print("libro cargado con exito.")

def mostrar_libro(biblioteca):
    cont = 0
    if biblioteca:
        for libro in biblioteca:
            cont += 1
            print(f"libro: {cont}")
            print(f"Titulo: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['año']}")
            print(f"-" * 50)
    else:
        print("No hay libros cargados")

def eliminar_libro(biblioteca):
    eliminar = input("Introduzca el titulo del libro a eliminar: ")
    cont = 0
    for libro in biblioteca:
        cont += 1
        if libro["titulo"].lower() == eliminar.lower():
            biblioteca.pop(cont - 1)
            print("Libro eliminado.")
            break
    else:
        print("No se encontro ningun libro con ese titulo.")

def buscar_libro(biblioteca):
    while True:
        nombre = input("Ingrese el nombre del libro a buscar: ")

        if len(nombre.strip()) == 0:
            print("Ingrese un nombre valido.")
            continue
        else:
            break
    for libro in biblioteca:
        if libro["titulo"].lower() == nombre.lower():
            print(f"Titulo: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['año']}")
            print(f"-" * 50)
            break

    else:
        print("No se encuentra libro con ese nombre.")

def principal():
    biblioteca = []
    band1 = False
    while True:
        mostrar_menu()
        try:
            op = int(input("Ingrese una opcion: "))

        except ValueError:
            print("Ingrese un numero.")
            continue

        if 1 > op or op > 5:
            print("Opcion invalida.")
            continue

        if op == 1:
            agregar_libro(biblioteca)
            band1 = True

        elif op == 2 and band1:
            mostrar_libro(biblioteca)


        elif op == 3 and band1:
            eliminar_libro(biblioteca)

        elif op == 4 and band1:
            buscar_libro(biblioteca)

        elif op == 5:
            break

        else:
            print("Primero cargue el libro.")


if __name__ == "__main__":
    principal()