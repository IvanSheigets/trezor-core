
from micropython import const

NEM_NETWORK_MAINNET = const(0x68)
NEM_NETWORK_TESTNET = const(0x98)
NEM_NETWORK_MIJIN = const(0x60)
NEM_CURVE = 'ed25519-keccak'

NEM_TRANSACTION_TYPE_TRANSFER = const(0x0101)
NEM_TRANSACTION_TYPE_IMPORTANCE_TRANSFER = const(0x0801)
NEM_TRANSACTION_TYPE_AGGREGATE_MODIFICATION = const(0x1001)
NEM_TRANSACTION_TYPE_MULTISIG_SIGNATURE = const(0x1002)
NEM_TRANSACTION_TYPE_MULTISIG = const(0x1004)
NEM_TRANSACTION_TYPE_PROVISION_NAMESPACE = const(0x2001)
NEM_TRANSACTION_TYPE_MOSAIC_CREATION = const(0x4001)
NEM_TRANSACTION_TYPE_MOSAIC_SUPPLY_CHANGE = const(0x4002)

NEM_MAX_DIVISIBILITY = const(6)
NEM_MAX_SUPPLY = const(9000000000)

NEM_SALT_SIZE = const(32)
AES_BLOCK_SIZE = const(16)
NEM_HASH_ALG = 'keccak'
NEM_PUBLIC_KEY_SIZE = const(32)  # ed25519 public key
