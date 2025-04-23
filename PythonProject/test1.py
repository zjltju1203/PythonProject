import argparse
import torch
parser = argparse.ArgumentParser(description="desc")
parser.add_argument('-gf', '--girlfriend', choices=['jingjing', 'lihuan'])
parser.add_argument('--no-debug', action='store_false', dest='debug', default=True, help='Disable debug mode')
parser.add_argument('--no_dd', action='store_true', help='Disable debug mode')
args = parser.parse_args()

if args.debug:
    print('Debug mode is enabled.')
else:
    print('Debug mode is disabled.')

print('girlfriend:', args.girlfriend)
print('no-dd', args.no_dd)




