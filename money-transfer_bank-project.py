users = {
    'james':{
    'password':'james123',
    'balance': 34231
  }, 

  'billy':{
      'password':'billy.jean',
      'balance' :232312
           
  },

  'freddy':{
      'password':'bohamian.freddy',
      'balance' : 3233422
  }
}


def login(users):
    for n in range(3):
        creat_account = input('\n create an account(yes,no) \n')
        if creat_account in ('yes','YES','Yes'):
           return 'creat'
        elif creat_account in ('no','NO','No'):
         username = input('name: ')
         password = input('password: ')
        
        
         if username in users and password == users[username]['password']:
            print(f"welcome {username}")
            return username
        
        print('invalid credentials')
    
        
    
    return None

def account_creat(users):
   name = input('name: ')
   password = input('password: ')
   users[name] = {'password': password,'balance': 0}



def add(money,amount):
    return money + amount

def withdraw(money,amount):
    if amount > money : return None
    return money - amount  

def menu(current_user):
    while True:
        ask = input(
            '\n 1. see balance '
            '\n 2. add money'
            '\n 3. withdraw money'
            '\n 4. transfer money '
            '\n 5. logout \n'
        )

        if ask == '1' or ask == 'see balance':
            print(f"your balance is : ${users[current_user]['balance']}")
        
        elif ask in ('2','add','add money'):
            try:
             amount = int(input('input amount: '))
            except ValueError:
                print('enter a valid amount')
                continue

            users[current_user]['balance'] = add(users[current_user]['balance'],amount)
            print(f"\n money succesfully added\n"
                 f"current balance : ${users[current_user]['balance']}"
                  )

        elif ask in ('3','withdraw','withdraw money'):
            try:
             amount = int(input('how much money whould you like to withdraw : '))
            except ValueError:
                print('enter a valid number')
                continue
            else:
             result = withdraw(users[current_user]['balance'],amount)
             if result == None:
                print('\n not enough money')

             else:

              users[current_user]['balance'] = result

              print(f"money succesfully withdrawn \n current balance is ${users[current_user]['balance']}")
        
        elif ask in ('4','transfer','transfer amount'):
           sender = current_user

           receiver = input('whom to transfer: ')
           if receiver == sender:
              print('cant transfer to yourself')
              continue
           try:
            amount = int(input('transfer amount: '))
           except ValueError:
              print('enter a valid amount')
              continue
           result = transfer(users,sender,receiver,amount)
                             
           if result == False:
              print('user not found')

           elif result == None:
              print('not enough balance')
              continue

           elif result == True:  
        
            print(f"transiction succesfull \n user balance is {users[sender]['balance']}")



        elif ask in ('5','logout','log out'):

            break



        else:

           continue
  
def transfer(users,sender,receiver,amount):
   if sender in users and receiver in users:
      
      
      if amount > 0 and amount <= users[sender]['balance']:
       
       users[sender]['balance'] = withdraw(users[sender]['balance'],amount)
       users[receiver]['balance'] = add(users[receiver]['balance'],amount)

       return True
   
   else:
      return False
   
      

def bank(users):
 while True:
    username = login(users) 
    if username == None:
        print('account locked') 
        break
    elif username == 'creat':
       account_creat(users)
       continue
    menu(username)  

bank(users)