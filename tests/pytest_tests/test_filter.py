import os
os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/tests/test_hello_7"
import pytest
from pytest_tests import setup_tests
import filter as Filter


def test__can_get_filtered_buffers_list():
    try:
        assert set(['vg_session_log', 'vg_base']) == set(Filter.FILTERED_BUFFERS_LIST)
    except Exception as ex:
        pytest.fail("error in filter tests: " + str(ex))

def test__can_get_filtered_buffers_file_list():
    try:
        assert set(['/work/tide/defaults/filters/vg_base.py',
                    '/work/tide/defaults/filters/vg_session_log.py']) == set(Filter.FILTERED_BUFFERS_FILE_LIST)
    except Exception as ex:
        pytest.fail("error in filter tests: " + str(ex))

def test__filter_lines_for_buffer():
    try:
        buffer_name = 'vg_base'
        lines_to_filter = "\\tthis is a test line with one apostrophe ' becoming two\\n"
        result = Filter.filter_lines_for_buffer(lines_to_filter, buffer_name)
        assert result == ["    this is a test line with one apostrophe '' becoming two"]
    except Exception as ex:
        pytest.fail("error in filter tests: " + str(ex))
