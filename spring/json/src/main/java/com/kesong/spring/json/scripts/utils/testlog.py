# -*- coding: utf-8 -*-
"""
Created on 2017/12/7.

@author: kesong
"""
import logging
import logging.config

logging.config.fileConfig("win_logger.conf")
log1 = logging.getLogger("count")
log2 = logging.getLogger("errorcount")
log1.info("success")
log2.error("error")