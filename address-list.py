from web3 import Web3
w3 = Web3()

# test mnemonic from ganache (don't use it!)
mnemonic = "seed phrase here"

w3.eth.account.enable_unaudited_hdwallet_features()
for i in range(100):
    acc = w3.eth.account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/{i}")
    print(f"{acc.address},{str(acc.key.hex()[2::])}")
