import setting
from game_math import square_vectors, square_distance


class make_sensor:
    """
    con 4 valores vectoriales(x, y) determina la posición de los sensores del obj pasado
    """

    def __init__(self, obj_parent):
        """
        inputs del objparent x y w h
        """
        self.x = obj_parent.x
        self.y = obj_parent.y
        self.w = obj_parent.w
        self.h = obj_parent.h

        self.a_x, self.a_y = 1, 1
        self.b_x, self.b_y = 1, 1
        self.c_x, self.c_y = 1, 1
        self.d_x, self.d_y = 1, 1

    def create_sensor(self):
        """
        crea los sensores llamando a la función square_vectors de math.py
        """

        response = square_vectors(self.x, self.y, self.h, self.w)


class example:
    """
    docstring
    """

    def __init__(self, x, y, w, h):
        """
        docstring
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
