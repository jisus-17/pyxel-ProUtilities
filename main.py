import pyxel

from engine import setting


class App:
    def __init__(self):
        pyxel.init(setting.window_H, setting.window_W, caption="Empezando de cero", fps=120 , quit_key=pyxel.KEY_END, fullscreen=False)
        pyxel.load("assets/assets_game.pyxres")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_END):
            print("End")

    def draw(self):
        pyxel.cls(0)
        


App()