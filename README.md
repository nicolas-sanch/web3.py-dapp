# Web3.py Dapp Sample Project

This codebase was obtained after following the [Full blockchain solidity course py](https://github.com/smartcontractkit/full-blockchain-solidity-course-py#lesson-4-web3py-simple-storage) lesson 4

## Getting started

Here's how to deploy this project

1. Clone the repo

```sh
git clone https://github.com/nicolas-sanch/web3.py-dapp
cd web3.py-dapp
```

2. Test if applications needed are already install in your OS
```sh
pip --version
pip show py-solc-x
node --version
yarn --version
ganache-cli --version
```

3. Start the local test node
```sh
ganache-cli
```

4. Create your .env file with your own values
```sh
cp .env.example .env
vi .env
```

5. Compile the solidity contract
```sh
python3 deploy.py
```