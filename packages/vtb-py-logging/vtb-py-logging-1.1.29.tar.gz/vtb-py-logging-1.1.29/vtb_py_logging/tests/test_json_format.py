import json
import logging

from vtb_py_logging import log_extra
from vtb_py_logging.tests.utils import init_log_for_test


class TestJSONFormat:

    def test_json_output_format_without_context(self):
        with init_log_for_test('test-formats') as log_reader:
            message = 'Test %s log message json format %s context vars'
            logging.info(message, 'info', 'without')

            records = list(log_reader)
            record = json.loads(records[0])
            assert record['level'] == 'INFO'
            assert record['payload']['message'] == message % ("info", "without")

    def test_json_output_format_with_context(self):
        APP_NAME = 'test-formats'
        LOG_LEVELS = ['info', 'warning', 'error', 'debug']

        with init_log_for_test('test-formats2', level="debug") as log_reader:
            message = 'Test %s log message json format %s context vars'
            tags = ["TEST", "TEST_TAG"]
            request_id = "some-request-id"
            with log_extra.log_extra(request_id=request_id, progname=APP_NAME, tags=tags):
                for level in LOG_LEVELS:
                    log_method = getattr(logging, level)
                    log_method(message, level, 'with')

                for level in LOG_LEVELS:
                    record = next(log_reader)
                    record = json.loads(record)
                    assert record.get('tags') == tags
                    assert record.get('level') == level.upper()
                    assert record.get('request_id') == request_id
                    assert record.get('progname') == APP_NAME
                    assert record['payload']['message'] == message % (level, "with")

                other_records = list(log_reader)
