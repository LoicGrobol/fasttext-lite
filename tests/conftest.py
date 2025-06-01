import pathlib

import pytest

from hypothesis import settings

import fasttextlt.fasttext
import fasttext
import fasttext.FastText

settings.register_profile("default", print_blob=True)
settings.load_profile("default")


@pytest.fixture(scope="session")
def test_data_dir() -> pathlib.Path:
    return pathlib.Path(__file__).parent / "fixtures"


# TODO: figure out a way to run tests on big models as an option
# TODO: figure out a ~nice~ way to test compressed models for parity
@pytest.fixture(
    params=[
        "smol_model.bin",
        # "smol_model.bin.gz",
        "smol_model_nochar.bin",
        # "cc.cy.300.bin",
    ],
    scope="session",
)
def model_path(test_data_dir: pathlib.Path, request) -> pathlib.Path:
    return test_data_dir / request.param


@pytest.fixture(scope="session")
def models(
    model_path: pathlib.Path,
) -> tuple[fasttextlt.fasttext.FastText, fasttext.FastText._FastText]:
    ft_model = fasttext.load_model(str(model_path))
    ftlt_model = fasttextlt.fasttext.FastText.load_model(model_path)

    return ftlt_model, ft_model


@pytest.fixture(scope="session")
def model(
    model_path: pathlib.Path,
) -> fasttextlt.fasttext.FastText:
    return fasttextlt.fasttext.FastText.load_model(model_path)
