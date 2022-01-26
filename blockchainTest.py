from hashlib import *
from datetime import datetime
from Block import Block
from numpy import block
import time as Time


class BlockchainTest:
    def __init__(self):
        self.blockchain = [self.StartGenesisBlock()]
        self.difficulcty = 4
    
    #
    # Starts the blockchain with a genesis block
    #
    def StartGenesisBlock(self):
        return Block(0, datetime.fromtimestamp(Time.time()), 'Genesis Block', '0')

    #
    # Gets the latest block from the blockchain
    #
    def ObtainLatestBlock(self):
        return self.blockchain[len(self.blockchain)-1]
    
    #
    # Adds new Bolck to the Blockchain
    #
    def AddNewBlock(self, newBlock: Block):
        newBlock.precedingHash = self.ObtainLatestBlock().hash
        newBlock.ProofOfWork(self.difficulcty)
        self.blockchain.append(newBlock)
    
    #
    # Check the validity of the blockchain
    #
    def CheckChainValidity(self):
        for n in range(len(self.blockchain)-1):
            currentBlock = self.blockchain[n]
            precedingBlock = self.blockchain[n-1]
            
            if currentBlock!= currentBlock.ComputeHash():
                return False
            if currentBlock.precedingHash != precedingBlock.hash:
                return False

            return True