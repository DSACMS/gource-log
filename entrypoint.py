#!/usr/bin/env -S python3 -B

import os
from subprocess import check_output


if __name__ == "__main__":
    print("Hello world!")
    print(os.getcwd())
    print(check_output(['git','config','--global','--add','safe.directory','/github/workspace']))
    print(check_output(['gource','--output-custom-log','gource-log.log']))
    print(check_output(['gource','--help']))

    with open('gource-log.log','r') as f:
        print(f.read())
