from algosdk.v2client import algod

algod_address = "https://testnet-api.algonode.cloud"
algod_token = ""

client = algod.AlgodClient(algod_token, algod_address)

address = "YOUR_ALGORAND_ADDRESS"

account_info = client.account_info(address)

print("Account balance:", account_info['amount'], "microAlgos")
