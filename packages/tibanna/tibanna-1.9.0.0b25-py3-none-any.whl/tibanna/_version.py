"""Version information."""
import tomlkit
from pathlib import Path


def _get_project_meta():
    toml_path = Path(__file__).parent.parent.joinpath('pyproject.toml')
    with open(toml_path) as pyproject:
        file_contents = pyproject.read()

    return tomlkit.parse(file_contents)['tool']['poetry']

pkg_meta = _get_project_meta()

__version__ = str(pkg_meta['version'])

