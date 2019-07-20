#Udemy OOP Challenge 7/19/2019

#For this challenge, create a bank account class that has two attributes:
# owner and balance and two methods: deposit and withdrawl
#As an added requirement, withdrawals may not exceed the available balance
#Instantiate your class, make several deposits and withdrawals,
#and test to make sure the account can't be overdrawn.


class Account(object):
            
    def __init__(self):#,owner,balance):
        self.owner = input("What is your name?: ")
        #self.owner = owner
        #self.balance = balance
        self.balance = float(input("What is the balance of your account?: "))


    #@classmethod
    #def get_user_input(self):
    #    while 1:
    #        try:
    #            owner = input("What is your name?: ")
    #            balance = float(input("What is the balance of your account?: "))
    #            return self(owner, balance)
    #        except:
    #            print('Invalid Input')
    #            continue
            
    def deposit(self, d_amount):

        if d_amount > 0:
            self.balance += d_amount
            recipt_YN = (input("Would you like a recipt? Y/N: ")).upper()

            if recipt_YN == 'Y':
                print("Your new balance is {0}.".format(self.balance))
            elif 'N':
                print("Good Bye")
            else:
                print("Invalid Response") #figure out how to make this re-loop
        else:                                    #back to ask wether they want a recipt or not
            print("Invalid Entry for a deposit.")
    
    def withdrawl(self, w_amount):
        if w_amount > 0 and w_amount <= self.balance:
            self.balance -= w_amount
            recipt_yn = (input("Would you like a recipit? Y/N: ")).upper()

            if recipt_yn == 'Y':
                print("Your new balance is {0}.".format(self.balance))
            elif recipt_yn == 'N':
                print("Good Bye")
            else:
                print("Invalid response")
        else:
            print("Invalid response for a withdrawal")


#owner = input("What's your name?")
#balance = float(input("How much money do you have in your Bank Account?: "))

account1 = Account()

w_or_d = (input("Would you like to make a deposit or take a with drawl? W/D: ")).upper()
if w_or_d == 'W': 
    withdrawl_amount = float(input("How much would you like to withdrawl?:"))
    account1.withdrawl(withdrawl_amount)
elif w_or_d == 'D':
    deposit_amount = float(input("How much would you like to deposit?: "))
    account1.deposit(deposit_amount)
else:
    print("Invalid Response")
