# pixibi.py
import neopixel
import machine

PIN = 14
WIDTH = 8
HEIGHT = 8
BRIGHTNESS = 0.03

np = neopixel.NeoPixel(machine.Pin(PIN), WIDTH * HEIGHT)

def _color_name_to_rgb(name):
    return {
        "red": (int(255 * BRIGHTNESS), 0, 0),
        "green": (0, int(255 * BRIGHTNESS), 0),
        "blue": (0, 0, int(255 * BRIGHTNESS)),
        "off": (0, 0, 0)
    }.get(name, (0, 0, 0))

def _xy(x, y):
    return y * WIDTH + x

class MatrixRow:
    def __init__(self, y):
        self.y = y
    def __setitem__(self, x, value):
        np[_xy(x, self.y)] = _color_name_to_rgb(value)
        np.write()

class Matrix:
    def __getitem__(self, y):
        return MatrixRow(y)

m = Matrix()  # exposed globally
matrix = m    # alias
