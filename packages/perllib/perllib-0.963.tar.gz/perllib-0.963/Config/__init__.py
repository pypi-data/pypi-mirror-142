"""Implementation of perl Config package"""

import perllib
import subprocess
import traceback
perllib.init_package('Config')

def config_sh():
    sp = subprocess.run(['perl', '-e', 'use Config qw/config_sh/; print config_sh() . "\n";'], capture_output=True,text=True,shell=False);
    return sp.stdout

Config.config_sh = config_sh

try:
    Config.Config = dict()
    lines = config_sh().splitlines()
    for line in lines:
        if '=' in line:
            (lhs, rhs) = line.split('=',1)
            rhs = rhs[1:-1] # Eat the quotes
            Config.Config[lhs] = rhs
except Exception:
    traceback.print_exc()
