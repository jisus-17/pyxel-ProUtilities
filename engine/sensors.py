from .game_math import *
from .collisions import *
from .setting import *
import pyxel
import time

class sensor:
    """
    docstring
    """

    def __init__(self, x, y):
        """
        docstring
        """
        self.x = x
        self.y = y

    def draw(self):
        """
        docstring
        """
        if debug == True:
            pyxel.rectb(self.x, self.y, 5, 5, 8)
        else:
            pass


def create_sersor(obj_parent, n=4):
    """
    crea el sensor usando la clase sensor para instanciar los cuatro vectores
    """
    x = obj_parent.x
    y = obj_parent.y
    h = obj_parent.h
    w = obj_parent.w
    vector_list = square_vectors(x, y, h, w)

    # tiene que ir cada dos elementos de la lista y crear un obj del sensor con su x , y 

    l = len(vector_list)
    i = 0
    while i > l:
        sensor(vector_list[i], vector_list[i+1])
        i += 2