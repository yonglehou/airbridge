# -*- config:utf-8 -*-
"""
    Copyright 2015 Airbridge

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import sys

from api.builder import create_app as build_api
from console.builder import create_app as build_console


APPS = {
    'api',
    'console'
}

config_file = '../config.cfg'

if len(sys.argv) > 1:
    APPS = list({str(sys.argv[1])})

try:
    for item in APPS:
        app = getattr(sys.modules[__name__], "build_%s" % item)([config_file])
        item = item.upper()
        app.run(host=app.config['%s_RUN_HOST' % item],
                port=app.config['%s_RUN_PORT' % item],
                use_reloader=app.config['%s_RUN_USE_RELOADER' % item],
                debug=app.config['%s_RUN_DEBUG' % item])
except Exception:
    raise Exception('Errors found in application start.')
