# Infura Web3 Py

## Objective

A Python CLI that uses the web3.py module to find the hashes of the block and transaction from which a contract address was deployed.

## Installation

* Note: This program has been tested on Python 3.7.0. Hence installation guide is as per the same.

1. Cloning the repository

```
git clone https://github.com/bhaveshAn/infura-web3-py.git
cd infura-web3-py
```

2. Creating & activating Virtual Environment (Python 3.7.0)

```
virtualenv venv

source venv/bin/activate
```

3. Installing the dependencies

```
pip install -r requirements.txt
```

## Usage

For your web3 host, please sign up for https://infura.io/ to get an API key.

Run the following command in terminal

```
python main.py 0xcontract_address_here --host https://mainnet.infura.io/<API_SECRET>
```

You will get the output as follows:

```
Block: 0xblock_from_which_contract_was_deployed`
Transaction: 0xtransaction_with_which_contract_was deployed
```

**Example**

Using `0xf20e482322f2ead3decdbec89ad6dadf715f5811` as argument `0xcontract_address_here` you will receive the following:

```
Block: 0x4ff9e5bf03e73305d3f78bbaedd979bce0cfb42cdc89dd8f5d5187b6bf2aaa24
Transaction: 0x93fd955fff68f9d763bafb133a852e5c3ef88f481b2dad75c92bf2714728c096
```

## Reason to search Block from the End

The last blocks will contain more transactions than the very first ones and this increases the possibility to find the block about which one wants the hashes.

## Author

[Bhavesh Anand](https://bhaveshan.github.io)
