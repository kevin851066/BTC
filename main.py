import argparse
from blockchain import Blockchain
from utils import Database

parser = argparse.ArgumentParser(description='Welcome to world of blockchain!!!')
subparser = parser.add_subparsers(dest='command', help='subcommands')

subparser_addblock = subparser.add_parser('addblock')
subparser_addblock.add_argument('-transaction', dest='transactions')

subparser_printchain = subparser.add_parser('printchain')

subparser_printblock = subparser.add_parser('printblock')
subparser_printblock.add_argument('-height', dest='height', type=int)

subparser_resetdb = subparser.add_parser('resetdb')
args = parser.parse_args()

bc = Blockchain()

if args.command == 'addblock' and args.transactions:
    bc.add_block(args.transactions)
elif args.command == 'printchain':
    bc.print_chain()
elif args.command == 'printblock' and args.height:
    bc.print_block(args.height)
elif (args.command == 'resetdb'):
    Database().reset()
else:
    parser.print_help()
