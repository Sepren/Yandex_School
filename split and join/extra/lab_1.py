user = input().split(':')
login = [user[0]]
password = [user[1]]
real_users = [user[4][:user[4].find(',')]]
while user != '':
    user = input().split(':')
    login.append(user[0])
    password.append(user[1])
    real_users.append([user[4][:user[4].find(',')]])
    
passwords = input().split(';')
for i in range(len(password)):
    if password[i] in passwords:
        print(f'To: {login[i]}\n{real_users[i]}, ваш пароль слишком простой, смените его.')