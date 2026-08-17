# Flavinus Py Life

An implementation of Conway's Game of Life to practice Python.

* https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
* https://realpython.com/conway-game-of-life-python/

## Setup

Systrem requirments: linux, python3, python3-pip

See `script/dev_setup.sh` for first setup

## Run

Be sure venv is enabled: `source .venv/bin/activate`

Then run: `python3 src/main.py`

Edit main.py to handle seed and view mode (ncurses or pygame)


## Seed samples

See patterns and utils files.

```
cells = get_pattern("blinker", 45, 25)

cells = get_pattern("square41", 45, 25)

cells = rotate(rotate(get_pattern("vaissel", 20, 20)))

cells = set()
cells = cells.union(get_pattern("vaissel", 25, 45))
cells = cells.union(get_pattern("vaissel", 20, 45))
cells = cells.union(get_pattern("vaissel", 25, 50))
cells = cells.union(get_pattern("vaissel", 20, 50))

cells = set()
cells = cells.union(get_pattern("beacon", 25, 45))
cells = cells.union(get_pattern("toad", 25, 45))
```

---
# Tools

Linter:
    `pylint src/*.py`

Linter auto-corrections:
    `autopep8 --in-place --aggressive --aggressive src/*.py`
