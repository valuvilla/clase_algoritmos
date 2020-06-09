from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair, CryptoKeypair


bdb = BigchainDB('https://test.ipdb.io')


tito = CryptoKeypair(private_key='7wT5KbrSxRZo9joTfMGsHfVTcJ2PFEZGxiFtD6wezvV', public_key='C388M3715unBfJmCjPkeKuccb615g9jMrDDk6SKALXda')
walter = CryptoKeypair(private_key='G5jFRrHAuCgtpYuhn2hQ3fbTVDFHjtgTsNaJ2gT1c9cM', public_key='G1fLqFLUMvrekdGizSy9RyVLFbsf9dacPbPBV3wxeqw3')


activo = {
    'data' : {'galactic coin' : {
        'valor' : 50
    }}
}

prepared_creation_tx = bdb.transactions.prepare(
   operation='CREATE',
   signers=walter.public_key,
   #recipients=[([tito.public_key], 5)],
   asset=activo
   )



fulfilled_creation_tx = bdb.transactions.fulfill(
   prepared_creation_tx, private_keys=walter.private_key)

#sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)

#print(fulfilled_creation_tx)
txid = 'b4b7b2ce1728f75a2e8a00231d162fd65ca950548dc0b1641ccb9d7324878e3a'
#print(fulfilled_creation_tx)

# block_height = bdb.blocks.get(txid='b4b7b2ce1728f75a2e8a00231d162fd65ca950548dc0b1641ccb9d7324878e3a')
# print(block_height)
# block = bdb.blocks.retrieve(str(block_height))
# print(block)

creation_tx = bdb.transactions.retrieve(txid)
transfer_asset = {
   'id': txid
   }

output_index = 0

output = creation_tx['outputs'][output_index]

transfer_input = {
   'fulfillment': output['condition']['details'],
   'fulfills': {
        'output_index': output_index,
        'transaction_id': creation_tx['id'],
        },
    'owners_before': output['public_keys'],
   }

prepared_transfer_tx = bdb.transactions.prepare(
    operation='TRANSFER',
    asset=transfer_asset,
    inputs=transfer_input,
    recipients=tito.public_key,
)

fulfilled_transfer_tx = bdb.transactions.fulfill(
   prepared_transfer_tx,
   private_keys=walter.private_key,
   )


#sent_transfer_tx = bdb.transactions.send_commit(fulfilled_transfer_tx)

#print(bdb.transactions.get(asset_id='b4b7b2ce1728f75a2e8a00231d162fd65ca950548dc0b1641ccb9d7324878e3a'))


#print(fulfilled_transfer_tx['outputs'][0]['public_keys'][0] == tito.public_key)
#print(fulfilled_transfer_tx['outputs'][0]['public_keys'][0] == walter.public_key)


assets = bdb.assets.get(search='b1dd2ece259b0e0265665203c34b0f8fdc7c74044e0f34226030c5c5e159c0eb')
print(assets)