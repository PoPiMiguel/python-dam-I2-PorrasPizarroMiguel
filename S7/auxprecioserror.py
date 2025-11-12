"""
Módulo robusto para analizar una lista de precios con manejo avanzado de errores.
"""

class PrecioError(Exception):
    """Clase base para excepciones relacionadas con precios"""
    pass

class PrecioNegativoError(PrecioError):
    """Se lanza cuando se detecta un precio negativo"""
    pass

class ListaPreciosVaciaError(PrecioError):
    """Se lanza cuando se intenta operar con una lista vacía"""
    pass

class TipoDatoIncorrectoError(PrecioError):
    """Se lanza cuando un precio no es del tipo correcto"""
    pass

class AnalizadorPreciosRobusto:
    def __init__(self):
        self._cache = {}
        self._precios = None
        self._errores_encontrados = []
    
    def _validar_precio(self, precio):
        """Valida un precio individual"""
        try:
            # Convertir a float si es posible
            precio_float = float(precio)
            
            if precio_float < 0:
                raise PrecioNegativoError(f"El precio {precio_float} es negativo")
                
            return precio_float
            
        except ValueError:
            raise TipoDatoIncorrectoError(f"El valor '{precio}' no es un número válido")
    
    def set_precios(self, precios):
        """Establece y valida la lista de precios"""
        if not precios:
            raise ListaPreciosVaciaError("La lista de precios está vacía")
            
        precios_validados = []
        errores = []
        
        # Validar cada precio
        for i, precio in enumerate(precios):
            try:
                precio_validado = self._validar_precio(precio)
                precios_validados.append(precio_validado)
            except PrecioError as e:
                errores.append(f"Error en índice {i}: {str(e)}")
        
        # Si hay errores, guardarlos pero continuar si hay precios válidos
        self._errores_encontrados = errores
        
        if not precios_validados:
            raise ListaPreciosVaciaError("No hay precios válidos después de la validación")
            
        self._precios = precios_validados
        self._cache = {}  # Reiniciar la caché
    
    def get_promedio(self):
        """Calcula el precio promedio de forma segura"""
        try:
            if not self._precios:
                raise ListaPreciosVaciaError("No hay precios para calcular el promedio")
            
            if 'promedio' not in self._cache:
                self._cache['promedio'] = sum(self._precios) / len(self._precios)
            
            return self._cache['promedio']
            
        except Exception as e:
            raise PrecioError(f"Error al calcular el promedio: {str(e)}")
    
    def get_maximo(self):
        """Obtiene el precio máximo de forma segura"""
        try:
            if not self._precios:
                raise ListaPreciosVaciaError("No hay precios para calcular el máximo")
            
            if 'maximo' not in self._cache:
                self._cache['maximo'] = max(self._precios)
            
            return self._cache['maximo']
            
        except Exception as e:
            raise PrecioError(f"Error al obtener el precio máximo: {str(e)}")
    
    def get_minimo(self):
        """Obtiene el precio mínimo de forma segura"""
        try:
            if not self._precios:
                raise ListaPreciosVaciaError("No hay precios para calcular el mínimo")
            
            if 'minimo' not in self._cache:
                self._cache['minimo'] = min(self._precios)
            
            return self._cache['minimo']
            
        except Exception as e:
            raise PrecioError(f"Error al obtener el precio mínimo: {str(e)}")
    
    def get_errores(self):
        """Retorna la lista de errores encontrados durante la validación"""
        return self._errores_encontrados
    
    def resumen_estadistico(self):
        """Retorna un resumen estadístico con manejo de errores"""
        try:
            return {
                'promedio': self.get_promedio(),
                'maximo': self.get_maximo(),
                'minimo': self.get_minimo(),
                'total_precios': len(self._precios) if self._precios else 0,
                'errores': self.get_errores()
            }
        except PrecioError as e:
            return {
                'error': str(e),
                'errores': self.get_errores()
            }

# Casos de prueba
def test_analizador():
    analizador = AnalizadorPreciosRobusto()
    
    # Caso de prueba 1: Precios válidos e inválidos mezclados
    try:
        precios_mixtos = [100, -50, "abc", 75.5, "200", -30]
        analizador.set_precios(precios_mixtos)
    except PrecioError as e:
        print(f"Test 1 - Error esperado: {e}")
        print("Errores encontrados:", analizador.get_errores())
    
    # Caso de prueba 2: Lista vacía
    try:
        analizador.set_precios([])
    except ListaPreciosVaciaError as e:
        print(f"\nTest 2 - Error esperado: {e}")

if __name__ == "__main__":
    test_analizador()