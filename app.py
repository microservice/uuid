# -*- coding: utf-8 -*-
from uuid import uuid4

from flask import Flask, make_response


class Handler:
    app = Flask(__name__)

    def generate(self):
        resp = make_response(f'{uuid4()}')
        resp.headers['Content-Type'] = 'text/plain; charset=utf-8'
        return resp


if __name__ == '__main__':
    handler = Handler()
    handler.app.add_url_rule('/generate', 'generate', handler.generate,
                             methods=['get'])
    handler.app.run(host='0.0.0.0', port=8000)
