import asyncio


def square_distance(n1=2, n2=4):
    """
    distancia cuadrada entre dos números
    """
    x_square = (n1.x - n2.x) ** 2
    y_square = (n1.y - n2.y) ** 2

    return x_square + y_square


def even_odd(n1=0):
    """
    calcula par o impar de un número
    devuelve True si es par y False si es impar
    """
    try:
        if n1 % 2 == 0:
            return True
        elif n1 == 0:
            pass
        else:
            return False
    except:
        pass


async def percentaje(n=0, n_max=0, t=0, f=0, action=False):
    """
    n = número actual del porcentaje n_max = número máximo del porcentage t = tiempo f = número que edita el porcentage
    crea un porcentage y lo edita en el tiempo según la acción, True = creciendo, False = decreciendo
    """

    if action == True:

        for i in range(n, n_max, f):
            n = i
            await asyncio.sleep(t)

        return n

    elif action == False:
        for i in range(n, 0, f):
            n = i
            await asyncio.sleep(t)

        return n


def square_vectors(x, y, h, w):
    """
    desde el punto arriba izquierda dando la x y de ese punto, genera el resto de esquinas usando el ancho w y el alto w
    """
    # 1
    a_x, a_y = x, y
    # 2
    b_x, b_y = x + w, y
    # 3
    c_x, c_y = x, y + h
    # 4
    d_x, d_y = x + w, y + h

    a = [a_x, a_y]
    b = [b_x, b_y]
    c = [c_x, c_y]
    d = [d_x, d_y]

    vectors = [a, b, c, d]

    return vectors


def rectagles_overlapping(parameter_list):
    """
    docstring
    """
    pass
