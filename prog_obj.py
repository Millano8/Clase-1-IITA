"""
# OOP

- Realizar un programa que, a su criterio, es más adecuado para ser resuelto con programación orientada a objetos.
- El programa debe tener al menos 3 clases.

"""

# Clase Computadora, con un sólo metodo prender.
class Computadora:
    def prender(self)->None:
        print("La computadora se esta encienciendo")
        print("La computadora esta encendida")

# Clase Battelfield, con un solo metodo inicializar_juego.
class Battelfield:
    def inicializar_juego(self)->None:
        print("Iniciando el juego Battelfield")
        print("Juego Battelfield Inicializado")

# Clase Messi, con un solo metodo elegir_personaje.
class Messi:
    def elegir_personaje(self)->None:
        print("Eligiendo el personaje...")
        print("Personaje Messi elegido, esperando a la red para conectarse con los demás personajes")  

def main():
    computadora = Computadora()
    computadora.prender()
    juego = Battelfield()
    juego.inicializar_juego()
    personaje = Messi()
    personaje.elegir_personaje()



main()