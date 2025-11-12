"""
Programa principal que utiliza el módulo de análisis de precios robusto.
"""

from auxprecioserror import AnalizadorPreciosRobusto, PrecioError, ListaPreciosVaciaError

# Crear instancia del analizador
analizador = AnalizadorPreciosRobusto()

try:
    # Solicitar precios al usuario
    print("Introduce los precios (uno por línea). Presiona Enter sin valor para terminar.")
    precios = []
    
    while True:
        entrada = input("Precio (o Enter para terminar): ").strip()
        if not entrada:
            break
        precios.append(entrada)
    
    # Procesar los precios
    analizador.set_precios(precios)
    
    # Mostrar resultados
    resumen = analizador.resumen_estadistico()
    print("\n=== RESUMEN DEL ANÁLISIS ===")
    
    if 'error' in resumen:
        print(f"Error principal: {resumen['error']}")
    else:
        print(f"Total de precios válidos: {resumen['total_precios']}")
        print(f"Precio promedio: {resumen['promedio']:.2f}€")
        print(f"Precio máximo: {resumen['maximo']:.2f}€")
        print(f"Precio mínimo: {resumen['minimo']:.2f}€")
    
    if resumen.get('errores'):
        print("\nErrores encontrados durante el análisis:")
        for error in resumen['errores']:
            print(f"- {error}")

except ListaPreciosVaciaError as e:
    print(f"\nError: {e}")
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")
except Exception as e:
    print(f"\nError inesperado: {e}")
finally:
    print("\nFin del análisis de precios.")