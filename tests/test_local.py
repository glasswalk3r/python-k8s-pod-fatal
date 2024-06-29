import pytest
import tempfile
import os

from kubernetes.pod.exceptions import Fatal


def test_basic():
    issubclass(Fatal, RuntimeError)


def test_fatal():
    with pytest.raises(Fatal, match=r'^A fatal error occurred:'):
        try:
            1 / 0
        except ZeroDivisionError as e:
            raise Fatal(str(e))


def test_default_log_file():
    instance = Fatal('some error')
    assert instance.log_file == '/dev/termination-log'


def test_fatal_with_tmp_file():
    tmp_fh = tempfile.NamedTemporaryFile(delete=False, delete_on_close=False)
    tmp_file_path = tmp_fh.name

    try:
        raise Fatal('winter is coming', tmp_file_path)
    except Exception as e:
        expected = 'A fatal error occurred: winter is coming'
        assert str(e) == expected
        assert e.log_file == tmp_file_path
        with open(tmp_file_path, 'r') as fp:
            data = fp.read()

        assert data == expected
    finally:
        tmp_fh.close()
        os.unlink(tmp_file_path)
