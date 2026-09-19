### Hexlet tests and linter status:
[![Actions Status](https://github.com/elzaelsa/qa-auto-engineer-python-project-241/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/elzaelsa/qa-auto-engineer-python-project-241/actions)

### Gendiff status
[![Python CI](https://github.com/elzaelsa/qa-auto-engineer-python-project-241/actions/workflows/pyci.yml/badge.svg)](https://github.com/elzaelsa/qa-auto-engineer-python-project-241/actions/workflows/pyci.yml)

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=elzaelsa_qa-auto-engineer-python-project-241)](https://sonarcloud.io/summary/new_code?id=elzaelsa_qa-auto-engineer-python-project-241)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=elzaelsa_qa-auto-engineer-python-project-241&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=elzaelsa_qa-auto-engineer-python-project-241)

# Gendiff

Gendiff - это утилита командной строки для сравнения конфигурационных файлов.
Утилита поддерживает файлы JSON и YAML и отображает различия в удобном формате.

## Requirements
Python 3.10 or higher

uv

## Installation

Clone the repository and install the project dependencies:

git clone https://github.com/elzaelsa/qa-auto-engineer-python-project-241.git

cd qa-auto-engineer-python-project-241

make install

## Usage

Сравнение 2-х json файлов:

gendiff tests/test_data/file1.json tests/test_data/file2.json

Сравнение 2-х YAML файлов YAML:

gendiff tests/test_data/file1.yml tests/test_data/file2.yml

stylish формать испольщуется по умолчанию.

Также можно явно указать формат:

gendiff -f stylish tests/test_data/file1.json tests/test_data/file2.json

## Development

Run the linter:

make lint

Run tests:

make test

Run tests with coverage:

make test-coverage

## Демонстрация работы

[![asciicast](https://asciinema.org/a/92iiilvG5mQUgtjH.svg)](https://asciinema.org/a/92iiilvG5mQUgtjH)

[![asciicast](https://asciinema.org/a/SQTaKDVWCShE5Vla.svg)](https://asciinema.org/a/SQTaKDVWCShE5Vla)

