import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from seeds.seed_db import load_units_data


def test_load_units_data_reads_json_seed_file():
    data = load_units_data()

    assert isinstance(data, list)
    assert data[0]["unit_number"] == 7
    assert data[0]["title"] == "MIND (La Mente)"
    assert "activities" in data[0]
    assert "study" in data[0]["activities"]
    assert data[0]["activities"]["study"][0].startswith("Lee artículos")
