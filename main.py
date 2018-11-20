import argparse
import sys
from helpers import get_block_and_transaction_hash

parser = argparse.ArgumentParser(
    description='A Python CLI that uses the web3.py module to find the ' +
    'hashes of the block and transaction from which a ' +
    'contract address was deployed'
)
named_args = parser.add_argument_group('Named arguments')
named_args.add_argument(
    'address', metavar='address',
    type=str, help='Provide the contract address'
)
named_args.add_argument(
    '-p', '--host',
    help='Web3 Host Domain like: https://mainnet.infura.io/<API_SECRET>',
    required=True
)
args = parser.parse_args()
try:
    block_hash, transaction_hash = get_block_and_transaction_hash(
        args.host, args.address)
    sys.stdout.write('Block: {}\n'.format(block_hash))
    sys.stdout.write('Transaction: {}\n'.format(transaction_hash))
except TypeError:
    raise Exception('{} address not found'.format(args.address))
