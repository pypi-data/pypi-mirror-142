# -*- coding: utf-8 -*-
import logging
from typing import Optional
from logging import Handler
import sentry_sdk


__all__ = ['SentryStreamHandler']


class SentryStreamHandler(Handler):

    """
    SentryStreamHandler

    ------------
    description: 
    send msg to sentry

    Parameters: 

    ::param token : sentry-token
    ::param host : sentry-host
    ::param port : sentry-port
    ::param project : sentry-project
    ::param level : logging-level
    ::param kwargs : sentry-kwargs

    """
    terminator = '\n'

    def __init__(self,
                 token,  # type: Optional[str]
                 host,  # type: Optional[str]
                 port,  # type: Optional[int]
                 project,  # type: Optional[int]
                 *,
                 level=logging.NOTSET,
                 **kwargs
                 ):

        self.level = level
        super(SentryStreamHandler, self).__init__(level)
        dsn = self._dsn(token, host, port, project)
        self.sentry_sdk = sentry_sdk
        sentry_sdk.init(dsn=dsn, **kwargs)
        self.sentry_sdk.set_level(level)

    def flush(self):
        """
        Flushes the stream.
        """
        self.acquire()
        try:
            if hasattr(self.sentry_sdk, "flush"):
                self.sentry_sdk.flush()
        finally:
            self.release()

    def _dsn(self, token, host, port, project):

        _fmt = "http://{token}@{host}:{port}/{project}"
        return _fmt.format(token=token, host=host, port=port, project=project)

    def emit(self, record):
        """
        Emit a record.

        If a formatter is specified, it is used to format the record.
        The record is then written to the stream with a trailing newline.  If
        exception information is present, it is formatted using
        traceback.print_exception and appended to the stream.  If the stream
        has an 'encoding' attribute, it is used to determine how to do the
        output to the stream.
        """
        try:

            msg = self.format(record)
            self.send_message(msg)

        except Exception:
            self.handleError(record)
        pass

    def send_message(self, message):

        self.sentry_sdk.capture_message(message)
