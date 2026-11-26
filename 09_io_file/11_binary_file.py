import reprlib
from pathlib import Path

import samples.bmp as bmp
import samples.fractal as fractal

HERE = Path(__file__).resolve().parent

pixels = fractal.mandelbrot(448, 256)

print(reprlib.repr(pixels))

out = HERE / "mandel.bmp"
bmp.write_grayscale(out, pixels)

dim = bmp.dimensions(out)
print(dim)
