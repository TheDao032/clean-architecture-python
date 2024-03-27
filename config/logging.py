import json
import logging
from pprint import pformat
from types import FrameType
from typing import cast

from loguru import logger


class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentation.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def format_record_development(record: dict) -> str:
    trace_id = (
        record["extra"]["trace_id"]
        if record["extra"].get("trace_id") is not None
        else ""
    )
    format_string = (
        "<level>{level}</level> "
        + f"<yellow>{trace_id}</yellow>"  # noqa
        + " <magenta>{thread.name}-{thread.id}</magenta> <cyan>{name}</cyan>:<cyan>{function}</cyan>:<red>{line}</red> <level>{message}</level>"  # noqa
    )
    if record["extra"].get("payload") is not None:
        record["extra"]["payload"] = pformat(
            record["extra"]["payload"], indent=4, compact=True, width=88
        )
        format_string += "\n<level>{extra[payload]}</level>"

    format_string += "{exception}\n"
    return format_string


def serialize(payload: dict) -> str:
    return json.dumps(
        payload,
        separators=(",", ":"),
        sort_keys=True,
        ensure_ascii=False,
        indent=None,
        default=str,
    )


def format_record_production(record: dict) -> str:
    trace_id = (
        record["extra"]["trace_id"]
        if record["extra"].get("trace_id") is not None
        else ""
    )

    audit = {
        "time": f"{record['time']}",  # time:YYYY-MM-DDHH:mm:ssZ
        "log_level": f"{record['level']}",
        "thread_id": f"http-8080-{record['thread']}",
        "source": f"{record['file']}-{record['line']}",
        "execution_time": f"{record['elapsed']}",
        "message": record["message"],
    }

    if trace_id:
        audit["trace_id"] = f"{trace_id}"

    if record["exception"] is not None:
        audit["message"] = record["exception"]

    record["extra"]["serialized"] = serialize(audit)
    return "{extra[serialized]}\n"
