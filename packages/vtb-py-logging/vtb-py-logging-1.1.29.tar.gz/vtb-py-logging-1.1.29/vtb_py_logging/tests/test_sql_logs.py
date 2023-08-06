import json
import logging

from vtb_py_logging.tests.utils import init_log_for_test
from vtb_py_logging import log_extra
from vtb_py_logging.log_config import LogConfigure


class TestSQLlogs:
    def test_sql_log_with_context(self):
        with init_log_for_test("test-sql-logs", log_sql=True) as log_reader:
            message = ''
            tags = ["TEST", "TEST_TAG"]
            request_id = "some-request-id"
            sql = "SELECT * from test"
            params = {"some_param": "some value"}
            duration = 0.123
            with log_extra.log_extra(request_id=request_id, tags=tags):
                logger = logging.getLogger("django.db.backends")
                logger.warning(message, extra={
                                   "duration": duration,
                                   "sql": sql,
                                   "params": params
                                })
                record = list(log_reader)[0]
                record = json.loads(record)
                assert record['tags'] == tags
                assert record['level'] == 'WARNING'
                assert record['request_id'] == request_id
                message = record['payload']['message']
                assert "SELECT" in message
                assert str(params) in message
                assert str(duration) in message
                extra = record['payload']['extra']
                assert extra['params'] == params
                assert extra["sql"] == sql
                assert extra['duration'] == duration
