# 09 — File I/O and resource management

## `open()`

- Modes: read `r`, write `w`, append `a`
- Selectors: binary `b`, text `t`
- Prefer `with open(...) as f:` so files always close

## File-like objects

- Objects that behave like files (a semi-formed protocol)
- Use an EAFP approach when necessary

## Scripts & samples

| Path | Notes |
|------|--------|
| `02_writing_file.py` … `05_iterating_file.py` | Text I/O around `wasteland.txt` |
| `06_recman_seq_file.py` … `10_with_file.py` | Recaman sequence write/read |
| `11_binary_file.py` | Mandelbrot → grayscale BMP |
| `12_file_like.py` | Local file vs `urlopen` response |
| `13_context_managers.py` | `contextlib.closing` demo |
| `samples/bmp.py` / `fractal.py` | BMP writer & Mandelbrot helper |

Generated `*.txt` / `*.dat` / `*.bmp` beside these scripts are gitignored.
