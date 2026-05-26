class Bank:
    def __init__(self , bankholdername , currentamount):
        self.bank = bankholdername;
        self.amount = currentamount; 
    
    def deposite(self):
        deposite = self.currentamount + 500; 
        return deposite
    
    def withdraw(self):
        withdraw = self.currentamount - 1000; 
        return withdraw 
    
    def checkb(self):
        checkb = self.currentamount + self.deposite - self.withdraw; 
        return checkb
    
hdfc = Bank("Devu" , 5000); 
print(hdfc.bankh , hdfc.currentamount);     
        