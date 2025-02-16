def create_account(name: str,holder: str , account_holders: list=[]): #default value of account_holders is mutable
    if account_holders is None:
        account_holders = []
    #print(id(account_holders))
    account_holders.append(holder)

    return {    
    'name': name,
    'main_account_holder': holder,
    'account_holders': account_holders
    }
a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')
print(a2) #the account holders of a2 will be ['Rolf', 'Jen'] because the default value of account_holders is mutable

