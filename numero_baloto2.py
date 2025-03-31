import tkinter as tk
import random

#aqui se generan 5 numeros aleatorios entre el rango que se dictará
class GeneradorNumerosAleatorios:      
    def __init__(self, minimo, maximo, cantidad):
        self.minimo = minimo
        self.maximo = maximo
        self.cantidad = cantidad

    def generar_numeros(self):
        return random.sample(range(self.minimo, self.maximo+1), self.cantidad)      # se usa el random.sample() para obtener  una lista de números únicos.

class GeneradorNumeroBalota:        #Esta clase genera la balota roja que es del 1 al 16
    def __init__(self, minim, maxim):
        self.minim = minim
        self.maxim = maxim

    def generate_numbers(self):
        return random.randint(self.minim, self.maxim)     # igual con el random...pero este es random.radint que genera 1 número leatorio

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

# AQUI SE CREAN LAS INSTANCIAS
generador = GeneradorNumerosAleatorios(1, 43, 5)
generate = GeneradorNumeroBalota(1, 16)

# Configurar ventana
root = tk.Tk()
root.title("GENERADOR DE LOS NUMEROS GANADORES DE JUAN TORO")

# Crear canvas para dibujar
canvas = tk.Canvas(root, width=500, height=150)
canvas.pack()

# Botón para generar números
btn_generar = tk.Button(root, text="GENERANDO LOS NUMEROS GANADORES", command=generar_numeros, bd=5)
btn_generar.pack()

# Mostrar números iniciales
generar_numeros()

# Ejecutar la aplicación
root.mainloop()
