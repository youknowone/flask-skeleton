#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from template import app

import sys
print 'python:', sys.version
import jinja2
print 'jinja2:', jinja2.__version__
import werkzeug
print 'werkzeug:', werkzeug.__version__

from werkzeug.contrib.profiler import ProfilerMiddleware
#app.wsgi_app = ProfilerMiddleware(app.wsgi_app, sort_by=('cumulative', 'calls'))
#app.wsgi_app = ProfilerMiddleware(app.wsgi_app)

app.run(host='0.0.0.0', port=3733, debug=True)
