import pickle
dict_1 = {
}
print(dict_1)
filename = 'Email_dict.txt'
file = open(filename, 'rb')
x = pickle.load(file)
dict_1.update(x)

print(dict_1)
def login():
    a = input('Please enter your Email: ')
    if a in dict_1.keys():
        b = input('Please enter your password!: ')
        if dict_1[a] == b:
            return 'You may login!'
        elif dict_1[a] != b:
            print('Invalid password!')
            return login()
    elif a not in dict_1.keys():
        print('Invalid Email!')
        return login()


print(login())