#!/usr/bin/env python
# -*- coding: utf8 -*-

import subprocess
import concurrent.futures


def get_outout(cmd):
    cmd = cmd.split() if isinstance(cmd, str) else cmd
    stdout = subprocess.check_output(cmd)
    print(stdout.decode('utf-8'), end='\n'*3)
    stdout = stdout.decode('utf-8')
    return stdout


if __name__ == '__main__':
    cmd_list = ['brew cask info adafruit-arduino', 'brew cask info galileo-arduino', 'brew cask info arduino']
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        out_res = {executor.submit(get_outout, cmd): cmd for cmd in cmd_list}
        for out in concurrent.futures.as_completed(out_res):
            data = out.result()
            print('≈'*79 + '\n\n' + data)
