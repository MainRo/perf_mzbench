import mzbench
import urllib2
from threading import Timer
import json

def initial_state():
    pass

def metrics():
    return [
        [
            ('avg1', 'gauge'),
            ('avg5', 'gauge'),
            ('avg11', 'gauge')
        ]
    ]

def get_perf_metrics(host, port):
    url = 'http://' + host + ':' + str(port) + '/status'
    response = urllib2.urlopen(url)
    status = response.read()
    status = json.loads(status)
    mzbench.notify(('avg1', 'gauge'), status['load']['load1'])
    mzbench.notify(('avg5', 'gauge'), status['load']['load5'])
    mzbench.notify(('avg15', 'gauge'), status['load']['load15'])
