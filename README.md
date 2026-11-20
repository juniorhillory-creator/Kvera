# Kvera Blocks

A simple blockchain implementation in Python demonstrating core blockchain concepts including block creation, cryptographic hashing, chain validation, and tamper detection.

## Project Details

This project implements a basic blockchain with the following features:

- **Block Structure**: Each block contains an index, data payload, previous block hash, and its own calculated hash
- **Genesis Block**: Automatic creation of the first block in the chain
- **Cryptographic Hashing**: SHA-256 hashing using Python's `hashlib` library
- **Chain Validation**: Verifies chain integrity by checking hashes and previous block references
- **Tamper Detection**: Demonstrates detection of modified blocks in the chain

## Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.x | Core implementation language |
| hashlib | Standard Library | SHA-256 cryptographic hashing |

## Implementation Status

| Feature | Status | Description |
|---------|--------|-------------|
| Block Class | ✅ Complete | Block structure with index, data, prev_hash, and hash |
| Hash Calculation | ✅ Complete | SHA-256 hash generation from block contents |
| Blockchain Class | ✅ Complete | Chain management with genesis block creation |
| Add Block | ✅ Complete | Append new blocks with automatic linking |
| Chain Validation | ✅ Complete | Verify integrity of entire chain |
| Tamper Detection | ✅ Complete | Detects modified blocks and broken links |
| Genesis Block | ✅ Complete | Automatic initialization with index 0 |

## Usage

```python
from Blockchain import Blockchain

# Create a new blockchain
chain = Blockchain()

# Add blocks
chain.add_block("Transaction data here")

# Print the chain
chain.print_chain()

# Validate chain integrity
print(chain.is_chain_valid())
```

## Example Output

Running `python Blockchain.py` demonstrates:
1. Creating a blockchain with genesis block
2. Adding 4 transaction blocks
3. Tampering with block 3 data
4. Chain validation detecting the tampering (returns `False`)

## Files

- `Blockchain.py` - Main blockchain implementation
- `test.py` - Simple hashlib test

## Future Improvements

- [ ] Proof-of-Work consensus mechanism
- [ ] Peer-to-peer networking
- [ ] Transaction validation and UTXO model
- [ ] Persistent storage (database/file)
- [ ] REST API interface
- [ ] Unit tests with pytest
