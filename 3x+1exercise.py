#Finding a code to represent the 3x+1 mathematica excercise

count = 1 #count of cicles
exp = 1 #exponent of excercise
turns = 0

result = int(input('Please write a number. '))
print(result)

while count > 0 :

    if result % 2 == 0:
        result = result / 2
        print(result)
    else:
        result = result*3 + 1
        print(result)
    if result == 1:
        count = 0

    turns += 1

print('The excercise need ', turns , ' turns to end.')
    



