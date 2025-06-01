import filecmp
import pathlib
from fasttextlt.fasttext import FastText, FastTextVocab


def test_load_save_idempotency(model_path: pathlib.Path, tmp_path: pathlib.Path):
    save_path = tmp_path / "model.bin"
    f = FastText.load_model(model_path, full_model=True)
    f.save_model(save_path)
    assert filecmp.cmp(model_path, save_path)


def test_vocab_load_save_idempotency(model: FastText, tmp_path: pathlib.Path):
    save_path_first = tmp_path / "vocab.1.json"
    save_path_second = tmp_path / "vocab.2.json"
    model.vocabulary.save(save_path_first)
    reloaded = FastTextVocab.load(save_path_first)
    reloaded.save(save_path_second)
    assert filecmp.cmp(save_path_first, save_path_second)