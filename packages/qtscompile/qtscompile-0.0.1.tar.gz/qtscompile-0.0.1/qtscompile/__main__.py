import argparse
from __init__ import *
parser = argparse.ArgumentParser(prog='qtsCompile')
parser.add_argument('-v', "--version", action="store_true",
                    help="echo the this version")
parser.add_argument('-p', "--path",
                    help="path")
parser.add_argument('option', help='option', choices=[
                    'python2qts', 'analysis'])
args = parser.parse_args()


if args.version:
    print('version:', __version__)

if args.path:
    p = Path(args.path)
    option = 'p.'+args.option+'()'
    eval(option)
else:
    printf('error: The path option must be filled in')
