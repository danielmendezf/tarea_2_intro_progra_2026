# Autores: Trinidad González (22.141.114-5) - Daniel Méndez (17.673.909-6)

# Lista para guardar las temperaturas
temperaturas = []


# Función para ingresar temperaturas
def ingresar_temperaturas():
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)


# Función para calculo promedio
def calcular_promedio():
    return sum(temperaturas) / len(temperaturas)


# Función para calcular los días sobre el promedio
def dias_sobre_el_prmedio(promedio):
    dias_superiores = 0
    for tempemperatura in temperaturas:
        if tempemperatura > promedio:
            dias_superiores += 1
    return dias_superiores


# Función principal
def mostrar_resultados():
    promedio = calcular_promedio()
    maxima = max(temperaturas)
    minima = min(temperaturas)

    # Mostrar resultados
    print("\n--- RESULTADOS ---")
    print(f"Temperatura promedio: {promedio:.2f} grados")
    print("Temperatura máxima:", maxima)
    print("Temperatura mínima:", minima)
    print("Días sobre el promedio:", dias_sobre_el_prmedio(promedio))


# Programa principal
ingresar_temperaturas()
mostrar_resultados()
