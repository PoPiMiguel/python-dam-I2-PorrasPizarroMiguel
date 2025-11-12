"""
Módulo para analizar una lista de precios.
Proporciona funciones útiles para trabajar con listas de precios,
evitando cálculos redundantes mediante el almacenamiento de valores calculados.
"""

class AnalizadorPrecios:
    def __init__(self):
        self._cache = {}
        self._precios = None
    
    def set_precios(self, precios):
        """Establece la lista de precios y reinicia la caché."""
        if not isinstance(precios, list):
            raise TypeError("Los precios deben ser una lista")
        if not all(isinstance(p, (int, float)) for p in precios):
            raise TypeError("Todos los precios deben ser números")
        self._precios = precios
        self._cache = {}  # Reiniciar la caché cuando se cambian los precios
    
    def get_promedio(self):
        """Calcula el precio promedio."""
        if 'promedio' not in self._cache:
            if not self._precios:
                return 0
            self._cache['promedio'] = sum(self._precios) / len(self._precios)
        return self._cache['promedio']
    
    def get_maximo(self):
        """Obtiene el precio máximo."""
        if 'maximo' not in self._cache:
            if not self._precios:
                return 0
            self._cache['maximo'] = max(self._precios)
        return self._cache['maximo']
    
    def get_minimo(self):
        """Obtiene el precio mínimo."""
        if 'minimo' not in self._cache:
            if not self._precios:
                return 0
            self._cache['minimo'] = min(self._precios)
        return self._cache['minimo']
    
    def get_rango(self):
        """Calcula el rango de precios (diferencia entre máximo y mínimo)."""
        return self.get_maximo() - self.get_minimo()
    
    def precios_sobre_promedio(self):
        """Retorna lista de precios por encima del promedio."""
        promedio = self.get_promedio()
        return [precio for precio in self._precios if precio > promedio]
    
    def precios_bajo_promedio(self):
        """Retorna lista de precios por debajo del promedio."""
        promedio = self.get_promedio()
        return [precio for precio in self._precios if precio < promedio]
    
    def resumen_estadistico(self):
        """Retorna un diccionario con el resumen estadístico de los precios."""
        return {
            'promedio': self.get_promedio(),
            'maximo': self.get_maximo(),
            'minimo': self.get_minimo(),
            'rango': self.get_rango(),
            'total_precios': len(self._precios) if self._precios else 0
        }
