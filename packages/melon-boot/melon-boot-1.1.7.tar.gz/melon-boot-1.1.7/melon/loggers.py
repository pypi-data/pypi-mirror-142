# -*- encoding: utf-8 -*-
"""
@Author  : zh_o
"""
import sys
from loguru import logger
from melon.settings import get_config


logger.remove()
default_format = '<cyan>{time:YYYY:MM:DD HH:mm:ss.SSS}</cyan> ' \
         '<black>[</black><magenta>TID:{thread.id}</magenta><black>]</black> ' \
         '<black>[</black><blue>{level}</blue><black>]</black> ' \
         '<black>{file}</black>' \
         '<black>[</black><blue>{line}</blue><black>]</black>' \
         '<black>:</black> ' \
         '{message}'
_format = get_config('melon.logging.format', default_format)

logger.add(
    sink=sys.stdout,
    format=_format
)
