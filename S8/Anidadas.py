# Estructura para rutinas de entrenamiento
rutinas = []

def añadir_registro(nombre, tipo, duracion):
    # Comprobación de tipos y vacíos
    if not nombre or not tipo or not isinstance(duracion, (int, float)):
        raise ValueError("Campos vacíos o tipo incorrecto.")
    # Control de duplicados
    for r in rutinas:
        if r["nombre"] == nombre:
            raise ValueError("Duplicado: ya existe una rutina con ese nombre.")
    # Añadir registro
    registro = {"nombre": nombre, "tipo": tipo, "duracion": duracion}
    rutinas.append(registro)

def buscar_por_campo(campo, valor):
    return [r for r in rutinas if r.get(campo) == valor]

def calcular_media_duracion():
    if not rutinas:
        return 0
    total = sum(r["duracion"] for r in rutinas)
    return total / len(rutinas)

def calcular_maximo_duracion():
    if not rutinas:
        return 0
    return max(r["duracion"] for r in rutinas)

# Ejemplo de uso
try:
    añadir_registro("Piernas", "fuerza", 50)
    añadir_registro("Cardio", "resistencia", 30)
    añadir_registro("Boxeo", "funcional", 40)
except Exception as e:
    print(e)

print(buscar_por_campo("tipo", "fuerza"))           # Busca rutinas de fuerza
print(calcular_media_duracion())                    # Media de duración de rutinas
print(calcular_maximo_duracion())                   # Mayor duración registrada
