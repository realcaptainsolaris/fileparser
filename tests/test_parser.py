from pathlib import Path
import pytest
from fileparser.parser import parse, FileInfo


def test_parse_valid_file(tmp_path: Path):
    testfile = tmp_path / "example.txt"
    testfile.write_text("hello")

    info = parse(testfile)
    assert isinstance(info, FileInfo)
    assert info.name == "example"
    assert info.suffix == ".txt"
    assert info.type == "txt"


def test_parse_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        parse("not_here.txt")
