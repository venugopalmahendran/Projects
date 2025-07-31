user_name=input('enter the name:')
password=input("enter the password:")
count=password.__len__()
while count<4 or count>4:
    if count==4:
        break
    else:
        password=input('enter the 4 digit password:')
        count=0
        count=password.__len__()
        continue
while count==4 :
    if user_name=='venugopal':
        print('hi...!',user_name,)
    elif user_name!='venugopal':
        print('username is incorrect')
        user_name=input('enter username correctly:')
        continue
    if password=='1234':
        print('logging...')
        break
    elif password!='1234':
        print('password is incorrect')
        password=input('enter password correctly:')
        continue