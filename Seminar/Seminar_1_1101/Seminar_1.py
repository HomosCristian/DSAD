print('hello Python!')

a = 5
print(type(a), a)
a = 'mama mea'
print(type(a), a) # acesta un comentariu

# Tutorial Python
# https://www.tutorialspoint.com/python/index.htm

'''
Aceste
este un
comentariu care se extinde
pe 
mai multe
linii
'''

a = b = c = 5
print(a, b, c)

a, b, c = 1, 3.14, 'mama si tata'
print(a, b, c)

# operatori noi pentru tipuri numerice
# operatorul de cat al impartirii
a = 6
b = 4
print('catul impartirii lui a la b:', a // b)
print('restul impartirii lui a la b:', a % b)
# operatorul de ridicare la putere
print(' a la puerea b:', a ** b)

# siruri de caractere (strings)
string_1 = 'mama mea'
# stringurile sunt immutable
print(type(string_1), string_1, id(string_1))
string_1 += ' este minunata!'  # operatul += supraincarcat pentru concatenare de stringuri
print(type(string_1), string_1, id(string_1))

string_2 = 'mama said: "come home early!"'
print(string_2)
string_3 = '''mama said: "don't be late"'''
print(string_3)

# liste
list_1 = [1, 3.14, 'mama', [1, 2, 3]]
print(type(list_1), list_1)
  # stringul pare a fi interpretat ca o lista de caractere
print(list_1)
# list_1 = list_1 + 'inca un element'  # incorect
# print(list_1)
list_1 += ['un alt element']  # concatenare de liste
list_1 = list_1 + ['inca un element']
print(list_1)

# list slicing
list_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_2)
print(list_2[:])  # [inceput : sfarsit : pas], implicit pasul este 1


# accesare ultim element al listei
print(list_2[-1])
print(list_2[0:-1:1])  # in slicing este un interval deschis la dreapta

# selectare sublista de valori pentru indecsii pari
print(list_2[::2])
# selectare sublista de valori pentru indecsii impari
print(list_2[1::2])
# obtinerea elementelor listei in ordine inversa
print(list_2[-1::-1])
print(list_2[::-1])
