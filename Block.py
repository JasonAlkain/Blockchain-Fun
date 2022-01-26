from hashlib import *
import json

class Block:
    #============================================================
    # Initialize the Block with: 
    #   index
    #   timestamp
    #   data
    #   preceding hash
    #============================================================
    def __init__(self, index, timeStamp, data, precedingHash = ' '):
        self.nonce = 0
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.precedingHash = precedingHash
        self.hash = self.ComputeHash()

    
    #============================================================
    # Compute a new hash for the block
    #============================================================
    def ComputeHash(self):
        str_A = ''
        str_A += str(self.index)
        str_A += str(self.precedingHash)
        str_A += str(self.timeStamp)
        str_A += str(self.nonce)
        str_A += json.dumps(self.data)
        return sha512(bytes(str_A, 'utf-8')).hexdigest()


    #============================================================
    # Use the Proof Of Work system to create a new block
    #============================================================
    def ProofOfWork(self, difficulcty):
        prefixStr = '0'*difficulcty
        while self.hash.startswith(prefixStr) != True:
            self.nonce += 1
            self.hash = self.ComputeHash()
        pass