import rlp
import sha3
from web3 import Web3, HTTPProvider
from web3.exceptions import InvalidAddress


def get_block_and_transaction_hash(host, address):
    web3 = Web3(HTTPProvider(host))
    if not web3.isAddress(address):
        raise InvalidAddress('{} address is invalid'.format(address))
    if not web3.isConnected():
        raise Exception('Connection Problem exists')
    address = address.lower()
    for block in range(web3.eth.blockNumber, 1, -1):
        for transaction in web3.eth.getBlock(block, full_transactions=True)['transactions']:
            if not transaction['to']:
                sender = bytes.fromhex(
                    str(transaction['from']).replace('0x', '')
                )
                contract = '0x' + str(
                        sha3.keccak_256(rlp.encode(
                            [sender, transaction['nonce']])).hexdigest()[-40:]
                )
                if contract == address:
                    block_hash = str(web3.toHex(transaction['blockHash']))
                    transaction_hash = str(web3.toHex(transaction['hash']))
                    return block_hash, transaction_hash
