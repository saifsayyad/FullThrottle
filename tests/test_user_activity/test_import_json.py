import subprocess
import pytest


def test_import_valid_json():
    """
    Called the ``import_data_json`` management command with valid JSON file.

    It is asserted that no error is raised.
    :return:
    """
    output = subprocess.check_output(
        ["python", "manage.py", "import_data_json", "tests/test_user_activity/Test JSON.json"])
    assert output.decode() == ""


def test_import_invalid_json():
    """
    Called the ``import_data_json`` management command with JSON file with invalid schema

    It is asserted that JSON schema error is raised.
    :return:
    """
    with pytest.raises(subprocess.CalledProcessError) as e:
        subprocess.check_output(
            ["python", "manage.py", "import_data_json", "tests/test_user_activity/Test_JSON_invalid.json"])
        assert "ERROR JSON schema not correct" in str(e.value)
