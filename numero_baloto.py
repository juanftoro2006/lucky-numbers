'''
crear código que me muestre seis numeros aleatorios más otro 
numero con mimimos y máximos que me haran ganador del BALOTO
'''
import random

class GeneradorNumerosAleatorios:
    def __init__(self, minimo, maximo, cantidad):
        self.minimo = minimo
        self.maximo = maximo
        self.cantidad = cantidad

    def generar_numeros(self):
        return random.sample(range(self.minimo, self.maximo+1), self.cantidad)


# Crear una instancia de la clase
generador = GeneradorNumerosAleatorios(1, 43, 5)  #el rango es del 1 al 43 y de allí toma 5 números

# Generar los números aleatorios
numeros_aleatorios = generador.generar_numeros()

print("Números Baloto ganador")
for i, num in enumerate(numeros_aleatorios, 1):
    print(f"El número {i} es: {num}")


class GeneradorNumeroBalota:
    def __init__(self, minim, maxim):
        self.minim = minim
        self.maxim = maxim
        
    def generate_numbers(self):
        balota = random.randint(self.minim, self.maxim)
        
        return balota

generate = GeneradorNumeroBalota(1, 16)
numero_balota = generate.generate_numbers()

print("Número de la SUPER-balota:", numero_balota)