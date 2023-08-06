import os
import logging

from vtb_py_logging import log_extra
from vtb_py_logging.tests.utils import init_log_for_test
from vtb_py_logging.log_config import LogConfigure


class TestTaggedFormat:
    def test_tagged_output_format_without_context(self):
        """
        Test simple output log format without context vars (request_id, tags, e.t.c)
        """
        with init_log_for_test("tagged", log_output='TAGGED') as log_readers:
            message = 'Test %s log message simple format %s context vars'
            logging.info(message, 'info', 'without')

            logs = list(log_readers)
            record = logs[0]
            assert record.split()[2] == 'INFO'
            assert message % ('info', 'without') in record

    def test_tagged_output_format_with_context(self):
        """
        Test simple output log format with context vars (request_id, tags, e.t.c)
        """
        LOG_LEVELS = ("info", "warning", "error")
        with init_log_for_test("tagged", log_output='TAGGED') as log_readers:
            message = 'Test %s log message simple format %s context vars'
            tags = ["TEST", "TEST_TAG"]
            request_id = "some-request-id"
            with log_extra.log_extra(request_id=request_id, tags=tags):
                for level in LOG_LEVELS:
                    log_method = getattr(logging, level)
                    log_method(message, level, 'with')

            for level in LOG_LEVELS:
                record = next(log_readers)
                splitted_title = record.split()
                r_date, r_time, r_level, req_id, tag_1, tag_2 = splitted_title[:6]

                # Check context vars
                assert r_level == level.upper()
                assert req_id[1:-1] == request_id
                assert tag_1[1:-1] == tags[0]
                assert tag_2[1:-1] == tags[1]
                assert message % (level, 'with') in record

            other_logs = list(log_readers)
