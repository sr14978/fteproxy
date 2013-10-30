#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of FTE.
#
# FTE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FTE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FTE.  If not, see <http://www.gnu.org/licenses/>.

import os
import tempfile


def getValue(key):
    return conf[key]


def setValue(key, value):
    conf[key] = value


def module_path():
    return os.path.dirname(__file__)


conf = {}


"""The base path for the location of the fte.* modules."""
conf['general.base_dir'] = os.path.abspath(os.path.join(module_path()))


"""The location that we store *.pid files, such that we can kill FTE from the command line."""
conf['general.pid_dir'] = tempfile.gettempdir()


"""Our runtime mode: client|server|test"""
conf['runtime.mode'] = None


"""The maximum number of queued connections for sockets"""
conf['runtime.fte.relay.backlog'] = 5


"""Our client-side ip:port to listen for incoming connections"""
conf['runtime.client.ip'] = '127.0.0.1'
conf['runtime.client.port'] = 8079


"""Our server-side ip:port to listen for connections from FTE clients"""
conf['runtime.server.ip'] = '127.0.0.1'
conf['runtime.server.port'] = 8080


"""Our proxy server, where the FTE server forwards outgoing connections."""
conf['runtime.proxy.ip'] = '127.0.0.1'
conf['runtime.proxy.port'] = 8081


"""The default socket timeout."""
conf['runtime.fte.relay.socket_timeout'] = 0.001


"""The maxium number of bytes to sgement for an outgoing message."""
conf['runtime.fte.record_layer.max_cell_size'] = 2 ** 16


"""The default client-to-server language."""
conf['runtime.state.upstream_language'] = 'manual-http-request'


"""The default server-to-client language."""
conf['runtime.state.downstream_language'] = 'manual-http-response'


"""The default AE scheme key."""
conf['runtime.fte.encrypter.key'] = 'FF' * 16 + '00' * 16


"""The default max_len parameter to use for buildTable."""
conf['fte.default_max_len'] = 512


"""The default definitions file to use."""
conf['fte.defs.release'] = '20131023'
