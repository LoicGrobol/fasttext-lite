import filecmp
import pathlib
from fasttextlt.format import load, Model, save


def test_load_save_idempotency(model_path: pathlib.Path, tmp_path: pathlib.Path):
    save_path = tmp_path / "model.bin"
    with open(model_path, "rb") as in_stream:
        m = load(in_stream, full_model=True)
    assert isinstance(m, Model)
    with open(save_path, "wb") as out_stream:
        save(m, out_stream)
    assert filecmp.cmp(model_path, save_path)
