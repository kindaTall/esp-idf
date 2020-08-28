# -*- coding: utf-8 -*-
#
# English Language RTD & Sphinx config file
#
# Uses ../conf_common.py for most non-language-specific settings.

# Importing conf_common adds all the non-language-specific
# parts to this conf module
try:
    from conf_common import *  # noqa: F403,F401
except ImportError:
    import sys
    import os
    sys.path.insert(0, os.path.abspath('..'))
    from conf_common import *  # noqa: F403,F401
    from local_util import download_file_if_missing  # noqa: E402 - need to import from common folder

# General information about the project.
project = u'ESP-IDF 编程指南'
copyright = u'2016 - 2021 乐鑫信息科技（上海）股份有限公司'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'zh_CN'

# Download font file that is stored on a separate server to save on esp-idf repository size.
print("Downloading font file")
download_file_if_missing('https://dl.espressif.com/dl/esp-idf/docs/_static/NotoSansSC-Regular.otf', '../_static')

# Set up font for blockdiag, nwdiag, rackdiag and packetdiag
blockdiag_fontpath = '../_static/NotoSansSC-Regular.otf'
seqdiag_fontpath = '../_static/NotoSansSC-Regular.otf'
actdiag_fontpath = '../_static/NotoSansSC-Regular.otf'
nwdiag_fontpath = '../_static/NotoSansSC-Regular.otf'
rackdiag_fontpath = '../_static/NotoSansSC-Regular.otf'
packetdiag_fontpath = '../_static/NotoSansSC-Regular.otf'
