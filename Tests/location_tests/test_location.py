from pathlib import Path

import pandas as pd

from aelib import location, io


DATA_DIR = Path(__file__).resolve().parent / "data"
WAVES = DATA_DIR / "K2_waves.txt"
WAVES2 = DATA_DIR / "waves2.txt"
WAVE = DATA_DIR / "wave.txt"
WAVE2 = DATA_DIR / "wave2.txt"
COORDS = DATA_DIR / "K2_coords.txt"
COORDS2 = DATA_DIR / "coords2.txt"

location.WIDTH = 520


def test_get_wave():
    data = io.open_file(WAVES)
    output = location.get_wave(data, 17)

    assert len(output) == 8


def test_dist():
    x1 = 0
    y1 = 0
    x2 = 7
    y2 = 4

    output = location.dist(x1, y1, x2, y2)
    print(output)

    assert output == 65 ** 0.5


def test_speed_eq():
    x = 0
    y = 0
    x1 = 7
    y1 = 4
    x2 = 11
    y2 = 8
    t1 = 0
    t2 = 0.2

    output = location.speed_eq(x, y, x1, y1, x2, y2, t1, t2)

    assert output == abs((7 ** 2 + 4 ** 2) ** 0.5 - (11 ** 2 + 8 ** 2) ** 0.5) / 0.2


def test_take_channels_coords():
    data = io.open_file(WAVE)
    coords = pd.read_csv(COORDS, sep=" ")
    expect = [[76.0, 342.0], [105.0, 410.0], [187.0, 50.0]]

    output = location.take_channels_coords(data, coords, 3)

    assert output == expect


def test_localize_wave():
    data = io.open_file(WAVE2)
    coords = pd.read_csv(COORDS2, sep=" ")

    output = location.localize_wave(data, coords, 0, 1000, 3, 0.01)

    assert output == [[2.6, -1.8, 5.06]]


def test_localize():
    data = io.open_file(WAVES2)
    coords = pd.read_csv(COORDS2, sep=" ")

    output = location.localize(data, coords, 0, 1000, 424, 3, 0.01)

    assert output == [[2.6, -1.8, 5.06], [2.6, 4.2, 5.06], [10.6, -1.8, 5.06], [10.6, 4.2, 5.06]]
