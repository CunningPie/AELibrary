from pathlib import Path
from aelib import io

import pytest
import numpy as np
import pandas as pd


DATA_DIR = Path(__file__).resolve().parent / "data"
AEFILE1 = DATA_DIR / "aefile1.txt"
AEFILE2 = DATA_DIR / "aefile2.txt"
AEFILE3 = DATA_DIR / "aefile3.txt"


@pytest.mark.parametrize("filename, expected", [(AEFILE1, 45), (AEFILE2, 80)])
def test_open_file_count(filename, expected):
    output = io.open_file(filename)

    assert len(output) == expected


def test_open_file_content():
    output = io.open_file(AEFILE3)
    expect = pd.DataFrame({
        'Id': ["le", "ht", "ht", "ht", "ht", "ev"],
        'DSET': ["6", "7", "8", "10", "11", "27"],
        'HHMMSS': ["06:51:52", "06:51:52", "06:51:52", "06:51:52", "06:51:52", "06:51:52"],
        'MSEC': ["221.4381", "221.4581", "221.6773", "222.0477", "222.4279", "227.2329"],
        'CHAN': ["13", "14", "17", "12", "18", "2"],
        'A': ["50.5", "61.4", "47.1", "47.9", "55.8", "42.6"],
        'CNTS': ["3", "44", "12", "15", "14", "2"],
        'DT1X': [np.nan, "20.0", "239.2", "609.6", "989.8", np.nan]
    })

    assert output.equals(expect)


@pytest.mark.parametrize("filename, expected", [(AEFILE1, ["Id", "DSET", "HHMMSS", "MSEC", "CHAN", "A", "CNTS", "DT1X"]),
                                                (AEFILE2, ["Num", "Event", "Time", "Channel", "Amplitude"])])
def test_open_file_header_params(filename, expected):
    output = io.open_file(filename)

    assert list(output.columns) == expected
