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


def test_generate_diff_yaml():
    file1 = get_fixture_path("file1.yml")
    file2 = get_fixture_path("file2.yml")
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


def test_main_with_format(monkeypatch, capsys):
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")

    monkeypatch.setattr(
        "sys.argv",
        [
            "gendiff",
            "-f",
            "stylish",
            str(file1),
            str(file2),
        ],
    )

    main()

    captured = capsys.readouterr()

    expected = get_fixture_path("result.txt").read_text().strip()

    assert captured.out.strip() == expected


def test_generate_diff_plain():
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")

    expected = (
        "Property 'follow' was removed\n"
        "Property 'proxy' was removed\n"
        "Property 'timeout' was updated. From 50 to 20\n"
        "Property 'verbose' was added with value: true"
    )

    actual = generate_diff(file1, file2, "plain")

    assert actual == expected


def test_generate_diff_plain_values():
    file1 = get_fixture_path("plain_file1.json")
    file2 = get_fixture_path("plain_file2.json")

    expected = (
        "Property 'follow' was updated. From false to null\n"
        "Property 'host' was updated. "
        "From 'old.example.com' to 'hexlet.io'\n"
        "Property 'timeout' was updated. From 50 to 20\n"
        "Property 'value' was removed\n"
        "Property 'verbose' was added with value: true"
    )

    actual = generate_diff(file1, file2, "plain")

    assert actual == expected
