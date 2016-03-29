#!/usr/bin/env python
# -*- coding: utf8 -*-

import subprocess
from multiprocessing.dummy import Pool

def get_outout(cmd):
    cmd = cmd.split() if isinstance(cmd, str) else cmd
    stdout = subprocess.check_output(cmd)
    stdout = stdout.decode('utf-8')
    return stdout


if __name__ == '__main__':
    cmd_list = ['brew cask info adafruit-arduino', 'brew cask info galileo-arduino', 'brew cask info arduino']
    p = Pool(processes=4)
    out = p.map_async(get_outout, cmd_list)
    out.wait()
    if out.successful():
        for el in out.get():
            print('≈'*79 + '\n\n' + el)
