class ATM:#defines a class named ATM
  # initialization(__init__)
  def __init__(self,balance,pin):#constructor of ATM class
    self.balance=0.0#initial balance
    self.password=pin#passed parameter pin to password
    self.transactions = []#empty transaction list

  #This method checks if the provided pin is correct.   
  def check_pin(self, pin):#takes a pin as input
        try:
            pin = int(pin)
            if pin != self.password:#verifies entered pin is same as password
                print("Incorrect pin. Please try again.")
                return False
            return True
        except ValueError:
            print("Invalid input. Pin must be a number.")
            return False

  #This function manages depositing money.
  def deposit(self,amount,pin):
    if not self.check_pin(pin):#It first validates the PIN using check_pin(pin). If the pin is wrong, the function returns.
            return
    if amount>0:#checks amount is greater than 0
            self.balance += amount#balance get updated
            self.transactions.append(f"Deposited {amount}")#add the deposit in transaction history
            print(f"Deposited {amount}.New amount is {self.balance}.")
    else:
            print(f"deposit amount must be positive.")
  
  #This function processes withdrawing cash.
  def withdrawl(self,amount,pin):
    if not self.check_pin(pin):#It verifies the PIN
            return
    if amount>0 and amount<=self.balance:#checks if amount is greater than 0 and less than equal to balance
      self.balance-=amount
      self.transactions.append(f"withdrew {amount}")#it takes the amount from the balance, adds the transaction to the transactions history
      print(f"withdrawal{amount}.New amount is {self.balance}.")

  #It then returns the present balance
  def balance_inquiry(self,pin):
    if not self.check_pin(pin):#It verifies the PIN
            return
    return self.balance
     
  #This function used to change the old pin
  def pin_change(self,pin):
    if not self.check_pin(pin):#It verifies the PIN
            return
    pin=int(input("Enter your new pin:"))
    print(f"Your pin has changed successfully to {pin}")
    self.password=pin#modifies the password.
 
  #
  def Transaction_history(self,pin):
    if not self.check_pin(pin):#It verifies the PIN
            return
    print(f"Transaction History:")
    for transaction in self.transactions:#loops through the transaction history
          print(transaction)
    print(f"Current balance is: {self.balance}")#prints current balance
    
  def run(self):
    while True:
            print("\n1.Deposit\n2.Withdraw\n3.Balance Inquiry\n4.Pin Change\n5.Transaction History\n6.Exit")#It prints a menu of choices.
            choice = int(input("enter your choice:"))#takes input of choice
            if choice==1:
                pin=input("Enter your pin:")
                amount = float(input("Enter the amount to deposit:"))
                self.deposit(amount,pin)#calls the deposit function 

            elif choice==2:
                pin=input("Enter your pin:")
                amount = float(input("Enter the amount to withdraw:"))
                self.withdrawl(amount,pin) #calls the withdrawl function 
    
            elif choice==3:
                pin=input("Enter your pin:")
                balance = self.balance_inquiry(pin)#calls the balance_inquiry function 
                print(f"Your balance is: {balance}") 
    
            elif choice==4:
              pin=int(input("Enter your pin:"))
              if pin!=self.password:
                print("Incorrect pin.Please try again.")
              else:
                self.pin_change(pin)#calls the pin_change function 
    
            elif choice==5:
                pin=input("Enter your pin:")
                self.Transaction_history(pin)#calls the Transaction_history function 
    
            elif choice==6:
                break#Terminates the loop
            else:
                print(f"invalid choice .Please try again")
        
ATM_machine=ATM(0.0,1234)#object 
ATM_machine.run()#uses run method 