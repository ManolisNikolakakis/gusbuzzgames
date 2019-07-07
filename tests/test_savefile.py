from pathlib import Path
from pytest import fixture

from .context import Savefile
from .context import settings


@fixture
def savefile():
    savefile = Savefile()
    return savefile


def test_str(savefile):
    expected_path = Path('.') / settings.SAVE_LOCATION
    assert str(savefile) == f'{expected_path.resolve()}'


def test_repr(savefile):
    expected_path = Path('.') / settings.SAVE_LOCATION
    assert repr(savefile) == f'{expected_path.resolve()}'


def test_save(savefile):
    savefile.high_score = 5
    savefile.save_file()
    expected_path = Path('.') / settings.SAVE_LOCATION
    assert int(expected_path.read_text()) == 5
