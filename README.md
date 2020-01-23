# Simple blockchain python implementation

## 1.1 Prerequisites: 
### Libraries:

- python 3

- redis

- sys

- pickle
- argparse
- datetime

## 1.2 How to use my pseudo bitcoin?
### Step 1:

 Open the redis server: there is a directory called "redis-server", click it and choose the 32bit or 64bit directory which depends on TA's computer system, then click redis-server.exe to open the redis server.

### Step 2: 

Open the commander and type python3 main.py addblock -transaction {bla bla bla} 
to create a block.

### Step 3:

Type python3 main.py printchain to print the whole info of the pseudo blcokchain.
Or type python3 main.py printblock -height {x} to print the specific block with height x. 

### Step 4: 

Type python3 main.py resetdb to reset the blockchain's info.

## 1.3 The functionalities I've implemented.

- addblock:

   In blockchain.py there is a function called add_block(), this function will launch after the user use the addblock function. Then this function will call the function called pow_of_block() in the block.py to compute the hash value which meet the pre-defined limitation(difficulty). After computing, the new block's info will be stored in the database.

- printchain:

  In blockchain.py there is a function called print_chain(), this function will launch after the user use the printchain function. Then this function will call the function print_block() in the same file to print each block's info which has already established on the blockchain.

- printblock: 

  In blockchain.py there is a function called print_block(), this function will launch after the user use the printblock function. This function will print the info such as height, establish time, previous block's hash value, hash value and data of the block with specific height. 

- resetdb: 

  In the class Database() in utils.py there is a function called reset. This function will be launch after the user use the resetdb function. This function will delete all the info on the blockchain."# BTC" 
