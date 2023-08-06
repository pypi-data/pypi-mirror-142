import pytest
from sqlalchemy_ibmi.base import IBMiDb2Dialect


def test_foo():
    opts = {
        'invalid': None
    }
    with pytest.raises(ValueError):
        IBMiDb2Dialect.map_connect_opts(opts)
