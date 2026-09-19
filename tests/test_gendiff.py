from pathlib import Path

from gendiff import generate_diff
from gendiff.scripts.gendiff import main


def get_fixture_path(file_name):
    return Path(__file__).parent / "test_data" / file_name


def test_generate_diff():
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")
    expected = get_fixture_path("result.txt").read_text().strip()

    actual = generate_diff(file1, file2)

    assert actual == expected


def test_main(monkeypatch, capsys):
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")

    monkeypatch.setattr(
        "sys.argv",
        ["gendiff", str(file1), str(file2)],
    )

    main()

    captured = capsys.readouterr()

    expected = get_fixture_path("result.txt").read_text().strip()

    assert captured.out.strip() == expected