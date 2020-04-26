import pickle
dict_1 = {
}
print(dict_1)
filename = 'Email_dict.txt'
file = open(filename, 'rb')
x = pickle.load(file)
dict_1.update(x)

def create_account():
    x = input('Please enter your new username: ')
    if x in dict_1.keys():
        return 'Email already in use!'
    if x not in dict_1.keys():
        dict_1.update( {x: 'value',})
        y = input('Please enter your new password: ')
        if y not in dict_1.values():
            dict_1.update({x: y,})
            return 'Account created!'

print(create_account())
print(dict_1)

file_update = open(filename, 'wb')
pickle.dump(dict_1, file_update)
file_update.close()