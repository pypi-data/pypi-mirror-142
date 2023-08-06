import logging

from vtb_py_logging import log_extra
from vtb_py_logging.tests.utils import init_log_for_test
from vtb_py_logging.log_config import LogConfigure


class TestTreaceback:
    def test_tagged_output_with_traceback(self):
        """
        Test simple output log format with traceback
        """
        with init_log_for_test("test-traceback", log_output='TAGGED') as log_reader:
            message = 'Test Traceback log'
            tags = ["TEST", "TEST_TAG"]
            request_id = "some-request-id"
            with log_extra.log_extra(request_id=request_id, tags=tags):
                try:
                    1 // 0
                except:
                    logging.exception(message)

            logs = list(log_reader)
            record = logs[0]
            r_date, r_time, r_level, req_id, tag_1, tag_2 = record.split()[:6]

            # Check context vars
            assert r_level == 'ERROR'
            assert req_id[1:-1] == request_id
            assert tag_1[1:-1] == tags[0]
            assert tag_2[1:-1] == tags[1]

            assert message in record
            assert 'Traceback' in logs[1]
