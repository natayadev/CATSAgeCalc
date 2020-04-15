factor1 = 4.0
factor2 = 10
print("----------¡Bienvenido a la calculadora gatuna!----------")
print("Por favor, ingrese la edad de su gato/a en años humanos")
print(" > Para expresar la edad en meses utilice decimales")
print(" > Para expresar la edad en años utilice números enteros")
print("   (Por ejemplo: para 3 meses escribir 0.3)")
print("--------------------------------------------------------")
edadHumana = float(input("Edad humana: "))

def calculadoraGatuna():
    if edadHumana >= 1:
        edadGatuna = 10 + (factor1 * edadHumana)
        return print("Su mascota tiene aproximadamente " + str(edadGatuna) + " años gatunos :)")
    elif edadHumana <= 0.9:
        edadGatuna = 4 + (factor2 * edadHumana)
        return print("Su mascota tiene aproximadamente " + str(edadGatuna) + " años gatunos :)")
    elif edadHumana <= 0.6:
        edadGatuna = (factor2 * edadHumana)
        return print("Su mascota tiene aproximadamente " + str(edadGatuna) + " años gatunos :)")
    
calculadoraGatuna()