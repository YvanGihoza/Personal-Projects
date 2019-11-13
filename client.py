import socket

# port of connection 
port = 23236

# create a socket object 
s = socket.socket()


# connect to the server
s.connect(('127.0.0.1', port))

while True:

   # provide user the different choices
   print("Type 1 to Deposit")
   print("Type 2 to Withdrawl")
   print("Type 3 to Check balance")
   print("Type any other key to quit")

   # get input 
   makeChoice = input()
   userChoice = str.encode(str(makeChoice), 'utf-8')
   s.send(userChoice)
   print(s.recv(1024))

   makeChoice = input()
   userChoice = str.encode(str(makeChoice), 'utf-8')
   s.send(userChoice)
   print(s.recv(1024))

s.close