import unittest
from trash import TrashCity, Camion, Turno, Ruta, PuntoGeo, Persona
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.persona1 = Persona("Sebastian", "conductor")
        self.persona2 = Persona("Angel", "asistente")
        self.persona3 = Persona("Victor", "asistente2")

        self.punto = PuntoGeo(30.3874, 35.00370)

        self.ruta = Ruta([self.punto])

        self.turno = Turno(datetime.now(), [self.persona1, self.persona2, self.persona3], self.ruta, {"vidrio": 500})

        self.camion = Camion([self.turno])

        self.trashCity = TrashCity([self.camion])

    def test_get_residuos(self):
        vidrio_t = self.trashCity.get_residuos(datetime.now())
        self.assertEqual(vidrio_t, 500)


if __name__ == '__main__':
    unittest.main()
