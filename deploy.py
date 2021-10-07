# Code was forgotten in the course video : https://github.com/smartcontractkit/full-blockchain-solidity-course-py/blob/main/chronological-issues-from-video.md#lesson-4
from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# 1 - Reading our solidity file
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()


# 2-a - Compile Our Solidity contract
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        }
    },
    solc_version="0.6.0",
)
# 2-b - Dump the compiled data from variable to the file
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# 3 - Get bytecode and abi from compile data
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# 4 - Connection to the Ganache local blockchain
w3 = Web3(Web3.HTTPProvider(os.getenv("HTTPPROVIDER")))
chain_id = int(os.getenv("CHAIN_ID"))
my_address = os.getenv("PUBLIC_KEY")
private_key = os.getenv("PRIVATE_KEY")

# 5 - Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# 6 - Deploy the contract
# 6-a Get the latest transaction
nonce = w3.eth.getTransactionCount(my_address)

# 6-b Build a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId":chain_id, "from":my_address, "nonce": nonce}
)
print(transaction)
# 6-c Sign a transaction
# 6-d Send a transaction