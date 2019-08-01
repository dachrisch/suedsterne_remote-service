# coding=utf-8
import os

import jsonpickle
from flask import Flask


class RemoteMethod(object):
    def __init__(self, name, remote, login=None):
        self.name = name
        self.remote = remote
        self.login = login


remote_app = Flask(__name__)


@remote_app.route('/remotes/api/v1.0/methods', methods=['GET'])
def get_methods():
    methods = (RemoteMethod('Google', 'https://meet.google.com/upv-baht-nyt'),
               RemoteMethod('Zoom', 'https://zoom.us/j/6787719716', CONTAINER + '4p46nyct6zemrkl7zcyamec7ym'),
               RemoteMethod('Talkyoo', '+494095063183', CONTAINER + 'qibsxmw3arg6do637ygaaulihq'),
               RemoteMethod('Satellite', '+4915678599302', CONTAINER + 'rxzgnk3nmhbalnq57aikrdt3eu'))
    return jsonpickle.encode(methods, unpicklable=False)


CONTAINER = 'https://it-agile.1password.eu/vaults/v2edm55d3ohyurvf5psbe6i7de/allitems/'

if __name__ == '__main__':
    remote_app.run(host=os.getenv('REMOTE_SERVICE_HOST', '0.0.0.0'),
                   port=os.getenv('REMOTE_SERVICE_PORT', 5000))
