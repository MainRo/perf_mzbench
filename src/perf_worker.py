import mzbench
import urllib2
from threading import Timer
import json

def initial_state():
    pass

def metrics():
    return [
        [
            ('load.avg1', 'gauge'),
            ('load.avg5', 'gauge'),
            ('load.avg15', 'gauge')
        ],
        [
            ('cpu.usr', 'gauge'),
            ('cpu.nice', 'gauge'),
            ('cpu.sys', 'gauge'),
            ('cpu.iowait', 'gauge'),
            ('cpu.irq', 'gauge'),
            ('cpu.soft', 'gauge'),
            ('cpu.steal', 'gauge'),
            ('cpu.guest', 'gauge'),
            ('cpu.gnice', 'gauge'),
            ('cpu.all', 'gauge')
        ],
        [
            ('mem.used', 'gauge'),
            ('mem.free', 'gauge'),
            ('mem.shared', 'gauge'),
            ('mem.buffers', 'gauge'),
            ('mem.cached', 'gauge')
        ],
        [
            ('mem.swap.used', 'gauge'),
            ('mem.swap.free', 'gauge')
        ]
    ]

def get_perf_metrics(host, port):
    url = 'http://' + host + ':' + str(port) + '/status'
    response = urllib2.urlopen(url)
    status = response.read()
    status = json.loads(status)
    mzbench.notify(('load.avg1', 'gauge'), status['load']['load1'])
    mzbench.notify(('load.avg5', 'gauge'), status['load']['load5'])
    mzbench.notify(('load.avg15', 'gauge'), status['load']['load15'])

    mzbench.notify(('cpu.usr', 'gauge'), status['cpu']['usr'])
    mzbench.notify(('cpu.nice', 'gauge'), status['cpu']['nice'])
    mzbench.notify(('cpu.sys', 'gauge'), status['cpu']['sys'])
    mzbench.notify(('cpu.iowait', 'gauge'), status['cpu']['iowait'])
    mzbench.notify(('cpu.irq', 'gauge'), status['cpu']['irq'])
    mzbench.notify(('cpu.soft', 'gauge'), status['cpu']['soft'])
    mzbench.notify(('cpu.steal', 'gauge'), status['cpu']['steal'])
    mzbench.notify(('cpu.guest', 'gauge'), status['cpu']['guest'])
    mzbench.notify(('cpu.gnice', 'gauge'), status['cpu']['gnice'])
    mzbench.notify(('cpu.all', 'gauge'), status['cpu']['all'])

    mzbench.notify(('mem.used', 'gauge'), status['mem']['used'])
    mzbench.notify(('mem.free', 'gauge'), status['mem']['free'])
    mzbench.notify(('mem.shared', 'gauge'), status['mem']['shared'])
    mzbench.notify(('mem.buffers', 'gauge'), status['mem']['buffers'])
    mzbench.notify(('mem.cached', 'gauge'), status['mem']['cached'])
    mzbench.notify(('mem.swap.used', 'gauge'), status['mem']['swap_used'])
    mzbench.notify(('mem.swap.free', 'gauge'), status['mem']['swap_free'])
