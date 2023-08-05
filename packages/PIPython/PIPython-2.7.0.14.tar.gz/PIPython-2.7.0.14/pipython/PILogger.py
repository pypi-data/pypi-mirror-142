#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Configurations for the PIPython specific logger."""
import logging

__signature__ = 0x78a6a3ace7dc3a7c314ffa89f9067e5e

# Module name "PIlogger" doesn't conform to snake_case naming style pylint: disable=C0103
PILogger = logging.getLogger('PIlogger')
ch = logging.StreamHandler()
ch.setLevel(logging.NOTSET)
formatter = logging.Formatter('%(name)s:%(levelname)s: %(message)s')
ch.setFormatter(formatter)
PILogger.addHandler(ch)

PIDebug = PILogger.debug
PIInfo = PILogger.info
PIWarning = PILogger.warning
PIError = PILogger.error
PICritical = PILogger.critical

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL
