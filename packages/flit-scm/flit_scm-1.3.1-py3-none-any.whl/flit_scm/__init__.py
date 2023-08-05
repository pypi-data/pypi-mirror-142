from flit_core import buildapi # Make Flit's build backend available as "flit_scm:buildapi"
from setuptools_scm import get_version
import toml

from ._version import version as __version__


try:
    pyproject = toml.load('pyproject.toml')
except OSError:
    pass # Do nothing if unable to access `pyproject.toml`
else:
    try:
        setuptools_scm_config = pyproject['tool']['setuptools_scm']
    except KeyError:
        pass # Do nothing if `setuptools_scm` is not configured in `pyproject.toml`
    else:
        get_version(**setuptools_scm_config)
