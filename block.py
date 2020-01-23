import datetime
from pow import Pow

class Block():
    def __init__(self, height, data, prev_block_hash):
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4] # str
        self.height = height
        self.data = data
        self.bits = 16  # difficulty
        self.prev_block_hash = prev_block_hash
        self.nonce = 0
        self.hash = None

    def pow_of_block(self):
        pow_worker = Pow(self)
        self.nonce, self.hash = pow_worker.run()
        return self
