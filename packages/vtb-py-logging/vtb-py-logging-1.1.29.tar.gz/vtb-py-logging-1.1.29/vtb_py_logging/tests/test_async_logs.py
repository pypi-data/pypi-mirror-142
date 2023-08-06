import json
import asyncio
import logging

from vtb_py_logging.tests.utils import init_log_for_test
from vtb_py_logging import log_extra
from vtb_py_logging.log_config import LogConfigure


class TestAsyncLogs:
    async def alog_3rd(self, message: str):
        logging.info(f'{message} 3rd depth')

    async def alog_2nd(self, message: str):
        logging.info(f'{message} 2nd depth')
        await asyncio.Task(self.alog_3rd(message))

    async def alog_1st(self, message: str):
        logging.info(f'{message} 1st depth')
        await asyncio.sleep(1)
        await self.alog_2nd(message)

    def test_async_log(self):
        APP_NAME = "test-async-log"
        with init_log_for_test(APP_NAME) as log_reader:
            message = 'Test info async log message'
            tags = ["TEST", "TEST_TAG"]
            request_id = "some-request-id"
            with log_extra.log_extra(request_id=request_id, progname=APP_NAME, tags=tags):
                asyncio.run(self.alog_1st(message))

                records = list(log_reader)
                assert len(records) == 3
                async_depths = ['1st', '2nd', '3rd']
                for x in range(len(async_depths)):
                    depth = async_depths[x]
                    record = records[x]
                    assert json.loads(record)
                    record = json.loads(record)
                    assert record.get('tags') == tags
                    assert record.get('level') == 'INFO'
                    assert record.get('request_id') == request_id
                    assert record.get('progname') == APP_NAME
                    assert record.get('payload').get('message') == f"{message} {depth} depth"

