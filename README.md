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

Using `0x045690a5a6ff78ea388bd3df76ce46fd07b7d332` as argument `0xcontract_address_here` you will receive the following:

```
Block: 0xa0ba75ca9aa1ff697e3ffbe05f2290379cea4d233a663b7bcccffe68583a1cd0
Transaction: 0x80a560ed8343ea614d10a7478f0ecc3d8330354028e43efad00a12e81e137344
```

## Reason to search Block from the End

The last blocks will contain more transactions than the very first ones and this increases the possibility to find the block about which one wants the hashes.

## Author

[Bhavesh Anand](https://bhaveshan.github.io)
