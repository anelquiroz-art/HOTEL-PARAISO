from datetime import datetime

class Reserva:
    def __init__(self, huesped, habitacion, fecha_entrada, fecha_salida):
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

    def mostrar_reserva(self):
        dias = (self.fecha_salida - self.fecha_entrada).days
        total = dias * self.habitacion.precio
        return (f"Huésped: {self.huesped.nombre} (DNI: {self.huesped.dni})\n"
                f"Tel: {self.huesped.telefono} | Correo: {self.huesped.correo}\n"
                f"Habitación: {self.habitacion.numero} ({self.habitacion.tipo})\n"
                f"Desde: {self.fecha_entrada.strftime('%d/%m/%Y')} "
                f"Hasta: {self.fecha_salida.strftime('%d/%m/%Y')} "
                f"({dias} noches)\n"
                f"Total: ${total:.2f}\n")