import socket, sys
class Account():

    # constructor
    def __init__(self):
        self.balance = float(10000)  
        self.initBalance = self.balance
        #self.deposit_amount = 0
        #self.withdrawal_amount = 0

    # deposit function
    def deposit(self, amount, c):
        self.balance += amount
        #self.deposit_amount += amount
        print("Deposited: $%.3f" % (amount))
        data = "Deposited: $%.3f" % (amount)
        c.send(data.encode())

    # withdrawal function
    def withdrawal(self, amount, c):
        if self.balance >= amount:
           self.balance -= amount
        #self.withdrawal_amount += amount
           print("Withdrawn: $%.3f" % (amount))
           data = "Withdrawn: $%.3f" % (amount)
           c.send(data.encode())
        else:
           print("NOT ENOUGH BALANCE FOR THE TRANSACTION! SYSTEM EXIT")
           data ="NOT ENOUGH BALANCE FOR THE TRANSACTION! SYSTEM EXIT"
           c.send(data.encode())
           sys.exit(1)

    # check balance function
    def print_balance(self, c):
        print("Balance: $%.3f" % self.balance)
        data = "Balance: $%.3f" % self.balance
        c.send(data.encode())

    # wrong input exit
    def wrongIn(self, c):
        print("WRONG INPUT SYTEM EXIT!")
        data = "WRONG INPUT SYTEM EXIT!"
        c.send(data.encode())

def main():

    # socket object 
    s = socket.socket()          
  
    # reserve a port
    port = 23236                
  
    # Bind to the port 
    s.bind(('', port))         
    print "socket to: %s" %(port) 
  
    # listening mode 
    s.listen(5)

    # connect with client 
    c, addr = s.accept()      
    print 'got connection from', addr    
   
    # creating an object of the class
    account = Account()

    while True:
        # get the selected option from the user
        makeChoice = c.recv(1024).decode()

        # deposit
        if makeChoice == b"1":
            c.send("amount to deposit: ".encode())
            amount = float(c.recv(1024).decode())
            account.deposit(amount, c)

        # withdrawing 
        elif makeChoice == b"2":
            c.send("amount to withdraw: ".encode())
            amount = float(c.recv(1024).decode())
            account.withdrawal(amount, c)

        # check balance
        elif makeChoice == b"3":
            account.print_balance(c)

        # Any other key to exit
        else:
            account. wrongIn(c)
            sys.exit(1)

    c.close()

main()