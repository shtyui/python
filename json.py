import json

fn='login.json'
account_list=[]
password_list=[]
with open(fn,'r') as fnObj:
    user_name=json.load(fnObj)
for c1 in user_name:
    account_list.append(c1["account"])
    password_list.append(c1["password"])
run=1
while run:
    login=input("請輸入帳號/離開(E)")
    new=0
    if login=='E':
        run=0
    else:
        for c1 in account_list:
            if(c1==login):
                print("%s歡迎回來"%login)
                new=1
        if new==0:
            with open(fn,'w')as fnObj:
                password=input("請輸入密碼: ")
                account_list.append(login)
                password_list.append(password)
                list1=zip(account_list,password_list)
                dict1=dict(list1)
                json.dump(dict1,fnObj)
                print("系統已經記錄你的帳號")

