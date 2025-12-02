# Datos del ejercicio
capital_inicial = 1000  # en dólares
tasa_interes = 5  # tasa de interés anual en porcentaje
años = 3  # tiempo en años

# Cálculo del monto final con interés compuesto
monto_final = capital_inicial * (1 + tasa_interes / 100) ** años

print(f"El monto final después de {años} años es: ${monto_final:.2f}")
