import os
import time

LOGDIR = './logs'


class Clog(object):
    def __init__(self, write_file=False):
        self.fp = None
        self.write_file = write_file
        self.filename = None
        self.remove_file = False

    def open(self, prefix, remove_file=False):
        self.remove_file = remove_file
        if self.write_file:
            if not os.path.exists(LOGDIR):
                os.mkdir(LOGDIR)
            self.filename = '%s/%s_%s' % (LOGDIR, prefix, time.strftime('%Y%m%d_%H%M%S'))
            self.fp = open(self.filename, 'w')

    def close(self):
        if self.fp:
            self.fp.close()
            self.fp = None
        if self.remove_file is True and self.filename:
            os.remove(self.filename)

    def _clog(self, level, string):
        _str = '%s: %s' % (level, string)
        print (_str)
        if self.write_file:
            if type(_str).__name__ == 'str':
                self.fp.write('%s\n' % _str)
            else:
                self.fp.write('%s\n' % _str.encode('utf-8'))

    def debug(self, str):
        self._clog('DEBUG', str)

    def info(self, str):
        self._clog('INFO', str)

    def warn(self, str):
        self._clog('WARN', str)

    def error(self, str):
        self._clog('ERROR', str)



