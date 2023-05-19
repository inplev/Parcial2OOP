from datetime import datetime
from typing import List

"""
Con punto Geo se busca es nada más buscar los puntos de longitud y latitud para que luego sean usados por la clase Ruta.

"""


class PuntoGeo:
    def __init__(self, longitud: float, latitud: float):
        self.longitud = longitud
        self.latitud = latitud


"""
La clase Ruta coge los puntos que salen en Punto Geo y se agregan a una lista.
"""


class Ruta:
    def __init__(self, puntos: List[PuntoGeo]):
        self.puntos = puntos


"""
La clase Persona nada más tiene parámetros para indicar el nombre y el puesto que tienen las personas que irán en el
camion.
"""


class Persona:
    def __init__(self, nombre: str, puesto: str):
        self.nombre = nombre
        self.puesto = puesto


"""
Turno toma parámetros sobre el dia, el resultado de los nombres y roles en Persona se guardan en una lista, lo que se
instancia de Ruta se agrega como parámetro en esta clase y el tipo de residuos se guarda en un diccionario con la
cantidad de vidrio también.
"""


class Turno:
    def __init__(self, dia: datetime, equipo: list[Persona], ruta: Ruta, residuos: dict):
        self.dia = dia
        self.equipo = equipo
        self.ruta = ruta
        self.residuos = residuos


"""
La clase camion pone todo los parámetros que se instancian en Turno se guarda en una lista.
"""


class Camion:
    def __init__(self, turnos: list[Turno]):
        self.turnos = turnos


"""
Con esta clase es donde se implementa la cantidad de residuos que son vidrios y se cuenta la cantidad que se recogió en
distintas rutas pero en el mismo día, se le pasa además una lista con los camiones que han salido en ese mismo día.
"""


class TrashCity:
    def __init__(self, camiones: list[Camion]):
        self.camiones = camiones

    def get_residuos(self, dia: datetime):
        vidrio_t = 0
        for camion in self.camiones:
            for turno in camion.turnos:
                if turno.dia.date() == dia.date():
                    vidrio_t += turno.residuos
        return vidrio_t
