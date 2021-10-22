
from typing import Optional


print('''
    Welcome to Cryptocalculator
    Please select an option, writing the number.
    1.- Token price calculator.
    2.- Market Cap calculator.
    3.- More info.
''')

option = int(input('What is your selection?: '))

if option == 1 :
    token = input('Please write your token or crypto name')
    market_cap = int(input('Please write the estimated market cap: '))
    token_num = float(input('Please write the estimated or number of token/crypto abiable: '))

    token_price = market_cap / token_num

    print('The value estimated for ', token, ' is: $', token_price)
elif option == 2 :
    token = input('Please write your token or crypto name')
    token_num = float(input('Please write the estimated or number of token/crypto abiable: '))
    token_price = int(input('Please write the value of token what you estimate in future: '))

    market_cap = token_num * token_price

    print('The necessary marketcap for ', token, ' is: $', market_cap)
else :
    about_program = "Let's continue with Dogecoin example, Elon Musk has create a monster (Yes, Dogecoin has a community very strong previously), he uses Doge as a future but it's have not a real background on this token, and by the Elon's advertising was born new Guru's of Crypto saying stuff like 'Doge will have a value of 10 USD on 1 year', but that's ilogic, because that i create this simple and free program to help you to choose well your crypto investment."


    print('''
            Welcome to more info, her you will find info about of this simple and useful project.
            Why Cryptocalculator? Simple, in the oustside of internet are a lot of people who sell you an unreal whay of prices. For example 10 dollar on dogecoin, that's ilogic.
                ''')
     









