from pathlib import Path
from aelib import classification
from aelib import io


DATA_DIR = Path(__file__).resolve().parent / "data"
DATA1 = DATA_DIR / "aefile1.txt"
DATA2 = DATA_DIR / "aefile2.txt"


def test_get_waves():
    data = io.open_file(DATA1)
    waves = classification.get_waves(data)

    assert 1


def test_count_pair_pearson():
    data = io.open_file(DATA1)
    #classification.count_pearson(data)

    assert 1


def test_create_pearson_matrix():
    data = io.open_file(DATA1)
    waves = classification.get_waves(data)
    expect = [[1.0, -0.119, 0.301, -0.337], [-0.119, 1.0, 0.908, 0.749], [0.301, 0.908, 1.0, 0.426], [-0.337, 0.749, 0.426, 1.0]]

    output = classification.create_pearson_matrix(waves)

    assert output == expect


def test_create_super_signal():
    data = io.open_file(DATA2)
    waves = classification.get_waves(data)
    expect = [[82.1, 221.4381], [99.8, 221.4581], [76.5, 221.6773], [77.8, 222.0477], [90.9, 222.4279]]

    output = classification.create_super_signal(waves)

    assert output == expect


def test_create_super_signals():
    data = io.open_file(DATA2)
    expect = [[[82.1, 221.4381], [99.8, 221.4581], [76.5, 221.6773], [77.8, 222.0477], [90.9, 222.4279]],
              [[82.1, 221.4381], [99.8, 221.4581], [76.5, 221.6773], [77.8, 222.0477], [90.9, 222.4279]],
              [[82.1, 221.4381], [99.8, 221.4581], [76.5, 221.6773], [77.8, 222.0477], [90.9, 222.4279]],
              [[82.1, 221.4381], [99.8, 221.4581], [76.5, 221.6773], [77.8, 222.0477], [90.9, 222.4279]]]

    output = classification.create_super_signals(data)

    assert output == expect