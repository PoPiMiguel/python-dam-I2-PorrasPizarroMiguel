import random
import datetime

def generar_nombre():
    """
    Genera un nombre aleatorio para el personaje combinando sílabas.
    """
    silabas = ["ka", "ra", "an", "el", "so", "mi", "la", "ve", "to", "di"]
    nombre = ""
    longitud = random.randint(2, 4)
    for _ in range(longitud):
        nombre += random.choice(silabas).capitalize()
    return nombre

def generar_atributos():
    """
    Genera atributos del personaje usando números aleatorios.
    Retorna un diccionario con fuerza, agilidad e inteligencia entre 1 y 10.
    """
    atributos = {
        "fuerza": random.randint(1, 10),
        "agilidad": random.randint(1, 10),
        "inteligencia": random.randint(1, 10)
    }
    return atributos

def crear_personaje(nombre_usuario):
    """
    Crea un personaje completo validando la entrada del usuario para el nombre,
    generando un nombre aleatorio si es incorrecto.
    Retorna un diccionario con nombre, atributos y fecha de creación.
    """
    try:
        # Validación sencilla: nombre de usuario no vacío y con letras solo
        if not nombre_usuario.isalpha():
            raise ValueError("El nombre debe contener solo letras y no estar vacío.")
        nombre = nombre_usuario.capitalize()
    except Exception as e:
        print(f"Error en nombre de usuario: {e}. Se generará un nombre aleatorio.")
        nombre = generar_nombre()

    atributos = generar_atributos()
    fecha_creacion = datetime.datetime.now()

    personaje = {
        "nombre": nombre,
        "atributos": atributos,
        "fecha_creacion": fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
    }

    return personaje

def main():
    """
    Función principal para interactuar con el usuario y mostrar
    los datos del personaje creado.
    """
    nombre_usuario = input("Introduce el nombre de tu personaje: ")
    personaje = crear_personaje(nombre_usuario)

    print("\nPersonaje generado:")
    print(f"Nombre: {personaje['nombre']}")
    print(f"Atributos:")
    for attr, valor in personaje['atributos'].items():
        print(f"  {attr.capitalize()}: {valor}")
    print(f"Creado el: {personaje['fecha_creacion']}")

if __name__ == "__main__":
    main()
