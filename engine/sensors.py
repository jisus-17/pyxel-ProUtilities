from game_math import *
from collisions import *
from setting import *
import pyxel
import time


class sensor:
    """
    docstring
    """

    def __init__(self, x, y):
        """
        usa el parámetr sensor list de donde extrae la posición 1 x , la 2 y
        """
        self.x = x
        self.y = y

    def draw(self):
        pyxel.rectb(self.x, self.y, 5, 5, 8)


def create_sensor(obj_parent):
    """
    crea el sensor usando la clase sensor para instanciar los cuatro vectores
    """
    x = obj_parent.x
    y = obj_parent.y
    h = obj_parent.h
    w = obj_parent.w
    vector_list = square_vectors(x, y, h, w)

    # cada parte de la lista a su vez es otra lista de
    # 2 elementos x , y en ese orden y lo pasa a la clase sensor
    a = vector_list[0]
    b = vector_list[1]
    c = vector_list[2]
    d = vector_list[3]

    top_s = sensor(a[0], a[1])
    bottom_s = sensor(b[0], b[1])
    right_s = sensor(c[0], c[1])
    left_s = sensor(d[0], d[1])

    obj_parent.sensors = [top_s, bottom_s, right_s, left_s]


def update_sensor(obj_parent):
    """
    docstring
    """
    x = obj_parent.x
    y = obj_parent.y
    h = obj_parent.h
    w = obj_parent.w
    sensors = obj_parent.sensors

    vector_list = square_vectors(x, y, h, w)

    a = vector_list[0]
    b = vector_list[1]
    c = vector_list[2]
    d = vector_list[3]

    sensors[0] = sensor(a[0], a[1])

    sensors[1] = sensor(b[0], b[1])

    sensors[2] = sensor(c[0], c[1])

    sensors[3] = sensor(d[0], d[1])


class example:
    """
    clase para probar funcionalidad
    """

    def __init__(self, x, y, w, h):
        """
        docstring
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sensors = []
