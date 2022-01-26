#============================================================
# Import Modules
#============================================================
from datetime import datetime, date, time
import time as Time
import json
from blockchainTest import BlockchainTest
from Block import Block
from random import randint
from timeit import default_timer as timer

#============================================================
# Create BlockchainTest objcet
#============================================================
bct = BlockchainTest()

#============================================================
# Start index at 0
#============================================================
index = 0

# Simple block creater function
def CreateNewBlock(Name):
    # Create simple data
    data = {'Name':f'{Name}', 'funds':randint(1,10)}
    # increment index
    index = len(bct.blockchain)
    # Create the block with the data
    block = Block(index, datetime.fromtimestamp(Time.time()), data)
    return block

#============================================================
# Alpha block
#============================================================
print('<==============================>')
print('Start Block Creation...')
start = timer()
bct.AddNewBlock(CreateNewBlock('Alpha'))
end = timer()
print('Found Block!!')
print(f'Time elapsed: ~{round((end - start), 4)}sec')
print('<==============================>')
Time.sleep(1)

#============================================================
# Beta block
#============================================================
print('<==============================>')
print('Start Block Creation...')
start = timer()
bct.AddNewBlock(CreateNewBlock('Beta'))
end = timer()
print('Found Block!!')
print(f'Time elapsed: ~{round((end - start), 4)}sec')
print('<==============================>')
Time.sleep(1)

#============================================================
# Gama block
#============================================================
print('<==============================>')
print('Start Block Creation...')
start = timer()
bct.AddNewBlock(CreateNewBlock('Gama'))
end = timer()
print('Found Block!!')
print(f'Time elapsed: ~{round((end - start), 4)}sec')
print('<==============================>')
Time.sleep(1)
print('\n')
#============================================================
# Print each block in the chain
#============================================================
for i in range(len(bct.blockchain)):
    print('<==============================>')
    print(f'Index: {bct.blockchain[i].index}')
    print(f'Time Stamp: {bct.blockchain[i].timeStamp}')
    print(f'Data: {bct.blockchain[i].data}')
    print(f'Hash [4:12]: {bct.blockchain[i].hash[4:12]}')
    print(f'Preceding Hash [4:12]: {bct.blockchain[i].precedingHash[4:12]}')
    print(f'Nonce: {bct.blockchain[i].nonce}')
    print('<==============================>')



