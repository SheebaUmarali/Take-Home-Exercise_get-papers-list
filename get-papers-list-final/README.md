# get-papers-list

A Python CLI tool to fetch PubMed papers authored by non-academic affiliations.

## Installation

### From TestPyPI

```bash
pip install -i https://test.pypi.org/simple/ get-papers-list
```

### From PyPI (once published)

```bash
pip install get-papers-list
```

## Usage

```bash
get-papers-list "cancer research" -f output.csv
```

Options:
- `-f <filename>`: Export results to CSV
- `-d`: Enable debug logs

## Development

This project uses [Poetry](https://python-poetry.org/) for packaging.

```bash
poetry install
poetry run pytest
```

## CI/CD and Publishing

GitHub Actions handles publishing:

- **Dev branch**: Publishes to **TestPyPI**
- **Tagged release on main**: Publishes to **PyPI**

Secrets required:
- `TEST_PYPI_TOKEN`
- `PYPI_TOKEN`

## LLM Tool Usage

As part of the project exercise, we leveraged an LLM to bootstrap project structure, unit tests, and workflow automation. Full conversation link will be shared in submission.

