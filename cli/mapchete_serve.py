#!/usr/bin/env python

import os
import sys
import argparse
from flask import Flask, send_file

from mapchete import *
from tilematrix import TilePyramid, MetaTilePyramid

import pkgutil

process_host = None

def main(args):

    parser = argparse.ArgumentParser()
    parser.add_argument("mapchete_file", type=str)
    parser.add_argument("--zoom", "-z", type=int, nargs='*', )
    parser.add_argument("--bounds", "-b", type=float, nargs='*')
    parser.add_argument("--log", action="store_true")
    parsed = parser.parse_args(args)

    try:
        print "preparing process ..."
        process_host = MapcheteHost(
            parsed.mapchete_file,
            zoom=parsed.zoom,
            bounds=parsed.bounds
            )
    except Exception as e:
        raise

    app = Flask(__name__)


    @app.route('/', methods=['GET'])
    def get_tasks():
        index_html = pkgutil.get_data('static', 'index.html')
        return index_html

    @app.route('/wmts_simple', methods=['GET'])
    def get_getcapabilities():
        return "getcapabilities"

    @app.route('/wmts_simple/<string:process_id>', methods=['GET'])
    def get_processname(process_id):
        return process_id

    @app.route('/wmts_simple/1.0.0/mapchete/default/WGS84/<int:zoom>/<int:row>/<int:col>.png', methods=['GET'])
    def get_tile(zoom, row, col):
        # return str(zoom), str(row), str(col)
        tileindex = str(zoom), str(row), str(col)
        tile = (zoom, row, col)
        try:
            image = process_host.get_tile(tile)
            return image
        except Exception as e:
            return Exception
        # return str(tileindex)

    app.run(debug=True)

if __name__ == '__main__':
    main(sys.argv[1:])