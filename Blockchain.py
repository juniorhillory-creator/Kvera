import hashlib

class Block:
    def __init__(self, index, data,prev_hash):
        self.index=index
        self.data=data
        self.hash=""
        #storing previous hash
        self.prev_hash= prev_hash
        
#calculate the hash
    def cal_hash(self):
        content=f"{self.index}|{self.data}|{self.prev_hash}"
        return hashlib.sha256(content.encode()).hexdigest()

def short(long_hash):
    return long_hash[:8]


#the genesis block(1st block)
class Blockchain:
    def __init__(self):
        genesis = Block(index=0, data="Genesis Block",prev_hash="0"*64)
        self.chain=[genesis]
        #hashing on genesis block
        genesis.hash=genesis.cal_hash()


    def add_block(self, data):
        last_block=self.get_last_block()
        block=Block(last_block.index+1, data, last_block.hash)
        #cal hash when adding a block
        block.hash=block.cal_hash()

        self.chain.append(block)

    def get_last_block(self):
        return self.chain[-1]

    def print_chain(self):
        for block in self.chain:
            print(f"#{block.index} \n data={block.data} \n prev={short(block.prev_hash)} \n hash={short(block.hash)}")

#check if its edited or not
    def is_chain_valid(self):
        for i in range(len(self.chain)):
            block= self.chain[i]
            prev_block=self.chain[i-1]

            if block.hash != block.cal_hash():
                return False
            if block.prev_hash != prev_block.hash:
                return False

        return True
    
#block adds        
Kvera=Blockchain()

Kvera.add_block("Satoshi pays Kush 10")
Kvera.add_block("Kush pays Roby 5")
Kvera.add_block("Kush pays Sathoshi 5")
Kvera.add_block("Satoshi pays kush 5")

#edit block3
block3=Kvera.chain[3]
block3.data="Satoshi pays Kush 50"
block3.hash=block3.cal_hash()

#edit block 4 with block3 prev hash
block4=Kvera.chain[4]
block4.prev_hash=block3.hash

#print blocks
Kvera.print_chain()

#validate is it true
print("is chain valid: ",Kvera.is_chain_valid())

#print edited block4
#print(short(block4.cal_hash()))

