import json
import os
import logging
import platform
import tempfile

from pathlib import Path
from vtb_py_logging.tests.utils import init_log_for_test
from vtb_py_logging.log_config import LogConfigure


class TestEnvironVars:
    def test_environ_vars(self):
        logdir = tempfile.mkdtemp("-log", "vtb-logging-")
        environ = {
            'LOG_FORMAT': 'JSON',
            'LOG_FILENAME': 'custom_name_log.log',
            'LOG_DIR': logdir
        }
        with init_log_for_test("test-environ-vars", environ=environ) as log_reader:
            message = 'Test environ vars'
            logging.info(message)

            # TODO
            # # Check file path by environ vars
            # assert os.path.exists(self.log_path)
            # assert self.log_path.endswith('custom_name_log.log')
            # tempdir = Path("/tmp" if platform.system() == "Darwin" else tempfile.gettempdir())
            # assert self.log_path.startswith(str(tempdir))

            records = list(log_reader)
            record = json.loads(records[0])
            assert record['level'] == 'INFO'
            assert record['payload']['message'] == message
