import tkinter as tk
import random


class GeneradorNumerosAleatorios:
    def __init__(self, minimo, maximo, cantidad):
        self.minimo = minimo
        self.maximo = maximo
        self.cantidad = cantidad

    def generar_numeros(self):
        return random.sample(range(self.minimo, self.maximo+1), self.cantidad)

class GeneradorNumeroBalota:
    def __init__(self, minim, maxim):
        self.minim = minim
        self.maxim = maxim

    def generate_numbers(self):
        return random.randint(self.minim, self.maxim)

# Función para actualizar la interfaz
def generar_numeros():
    numeros = generador.generar_numeros()
    balota_roja = generate.generate_numbers()
    mostrar_numeros(numeros, balota_roja)

# Función para mostrar los números en la interfaz
def mostrar_numeros(numeros, balota_roja):
    canvas.delete("all")  # Limpiar el canvas
    
    # Dibujar fondo azul
    canvas.create_rectangle(0, 0, 500, 150, fill="blue", outline="blue")
    
    # Dibujar balotas amarillas
    for i, num in enumerate(numeros):
        x = 50 + i * 80
        canvas.create_oval(x, 50, x+50, 100, fill="gold", outline="black")
        canvas.create_text(x+25, 75, text=f"{num:02d}", font=("Arial", 14, "bold"))
    
    # Dibujar balota roja
    x = 50 + 5 * 80
    canvas.create_oval(x, 50, x+50, 100, fill="red", outline="black")
    canvas.create_text(x+25, 75, text=f"{balota_roja:02d}", font=("Arial", 14, "bold"), fill="white")

# Crear instancias de las clases
generador = GeneradorNumerosAleatorios(1, 43, 5)
generate = GeneradorNumeroBalota(1, 16)

# Configurar ventana
root = tk.Tk()
root.title("Generador de Números")

# Crear canvas para dibujar
canvas = tk.Canvas(root, width=500, height=150)
canvas.pack()

# Botón para generar números
btn_generar = tk.Button(root, text="Generar Números", command=generar_numeros)
btn_generar.pack()

# Mostrar números iniciales
generar_numeros()

# Ejecutar la aplicación
root.mainloop()
