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
            ('avg15', 'gauge')
        ],
        [
            ('usr', 'gauge'),
            ('nice', 'gauge'),
            ('sys', 'gauge'),
            ('iowait', 'gauge'),
            ('irq', 'gauge'),
            ('soft', 'gauge'),
            ('steal', 'gauge'),
            ('guest', 'gauge'),
            ('gnice', 'gauge'),
            ('all', 'gauge')
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

    mzbench.notify(('usr', 'gauge'), status['cpu']['usr'])
    mzbench.notify(('nice', 'gauge'), status['cpu']['nice'])
    mzbench.notify(('sys', 'gauge'), status['cpu']['sys'])
    mzbench.notify(('iowait', 'gauge'), status['cpu']['iowait'])
    mzbench.notify(('irq', 'gauge'), status['cpu']['irq'])
    mzbench.notify(('soft', 'gauge'), status['cpu']['soft'])
    mzbench.notify(('steal', 'gauge'), status['cpu']['steal'])
    mzbench.notify(('guest', 'gauge'), status['cpu']['guest'])
    mzbench.notify(('gnice', 'gauge'), status['cpu']['gnice'])
    mzbench.notify(('all', 'gauge'), status['cpu']['all'])
