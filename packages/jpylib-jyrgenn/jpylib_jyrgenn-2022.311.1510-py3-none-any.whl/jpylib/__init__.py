#!/usr/bin/env python3
# Have all support function modules here at hand.

import os
import pwd
import sys

from .pgetopt import parse as pgetopts
from .alerts import L_ERROR, L_NOTICE, L_INFO, L_DEBUG, L_TRACE, \
    alert_config, alert_level, alert_level_name, \
    alert_level_up, alert_level_zero, is_notice, is_info, is_debug, is_trace, \
    debug_vars, fatal, err, notice, info, debug, trace, \
    tracef, debugf, infof, noticef, errorf, fatalf, temporary_alert_level
from .fntrace import tracefn
from .stringreader import StringReader
from .kvs import parse_kvs
from .namespace import Namespace
from .config import Config
from .secrets import putsecret, getsecret, getsecret_main, putsecret_main, \
     FileModeError
from .sighandler import sanesighandler
from .terminal import ttyi, ttyo, ptty
from .capture import outputCaptured, outputAndExitCaptured, inputFrom
from .process import backquote
from .assorted import boolish, flatten, is_sequence
from .numeric import maybe_int, is_int, maybe_num, is_num, \
     avg_midrange, remove_outliers
from .iohelper import all_input_lines
from .time import isotime, isotime_ms, iso_time, iso_time_ms, iso_time_us
from .table import format_table
from .singleton import Singleton
from .multiset import Multiset

version = "2022.311.1510"
program = os.path.basename(sys.argv[0])
real_home = pwd.getpwuid(os.getuid()).pw_dir
home = os.environ.get("HOME") or real_home
verbosity_option = ("verbose", alert_level_up, alert_level(L_NOTICE),
                    "increase verbosity")
