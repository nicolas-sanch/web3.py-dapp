# Code was forgotten in the course video : https://github.com/smartcontractkit/full-blockchain-solidity-course-py/blob/main/chronological-issues-from-video.md#lesson-4
from solcx import compile_standard, install_solc

# 1 - Reading our solidity file
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()


# Compile Our Solidity
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
print(compiled_sol)