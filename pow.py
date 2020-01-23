import sys
import utils  
import hashlib

max_nonce = sys.maxsize

class Pow():

    def __init__(self, block):
        self.block = block
        self.target = 1 << (256 - block.bits)  # 2^(256-16)

    def prepare_data(self, nonce):
        data_list = [self.block.prev_block_hash, # str
                     self.block.data,
                     self.block.time,            # str
                     str(self.block.bits),       # int -> str
                     str(nonce)]                 # int -> str
        # return utils.encode(''.join(data_list))
        return ''.join(data_list)

    def run(self):
        nonce = 0
        while self.block.nonce < max_nonce:
            data = self.prepare_data(nonce)
            # _hash = utils.sha256(data.encode())
            _hash = utils.create_hash(data)
            print(_hash, end='\r', flush=True)
            if int(_hash, 16) < self.target: # convert hex to dec  
                break
            else:
                nonce += 1
        
        return nonce, _hash
