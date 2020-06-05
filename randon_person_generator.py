
import string
from random import choice
import random
# or we can improt random

# lsit of first names

first_names = ['Jon', 'Rick', 'Bill', 'Ben', 'Vishal']

last_names = ['Hu','Zhang', 'Tian', 'Shah', 'Patel']

email_services = ['@gmail.com', '@yahoo.com','@hotmail.com','@outlook.com', '@icloud.com']
random_phone_number1 = 0
random_phone_number2 = 0
random_phone_number3 = 0

#randon phone format : 123-444-5575
for x in range(100):
    random_name = '{} {}'.format(choice(first_names), choice(last_names))
    email = '{}.{}{}'.format(choice(first_names).lower(), choice(last_names).lower(), choice(email_services))
    print('------------------------------------------')
    print(random_name)
    print(email)
    random_phone_number1 = random.randint(101, 999)
    random_phone_number2 = random.randint(101, 999)
    random_phone_number3 = random.randint(1001, 9999)
    print('{}-{}-{}'.format(random_phone_number1, random_phone_number2, random_phone_number3))
    print('------------------------------------------')
