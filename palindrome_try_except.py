def palindrome(word):
    return word == word[::-1]


def main():
    word = input('Please write a word') #I dont know how to solve it :c

    try:
        if type(word) != float:
            print(palindrome(word))
    except:
        print('You only can write words')

   


if __name__ == '__main__':
    main()