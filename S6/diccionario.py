# Gestor sencillo de miembros para un gimnasio
# Características:
# - Insertar, modificar y eliminar registros (CRUD)
# - Calcular métricas: media de cuota mensual, suma de cuotas, máximo de sesiones/semana
# - Recorrer claves y valores con un bucle for
# - Adaptación personalizada: sugerir plan según edad y sesiones/semana
# No usa librerías externas ni funciones externas.

# Datos iniciales: diccionario donde la clave es el ID del socio
members = {
    "M001": {"nombre": "Ana",   "edad": 28, "cuota": 35.0, "sesiones_sem": 3},
    "M002": {"nombre": "Luis",  "edad": 42, "cuota": 45.0, "sesiones_sem": 2},
    "M003": {"nombre": "Carmen","edad": 55, "cuota": 30.0, "sesiones_sem": 1},
}

#Esta función es necesaria ya que se usa varias veces y no es buena idea repetir codigo
def mostrar_miembro(id_):
    if id_ in members:
        m = members[id_]
        print(f"{id_} -> Nombre: {m['nombre']}, Edad: {m['edad']}, Cuota: {m['cuota']}€, Ses/sem: {m['sesiones_sem']}")
    else:
        print("No existe un miembro con ese ID.")

# Menú principal (usa input para interactuar)
while True:
    print("\n--- GIMNASIO: Gestor de miembros ---")
    print("1) Insertar socio")
    print("2) Modificar socio")
    print("3) Eliminar socio")
    print("4) Mostrar todos los socios")
    print("5) Calcular métricas")
    print("6) Aplicar adaptación personalizada (sugerir plan)")
    print("7) Salir")
    opcion = input("Elige una opción (1-7): ").strip()

    if opcion == "1":
        # Insertar
        nid = input("ID nuevo (ej. M004): ").strip()
        if nid in members:
            print("Ese ID ya existe. Usa modificar si quieres cambiar datos.")
        else:
            nombre = input("Nombre: ").strip()
            edad = int(input("Edad: ").strip())
            cuota = float(input("Cuota mensual (€): ").strip())
            sesiones = int(input("Sesiones/semana previstas: ").strip())
            members[nid] = {"nombre": nombre, "edad": edad, "cuota": cuota, "sesiones_sem": sesiones}
            print("Socio insertado correctamente.")
            mostrar_miembro(nid)

    elif opcion == "2":
        # Modificar
        mid = input("ID del socio a modificar: ").strip()
        if mid not in members:
            print("No existe ese socio.")
        else:
            print("Dejar en blanco para no cambiar el campo.")
            cur = members[mid]
            nombre = input(f"Nombre [{cur['nombre']}]: ").strip()
            edad = input(f"Edad [{cur['edad']}]: ").strip()
            cuota = input(f"Cuota [{cur['cuota']}]: ").strip()
            sesiones = input(f"Sesiones/semana [{cur['sesiones_sem']}]: ").strip()
            if nombre:
                cur['nombre'] = nombre
            if edad:
                cur['edad'] = int(edad)
            if cuota:
                cur['cuota'] = float(cuota)
            if sesiones:
                cur['sesiones_sem'] = int(sesiones)
            print("Socio modificado:")
            mostrar_miembro(mid)

    elif opcion == "3":
        # Eliminar
        eid = input("ID del socio a eliminar: ").strip()
        if eid in members:
            print("Eliminando socio:", eid, members[eid]['nombre'])
            del members[eid]
            print("Socio eliminado.")
        else:
            print("No existe ese socio.")

    elif opcion == "4":
        # Mostrar todos: aquí se recorre claves y valores con for
        if not members:
            print("No hay socios registrados.")
        else:
            print("\nLista de socios (ID -> datos):")
            for member_id, datos in members.items():
                # Ejemplo de uso del bucle for para claves y valores
                print(f"- {member_id}: Nombre={datos['nombre']}, Edad={datos['edad']}, Cuota={datos['cuota']}€, Ses/sem={datos['sesiones_sem']}")

    elif opcion == "5":
    # Calcular métricas: media de cuota, suma de cuotas, total de sesiones
    # y mostrar el cliente con más sesiones semanales
        if not members:
            print("No hay datos para calcular métricas.")
        else:
            total_cuota = 0.0
            suma_sesiones = 0
            count = 0
            max_sesiones = None  # Guardará (id, datos) del socio más activo

            for _id, d in members.items():
                total_cuota += d['cuota']
                suma_sesiones += d['sesiones_sem']
                count += 1

                if (max_sesiones is None) or (d['sesiones_sem'] > max_sesiones[1]['sesiones_sem']):
                    max_sesiones = (_id, d)

            media_cuota = total_cuota / count
            print(f"Nº socios: {count}")
            print(f"Suma cuotas mensuales: {total_cuota:.2f} €")
            print(f"Media cuota mensual: {media_cuota:.2f} €")
            print(f"Suma de sesiones/semana (todos): {suma_sesiones}")

            # Mostrar socio más activo (con más sesiones)
            if max_sesiones:
                id_max, datos_max = max_sesiones
                print("\n🏋️ Socio con más sesiones semanales:")
                print(f"ID: {id_max}")
                print(f"Nombre: {datos_max['nombre']}")
                print(f"Edad: {datos_max['edad']}")
                print(f"Cuota: {datos_max['cuota']} €")
                print(f"Sesiones por semana: {datos_max['sesiones_sem']}")


    elif opcion == "6":
        # Adaptación personalizada: sugerir plan según edad y sesiones por semana
        # (no se crea función externa; se realiza aquí)
        if not members:
            print("No hay socios para adaptar planes.")
        else:
            print("\nSugerencias de plan personalizadas:")
            for mid, datos in members.items():
                edad = datos['edad']
                sesiones = datos['sesiones_sem']
                # lógica de ejemplo (personalizable):
                if edad >= 50:
                    if sesiones <= 1:
                        plan = "Mantenimiento suave: 2 sesiones de movilidad + 1 sesión supervisada."
                    else:
                        plan = "Entrenamiento enfocado en fuerza ligera y equilibrio."
                elif edad >= 30:
                    if sesiones <= 2:
                        plan = "Plan equilibrado: 2 cardio + 2 fuerza moderada."
                    else:
                        plan = "Enfasis en fuerza + cardio intervalado (según tolerancia)."
                else:
                    # menores de 40
                    if sesiones >= 4:
                        plan = "Plan intenso: combinar fuerza, HIIT y técnica."
                    elif sesiones >= 3:
                        plan = "Plan estándar: 2 fuerza + 1 cardio + 1 recuperación activa."
                    else:
                        plan = "Iniciar con 2 sesiones semanales y progresar gradualmente."
                # Guardamos la sugerencia en el registro (adaptación permanente)
                datos['plan_recomendado'] = plan
                print(f"{mid} ({datos['nombre']}): {plan}")

    elif opcion == "7":
        print("Saliendo. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Elige entre 1 y 7.")
