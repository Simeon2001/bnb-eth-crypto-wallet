from web3 import Web3
import config
bsc = "https://speedy-nodes-nyc.moralis.io/4aec99bbde5dac3464032ea3/bsc/testnet"
w3 = Web3(Web3.HTTPProvider(bsc))
print(w3.isConnected())

account_1 = "0x7D00bdDd38783e8a46C60baa9A7CD48443598406"
account_2 = "0xa0E4e2778d756DD42A8ad9B4a0611464704Be21F"

balance = w3.eth.get_balance(account_2)
readable = w3.fromWei(balance,'ether')
print(readable)

nonce = w3.eth.getTransactionCount(account_1)
tx = {
    'chainId':97,
    'nonce':nonce,
    'to':account_2,
    'value':w3.toWei(0.2,'ether'),
    'gas':21000,
    'gasPrice':w3.toWei('50','gwei')
}

signed_tx = w3.eth.account.signTransaction(tx,config.privates)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(w3.toHex(tx_hash))