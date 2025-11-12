def programa():
    try:
        alumnos = []
        n = input("¿Cuántos alumnos? ")
        
        # Validación: n debe ser un número entero positivo
        # Esto evita que se ingresen valores no numéricos o negativos
        if not n.isdigit() or int(n) <= 0:
            raise ValueError("Debe ingresar un número entero positivo para el número de alumnos.")
        n = int(n)

        for _ in range(n):
            nota = input("Nota: ")
            
            # Validación: nota debe ser un número entero
            # Controla que no se ingresen cadenas u otros tipos inválidos
            if not nota.isdigit():
                raise ValueError("La nota debe ser un número entero.")
            nota = int(nota)
            
            # Validación de rango válido para nota entre 0 y 10
            if nota < 0 or nota > 10:
                raise ValueError("La nota debe estar entre 0 y 10.")
            
            # Se añade la nota a la lista usando append para modificar la lista original
            alumnos.append(nota)

        # Control para evitar división por cero si la lista está vacía
        if len(alumnos) == 0:
            raise ZeroDivisionError("No se pueden calcular estadísticas con lista vacía.")

        # Cálculo de la media usando función modularizada para facilitar mantenimiento
        media = calcular_media(alumnos)
        print("Media:", media)

        # Mostrar las notas aprobadas usando función separada para mejor organización
        print("Aprobados:")
        mostrar_aprobados(alumnos)

    except ValueError as ve:
        # Captura errores de tipo y validación para dar mensajes claros al usuario
        print(f"Error de valor: {ve}")
    except ZeroDivisionError as zde:
        # Captura error matemático de división por cero en caso que ocurra
        print(f"Error matemático: {zde}")

def calcular_media(lista):
    # Función que calcula la media aritmética de una lista de números
    return sum(lista) / len(lista)

def mostrar_aprobados(lista):
    # Función que imprime las notas que son iguales o mayores a 5
    for nota in lista:
        if nota >= 5:
            print(nota)

# Este bloque asegura que programa() solo se ejecute si corremos este archivo directamente
if __name__ == "__main__":
    programa()
