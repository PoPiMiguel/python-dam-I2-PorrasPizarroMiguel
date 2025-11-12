import matplotlib.pyplot as plt
from datetime import date, datetime

# Metodo estándar

#Función 1
print("\nFuncion 1")
ahora = datetime.now()
print("Fecha y hora actuales:", ahora)

#Funcion 2
print("\nFuncion 2")
# Una cadena con una fecha en formato día/mes/año
texto_fecha = "29/10/2025"

# Convertimos el texto en un objeto datetime
fecha_objeto = datetime.strptime(texto_fecha, "%d/%m/%Y")

print("Texto original:", texto_fecha)
print("Objeto datetime:", fecha_objeto)
print("Año:", fecha_objeto.year)
print("Mes:", fecha_objeto.month)
print("Día:", fecha_objeto.day)

#Funcion 3
print("\nFuncion 3")
hoy = date.today()
print("Fecha de hoy:", hoy)
print("Año:", hoy.year)
print("Mes:", hoy.month)
print("Día:", hoy.day)

# Metodo no estándar

# Datos para el gráfico
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
ventas = [1000, 1200, 900, 1500, 1300, 1700]

# Gráfico de barras
plt.bar(meses, ventas, color='green', alpha=0.7)
plt.title('Ventas por Mes (Barras)')

plt.xlabel('Meses')
plt.ylabel('Ventas (€)')

# Ajustar el layout y mostrar el gráfico
plt.tight_layout()
plt.show()
