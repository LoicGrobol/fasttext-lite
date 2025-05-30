import filecmp
import pathlib
from fasttextlt.fasttext import FastText


def test_load_save_idempotency(model_path: pathlib.Path, tmp_path: pathlib.Path):
    save_path = tmp_path / "model.bin"
    f = FastText.load_model(model_path, full_model=True)
    f.save_model(save_path)
    assert filecmp.cmp(model_path, save_path)
