from pathlib import Path
import numpy as np

import aelib.clusterization as cl

DATA_DIR = Path(__file__).resolve().parent / "data"
AEFILE = DATA_DIR / "data.txt"
SENSORS = DATA_DIR / "sensors.txt"
POINTS = DATA_DIR / "points.txt"


def test_get_radius():
    with open(POINTS, 'r') as f:
        data = np.array([[float(num) for num in line.split(' ')] for line in f])

    output = cl.get_radius(data)

    assert output == 5


def test_clusterization():
    with open(AEFILE, 'r') as f:
        data = np.array([[float(num) for num in line.split('\t')] for line in f])
    with open(SENSORS, 'r') as f:
        sensors = np.array([[int(num) for num in line.split(' ')] for line in f])

    cl.init(data, -185, -170, -90, -80)
    output = cl.clusterization(data)

    assert len(set(output.labels_)) - (1 if -1 in output.labels_ else 0) == 5
