import mzbench
import urllib2
from threading import Timer
import json

host = 'localhost'
port = '4242'
status_url = None
timer = None

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

def set_host(target_host, target_port):
    host = target_host
    port = target_port
    status_url = 'http://' + host + ':' + str(port) + '/status'

def start_monitoring():
    timer = Timer(5.0, update_metrics)
    timer.start()

def stop_monitoring():
    timer.cancel()

def update_metrics():
    response = urllib2.urlopen(status_url)
    status = response.read()
    status = json.loads(status)
    mzbench.notify(('avg1', 'gauge', status['load']['avg1']))
    mzbench.notify(('avg5', 'gauge', status['load']['avg5']))
    mzbench.notify(('avg15', 'gauge', status['load']['avg15']))

    timer.start()
