import logging
import re
import sys
from vtb_py_logging.configure import initialize_logging
from vtb_py_logging.log_extra import push_extra
from vtb_py_logging.request_id import RequestId
from django.conf import settings


def request_id_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        request_id = request.headers.get("X-Request-Id")
        if not request_id:
            request_id = RequestId.make(prefix=settings.REQUEST_ID_PREFIX)
        push_extra(request_id=request_id)
        return get_response(request)

    return middleware


def replace_suffix(name, suffix):
    return re.sub(r"(\w+)(\.\w+)?$", fr"\1.{suffix}", name, count=1)


def setup_logging(config, *, force=False, suffix=None):
    if force:
        initialize_logging._cleanup()

    name = settings.LOGGING_APP_NAME
    if suffix:
        name = replace_suffix(name, suffix)
    else:
        # check that celery worker is started
        for arg in sys.argv:
            if "celery" in arg or arg == "worker" or arg == "beat":
                name = replace_suffix(name, "tasks")

    initialize_logging(name)

    # suppress pika logs
    pika_logger = logging.getLogger("pika")
    if not settings.DEBUG:
        pika_logger.setLevel(logging.WARNING)

    logging.getLogger('urllib3').setLevel("WARNING")
