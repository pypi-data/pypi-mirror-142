# -*- coding: utf-8 -*-

import os
import json
import logging.config
import inspect


__all__ = [
    "fileConfig",
    "config"
]


# 保留原生
FILTER_OPTIONS = ['format', 'datefmt', 'style']


def _diff_all_options(c, cp, sectname):

    args = inspect.getargspec(c).args

    opts = cp.options(sectname)
    opt_diff = set(opts) - set(FILTER_OPTIONS)

    kwargs = dict()
    for opt in opt_diff:
        if opt not in args:
            continue

        value = cp.get(sectname, opt, raw=True, fallback=None)
        try:
            kwargs[opt] = json.loads(value)
        except Exception:
            kwargs[opt] = value

    return kwargs


def _filter_formats(cp, sectname):

    opts = []
    for op in FILTER_OPTIONS:
        if op != "style":
            opt = cp.get(sectname, op, raw=True, fallback=None)
        else:
            opt = cp.get(sectname, op, raw=True, fallback='%')
        opts.append(opt)

    return opts


def _create_formatters(cp):
    """Create and return formatters"""
    flist = cp["formatters"]["keys"]

    if not len(flist):
        return {}
    flist = flist.split(",")
    flist = logging.config._strip_spaces(flist)

    formatters = {}
    for form in flist:
        sectname = "formatter_%s" % form

        # 保留原生
        fs, dfs, stl = _filter_formats(cp, sectname)
        class_name = cp[sectname].get("class")

        if class_name:
            c = logging.config._resolve(class_name)
        else:
            c = logging.Formatter

        # 添加新增
        kwargs = _diff_all_options(c, cp, sectname)

        f = c(fs, dfs, stl, **kwargs)
        formatters[form] = f

    return formatters


def fileConfig(fname, defaults=None, disable_existing_loggers=True):
    """
    Read the logging configuration from a ConfigParser-format file.

    This can be called several times from an application, allowing an end user
    the ability to select from various pre-canned configurations (if the
    developer provides a mechanism to present the choices and load the chosen
    configuration).
    """

    import configparser

    if isinstance(fname, configparser.RawConfigParser):
        cp = fname
    else:
        cp = configparser.ConfigParser(defaults)
        if hasattr(fname, 'readline'):
            cp.read_file(fname)
        else:
            cp.read(fname)

    formatters = _create_formatters(cp)

    # critical section
    logging._acquireLock()
    try:
        _clearExistingHandlers()
        # Handlers add themselves to logging._handlers

        handlers = _install_handlers(cp, formatters)
        _install_loggers(cp, handlers, disable_existing_loggers)
    finally:
        logging._releaseLock()


config = logging.config
config.fileConfig = fileConfig

_clearExistingHandlers = logging.config._clearExistingHandlers
_install_handlers = logging.config._install_handlers
_install_loggers = logging.config._install_loggers


if __name__ == '__main__':

    logger_config = os.path.dirname(__file__)
    logger_file = os.path.join(logger_config, 'logging.conf')

    fileConfig(logger_file)
