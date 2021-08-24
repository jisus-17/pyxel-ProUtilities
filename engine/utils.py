import pyxel

def key_movement(obj, f, stable):
    """
    Usa configuración wasd y flechas, el valor f es el factor que edita la x , y del objeto
    Modos, 1 movimiento total, 2 movimiento vertical, 3 movimiento horizontal, 4 movimiento mouse, 
    si no se devuelve valor correcto
    si se escoje modos 2 o 3 se tiene que dar un valor stable que será la cifra para el punto que no se moverá
    """
    x = obj.x
    y = obj.y
    mode = obj.mode

    if mode == 1:
        if pyxel.KEY_W or pyxel.KEY_UP:
            y += f
        elif pyxel.KEY_S or pyxel.KEY_DOWN:
            y -= f
        if pyxel.KEY_A or pyxel.KEY_LEFT:
            x += f
        elif pyxel.KEY_D or pyxel.KEY_RIGHT:
            x -= f

    elif mode == 2:
        x = stable
        if pyxel.KEY_W or pyxel.KEY_UP:
            y += f
        elif pyxel.KEY_S or pyxel.KEY_DOWN:
            y -= f

    elif mode == 3:
        y = stable
        if pyxel.KEY_A or pyxel.KEY_LEFT:
            x += f
        elif pyxel.KEY_D or pyxel.KEY_RIGHT:
            x -= f

    elif mode == 4:
        x = pyxel.mouse_x()
        y = pyxel.mouse_y()

    else:
        x = 15
        y = 15

    return x, y
