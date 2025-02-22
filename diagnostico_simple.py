def diagnostico(sintomas):
    if "fiebre" in sintomas and "tos" in sintomas:
        return "Posible gripe"
    elif "dolor de cabeza" in sintomas and "mareo" in sintomas:
        return "Posible migraña"
    elif "dolor abdominal" in sintomas and "nauseas" in sintomas:
        return "Posible indigestión"
    else:
        return "Síntomas no claros. Consulte a un médico."

# Solicitar síntomas al usuario
print("Ingrese sus síntomas separados por coma (por ejemplo: fiebre, tos, dolor de cabeza):")
sintomas = input().lower().split(',')

# Diagnóstico
resultado = diagnostico(sintomas)
print(f"Diagnóstico: {resultado}")
