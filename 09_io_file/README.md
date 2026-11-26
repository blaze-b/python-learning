# Chapter 9: Files And I/O

Text and binary files, file-like objects, and context managers for reliable cleanup.

## What You'll Learn

- Opening files for read / write / append with explicit encodings
- Iterating lines and managing file lifetimes with `finally` and `with`
- Writing and reading structured numeric series (Recaman)
- Binary BMP output and Mandelbrot pixel buffers
- Treating local files and HTTP responses as file-like objects

## Lessons

| Script | What It Shows |
|--------|---------------|
| [01_file_encoding.py](./01_file_encoding.py) | Default text encoding from the interpreter |
| [02_writing_file.py](./02_writing_file.py) | Writing text with `open(..., mode="wt")` |
| [03_reading_file.py](./03_reading_file.py) | `read`, `readline`, `readlines`, and `seek` |
| [04_appending_file.py](./04_appending_file.py) | Appending lines with mode `at` |
| [05_iterating_file.py](./05_iterating_file.py) | Iterating lines; CLI path or local fallback |
| [06_recman_seq_file.py](./06_recman_seq_file.py) | Writing Recaman’s sequence to a `.dat` file |
| [07_recman_series_file.py](./07_recman_series_file.py) | Reading an integer series (simple close) |
| [08_recman_series_finally.py](./08_recman_series_finally.py) | Guaranteeing `close` with `finally` |
| [09_run_reader.py](./09_run_reader.py) | Line-by-line integer parsing |
| [10_with_file.py](./10_with_file.py) | `with` for both write and read |
| [11_binary_file.py](./11_binary_file.py) | Mandelbrot pixels → grayscale BMP |
| [12_file_like.py](./12_file_like.py) | Same helper over a file and a `urlopen` response |
| [13_context_managers.py](./13_context_managers.py) | `contextlib.closing` around a custom resource |
| [samples/bmp.py](./samples/bmp.py) | BMP writer / dimension reader |
| [samples/fractal.py](./samples/fractal.py) | Mandelbrot pixel generator |

## Key Concepts

### `open()`

- Modes: read `r`, write `w`, append `a`
- Selectors: text `t`, binary `b`
- Prefer `with open(...) as f:` so files always close

### File-Like Objects

- Any object that supports the needed file operations can stand in for a real file.
- Use EAFP when the exact protocol is incomplete.

### Generated Outputs

- Scripts may create `wasteland.txt`, `recman*.dat`, and `mandel.bmp` beside this folder.
- Those patterns are gitignored — safe to re-run locally.

## How To Run

```bash
python 09_io_file/02_writing_file.py
python 09_io_file/03_reading_file.py
python 09_io_file/10_with_file.py
python 09_io_file/11_binary_file.py
python 09_io_file/13_context_managers.py
```

## Try It Yourself

- Rewrite `05_iterating_file.py` to accept a path via `argparse`.
- Add a Recaman writer that stops after `n` terms using `islice` (already close — vary `n`).
- Use `contextlib.closing` (or a custom context manager) around a socket-like object.

## Navigation

Previous: [Chapter 8: Classes](../08_classes/README.md)  
Next: —
