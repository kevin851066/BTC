from block import Block
from utils import Database
import pickle

class Blockchain():
    def __init__(self):
        self.db = Database()
        if self.db.get('latest'):
            self.height = int(self.db.get('latest'))
            self.prev_block = pickle.loads(self.db.get(int(self.height))) # gonna creat a new block
        else:
            genesis_block = Block(0, 'This is the Genesis block baeeeee', '')
            genesis_block.time = '0'
            self.prev_block = genesis_block.pow_of_block()
            self.db.put(0, pickle.dumps(self.prev_block))
            self.db.put('latest', 0)
            self.height = 0

    def add_block(self, data):
        new_block = Block(self.height + 1, data, self.prev_block.hash).pow_of_block()
        self.prev_block = new_block 
        self.height = new_block.height
        self.db.put(self.prev_block.height, pickle.dumps(self.prev_block)) #
        self.db.put('latest', self.prev_block.height) #

    def print_chain(self):
        for num_of_block in range(self.height + 1):
            self.print_block(num_of_block)

    def print_block(self, num_of_block):
        if num_of_block <= self.height:
            block = pickle.loads(self.db.get(num_of_block))
            print('#{}'.format(block.height))
            print('Establish time: {}'.format(block.time))
            print('Previous hash: {}'.format(block.prev_block_hash))
            print('Data: {}'.format(block.data))
            print('Hash: {}'.format(block.hash))
        else:
            print('Error: the block {} does not EXIST!!!'.format(num_of_block))
