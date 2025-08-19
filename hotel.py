from datetime import datetime

from habitacion import Habitacion
from huesped import Huesped
from reserva import Reserva

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []
        self.precargar_habitaciones()

    def precargar_habitaciones(self):
        self.habitaciones.extend([
            Habitacion(101, "Simple", 50),
            Habitacion(102, "Doble", 75),
            Habitacion(201, "Suite", 120),
            Habitacion(202, "Doble", 80),
            Habitacion(301, "Suite", 150),
        ])

    def mostrar_todas_habitaciones(self):
        print("\n{:<10} {:<10} {:<15} {:<12}".format("Número", "Tipo", "Precio/Noche", "Estado"))
        print("-" * 50)
        for hab in self.habitaciones:
            num, tipo, precio, estado = hab.info()
            print(f"{num:<10} {tipo:<10} {precio:<15} {estado:<12}")
        print("-" * 50)

    def hacer_reserva(self):
        print("\n--- Registro de huésped ---")
        nombre = input("Nombre completo: ")
        dni = input("DNI: ")
        telefono = input("Teléfono: ")
        correo = input("Correo electrónico: ")
        huesped = Huesped(nombre, dni, telefono, correo)

        self.mostrar_todas_habitaciones()
        try:
            num_hab = int(input("Ingrese el número de la habitación a reservar: "))
            habitacion = next((h for h in self.habitaciones if h.numero == num_hab and not h.ocupada), None)
            if habitacion is None:
                print("Habitación no disponible o no existe.")
                return

            entrada = datetime.strptime(input("Fecha de entrada (dd/mm/yyyy): "), "%d/%m/%Y")
            salida = datetime.strptime(input("Fecha de salida (dd/mm/yyyy): "), "%d/%m/%Y")
            if salida <= entrada:
                print("Error: La fecha de salida debe ser posterior a la de entrada.")
                return

            reserva = Reserva(huesped, habitacion, entrada, salida)
            self.reservas.append(reserva)
            habitacion.ocupada = True
            print("\n¡Reserva realizada exitosamente!")
            print(reserva.mostrar_reserva())
        except ValueError:
            print("Error en el formato de fecha o número de habitación.")

    def ver_reservas(self):
        print("\n--- Reservas activas ---")
        if not self.reservas:
            print("No hay reservas registradas.")
        else:
            for r in self.reservas:
                print(r.mostrar_reserva())

    def obtener_saludo_por_hora(self):
        hora_actual = datetime.now().hour
        if 5 <= hora_actual < 12:
            return "Buenos días"
        elif 12 <= hora_actual < 18:
            return "Buenas tardes"
        else:
            return "Buenas noches"

    def menu(self):
        saludo = self.obtener_saludo_por_hora()
        print("\n" + "="*50)
        print(f"{saludo:^50}")
        print(f"{'¡Bienvenido al ' + self.nombre + '!':^50}")
        print(f"{'Sistema de Gestión Hotelera':^50}")
        print("="*50)

        while True:
            print("\nMenú principal")
            print("1. Ver habitaciones y disponibilidad")
            print("2. Hacer una reserva")
            print("3. Ver reservas activas")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.mostrar_todas_habitaciones()
            elif opcion == '2':
                self.hacer_reserva()
            elif opcion == '3':
                self.ver_reservas()
            elif opcion == '4':
                print("Gracias por usar el sistema del hotel.")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")