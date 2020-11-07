# This is a sample Python script.
import random
import re
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def gentelebook(n):
    my_file = open('telebook.txt', 'w')
    for i in range(n):
        my_file.write(str(random.randint(9000000000, 99999999999))+'\n')
    my_file.close()


N = int(input('Введите количество генерируемых номеров:'))
if N <= 0 | N > 10000:
    print('Выход')
else:
    gentelebook(N)
input_file = open('telebook.txt', 'r')
output_file = open('validtelebook.txt', 'w')
invalid_file = open('invalidtelebook.txt', 'w')
pattern = r"([78]\d{10})|(9\d{9})"
telebook = input_file.read()
telebook = telebook.splitlines()
for i in range(N):
    match = re.fullmatch(pattern, telebook[i])
    if match:
        output_file.write(telebook[i]+'\n')
    else:
        invalid_file.write(telebook[i]+'\n')
input_file.close()
output_file.close()
invalid_file.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
