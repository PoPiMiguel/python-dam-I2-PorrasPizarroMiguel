from auxprecios import AnalizadorPrecios

# Crear una instancia del analizador de precios
analizador = AnalizadorPrecios()

# Solicitar precios al usuario
print("Introduce los precios (uno por línea). Presiona Enter sin valor para terminar:")
precios = []
while True:
    try:
        precio = float(input("Precio (o Enter para terminar): ") or "")
        if precio == 0.0:  # Si el usuario solo presionó Enter
            break
        precios.append(precio)
    except ValueError:
        print("Error: Por favor introduce un número válido")

# Si no hay precios, terminar
if not precios:
    print("No se introdujeron precios.")
    exit()

# Establecer los precios en el analizador
analizador.set_precios(precios)

# Obtener y mostrar el resumen estadístico
print("\n=== ANÁLISIS DE PRECIOS ===")
resumen = analizador.resumen_estadistico()
print(f"\nTotal de precios analizados: {resumen['total_precios']}")
print(f"Precio promedio: {resumen['promedio']:.2f}€")
print(f"Precio máximo: {resumen['maximo']:.2f}€")
print(f"Precio mínimo: {resumen['minimo']:.2f}€")
print(f"Rango de precios: {resumen['rango']:.2f}€")

# Mostrar precios sobre y bajo el promedio
precios_altos = analizador.precios_sobre_promedio()
precios_bajos = analizador.precios_bajo_promedio()

print("\nPrecios por encima del promedio:")
for precio in precios_altos:
    print(f"  - {precio:.2f}€")

print("\nPrecios por debajo del promedio:")
for precio in precios_bajos:
    print(f"  - {precio:.2f}€")
