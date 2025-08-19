from datetime import datetime
import unittest
from hotel import Hotel
from habitacion import Habitacion
from huesped import Huesped
from reserva import Reserva

class TestHotel(unittest.TestCase):
    def test_hotel(self):
        hotel = Hotel("Hotel Paraíso")
        self.assertEqual(hotel.nombre, "Hotel Paraíso")

    def test_habitacion(self):
        habitacion = Habitacion(101, "Simple", 50)
        self.assertEqual(habitacion.numero, 101)
        self.assertEqual(habitacion.tipo, "Simple")
        self.assertEqual(habitacion.precio, 50)

    def test_huesped(self):
        huesped = Huesped("Juan Pérez", "12345678", "1234567890", "juan@example.com")
        self.assertEqual(huesped.nombre, "Juan Pérez")
        self.assertEqual(huesped.dni, "12345678")
        self.assertEqual(huesped.telefono, "1234567890")
        self.assertEqual(huesped.correo, "juan@example.com")

    def test_reserva(self):
        huesped = Huesped("Juan Pérez", "12345678", "1234567890", "juan@example.com")
        habitacion = Habitacion(101, "Simple", 50)
        fecha_entrada = datetime(2023, 3, 15)
        fecha_salida = datetime(2023, 3, 20)
        reserva = Reserva(huesped, habitacion, fecha_entrada, fecha_salida)
        self.assertEqual(reserva.huesped, huesped)
        self.assertEqual(reserva.habitacion, habitacion)
        self.assertEqual(reserva.fecha_entrada, fecha_entrada)
        self.assertEqual(reserva.fecha_salida, fecha_salida)

if __name__ == '__main__':
    unittest.main()