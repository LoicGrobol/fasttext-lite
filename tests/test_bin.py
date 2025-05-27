import pathlib
from fasttextlt.fasttext_bin import load, Model


def test_load_model(model_path: pathlib.Path):
    with open(model_path, "rb") as in_stream:
        m = load(in_stream)
    assert isinstance(m, Model)