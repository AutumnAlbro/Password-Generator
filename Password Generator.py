import random

print('Welcome To Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount of passwords needed: ')
number = int(number)

length = input('What is the length of your password: ')
length = int(length)

print('\n Here are your new generated passwords: ')

passwords = ''
for pwd in range(number):
    password = ''
    for c in range (length):
        password += random.choice(chars)
    passwords += password + '\n'

with open('passwordsgenerated.txt', 'a') as file:
    file.write(passwords)

    print(passwords)
