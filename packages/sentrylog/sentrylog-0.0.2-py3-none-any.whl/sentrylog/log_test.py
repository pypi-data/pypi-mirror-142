# -*- coding: utf-8 -*-

# pip install --upgrade sentry-sdk
import unittest
import sys
import os
import logging

path = os.path.dirname(__file__)
sys.path.append(path)
from logger import *


logger = logging.getLogger('rootHandler')


class TestLog(unittest.TestCase):

    # @unittest.skip
    def test_init(self):

        # 指定sentry 和原生的两种打印方式，会执行打印，打印的顺序先进先出
        token, host, port, project = '','','',''

        # 'application' code
        ch = SentryStreamHandler(token, host, port, project)
        ch1 = logging.StreamHandler()
        logger.addHandler(ch)
        logger.addHandler(ch1)
        logger.setLevel("DEBUG")

        # 支持conf配置
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        ch1.setFormatter(formatter)
        logger.debug('debug testestestestestestestestes')
        # logger.info('info message')
        # logger.warning('warn message')
        # logger.error('error testestestestestestestestes')
        # logger.critical('critical message')
        
      


if __name__ == '__main__':
    # unittest.main()
    t = TestLog()
    t.test_init()
