class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def info(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return [self.numero, self.tipo, f"${self.precio:.2f}", estado]