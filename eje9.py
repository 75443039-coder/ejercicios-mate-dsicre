# Datos del ejercicio
poblacion_inicial = 500  # cantidad de bacterias
tiempo_en_horas = 8  # tiempo transcurrido en horas

# Cálculo de la población final
poblacion_final = poblacion_inicial * (2 ** (tiempo_en_horas / 2))

print(f"La población de bacterias después de {tiempo_en_horas} horas es: {poblacion_final} bacterias")
