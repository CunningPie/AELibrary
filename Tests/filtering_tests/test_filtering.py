from pathlib import Path
from aelib import filtering
from aelib import io

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA1 = DATA_DIR / "aefile1.txt"
DATA2 = DATA_DIR / "aefile2.txt"


def test_filter_ev():
    output = io.open_file(DATA1)
    output = filtering.filter_ev(output)

    assert "ev" not in output["Id"]


def test_filter_threshold():
    output = filtering.filter_threshold(io.open_file(DATA1), 40, 100)

    assert len(output) == 21


def test_filter_signal_events_number():
    data = io.open_file(DATA1)
    output = filtering.filter_signal_events_number(data, 4)
    expect = pd.DataFrame({
        'Id': ["le", "ht", "ht", "ht", "ht", "le", "ht", "ht", "ht", "ht"],
        'DSET': ["6", "7", "8", "10", "11", "57", "58", "59", "60", "62"],
        'HHMMSS': ["06:51:52", "06:51:52", "06:51:52", "06:51:52", "06:51:52", "06:51:53", "06:51:53",
                   "06:51:53", "06:51:53", "06:51:53"],
        'MSEC': ["221.4381", "221.4581", "221.6773", "222.0477", "222.4279", "137.6557", "137.7154", "137.7474",
                 "137.8374", "137.8764"],
        'CHAN': ["13", "14", "17", "12", "18", "4", "5", "2", "1", "7"],
        'A': ["50.5", "61.4", "47.1", "47.9", "55.8", "65.6", "56.5", "50.9", "55.0", "43.7"],
        'CNTS': ["3", "44", "12", "15", "14", "23", "12", "8", "37", "4"],
        'DT1X': [np.nan, "20.0", "239.2", "609.6", "989.8", np.nan, "59.7", "91.7", "181.7", "220.7"]
    })

    assert output.equals(expect)


def test_filter_electromagnetic():
    output = filtering.filter_electromagnetic(io.open_file(DATA2))
    expect = pd.DataFrame({
        'Id': ["le", "ht", "ht", "ht", "ht"],
        'DSET': ["57", "58", "59", "60", "62"],
        'HHMMSS': ["06:51:53", "06:51:53", "06:51:53", "06:51:53", "06:51:53"],
        'MSEC': ["137.6557", "137.7154", "137.7474", "137.8374", "137.8764"],
        'CHAN': ["4", "5", "2", "1", "7"],
        'A': ["65.6", "56.5", "50.9", "55.0", "43.7"],
        'CNTS': ["23", "12", "8", "37", "4"],
        'DT1X': [np.nan, "59.7", "91.7", "181.7", "220.7"]
    })

    assert output.equals(expect)
