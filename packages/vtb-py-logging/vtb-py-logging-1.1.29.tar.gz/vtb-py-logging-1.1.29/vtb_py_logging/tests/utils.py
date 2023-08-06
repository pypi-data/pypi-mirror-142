import os
import shutil
import contextlib
import logging
from vtb_py_logging import log_extra
from vtb_py_logging.configure import initialize_logging
from vtb_py_logging.log_config import LogConfigure


def log_reader(log_path):
    with open(log_path, "r") as f:
        while line := f.readline():
            yield line


def cleanup_handlers():
    for logger in logging.Logger.manager.loggerDict.values():
        if not isinstance(logger, logging.PlaceHolder):
            for handler in logger.handlers:
                handler.close()
            logger.handlers = []

    for handler in logging.root.handlers:
        handler.close()


@contextlib.contextmanager
def init_log_for_test(app_name, log_output="JSON", environ=None, **kwargs):
    # setup environ vars
    original_environ = {}
    for key, val in (environ or {}).items():
        original = os.environ.get(key)
        if original is not None:
            original_environ[key] = original
        os.environ[key] = val

    log_config = LogConfigure(app_name=app_name, log_output=log_output, cleanup=True,
                              **kwargs)

    shutil.rmtree(log_config.directory, ignore_errors=True)

    if hasattr(initialize_logging.__wrapped__, "_initialized"):
        delattr(initialize_logging.__wrapped__, "_initialized")
    initialize_logging(config=log_config)
    log_extra.init_extra_logger()

    try:
        yield log_reader(log_config.get_filename(""))
    finally:
        cleanup_handlers()
        # restore environ
        os.environ.update(original_environ)
        shutil.rmtree(log_config.directory)
