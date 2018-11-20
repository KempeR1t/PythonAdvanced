__author__ = 'Швец Александр Николаевич'

 '''
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип 
и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление 
в формат Unicode и также проверить тип и содержимое переменных.
'''

first = 'разработка'
second = 'сокет'
third = 'декоратор'
 print(f'{first} - {type(first)}, \n{second} - {type(second)}, \n{third} - {type(third)}')
 first_uni = '\u0440\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u043A\u0430'
second_uni = '\u0441\u043E\u043A\u0435\u0442'
third_uni = '\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440'
 print(f'\n Проверка в Unicode:\n'
      f'{first_uni} - {type(first_uni)}, \n{second_uni} - {type(second_uni)},'
      f' \n{third_uni} - {type(third_uni)}\n')
 '''
разработка - <class 'str'>, 
сокет - <class 'str'>, 
декоратор - <class 'str'>
Проверка в Unicode:
разработка - <class 'str'>, 
сокет - <class 'str'>, 
декоратор - <class 'str'>
'''


'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность 
кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''

first_byte = b'class'
second_byte = b'function'
third_byte = b'method'
print(f'{first_byte}, {type(first_byte)}, {len(first_byte)}')
print(f'{second_byte}, {type(second_byte)}, {len(second_byte)}')
print(f'{third_byte}, {type(third_byte)}, {len(third_byte)}')
print('\n')
'''
b'class', <class 'bytes'>, 5
b'function', <class 'bytes'>, 8
b'method', <class 'bytes'>, 6
'''

'''
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
'''

first_byte = b'attribute'
# second_byte = b'класс'
# third_byte = b'функция'
fourth_byte = b'type'
print(f'{first_byte}, {type(first_byte)},'
    # f'\n{second_byte}, {type(second_byte)},'
    #  f'\n{third_byte}, {type(third_byte)},'
      f'\n{fourth_byte}, {type(fourth_byte)},')
 '''
 b'attribute', <class 'bytes'>,
   File "D:/Projects/pyhton_2/1й урок/hw1.py", line 70
    second_byte = b'класс'
                 ^
SyntaxError: bytes can only contain ASCII literal characters.
   File "D:/Projects/pyhton_2/1й урок/hw1.py", line 71
    third_byte = b'функция'
                 ^
SyntaxError: bytes can only contain ASCII literal characters.
 b'type', <class 'bytes'>,
 '''

 '''
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
'''

first = 'разработка'
second = 'администрирование'
third = 'protocol'
fourth = 'standard'
print('\nstring to byte:')
first_to_byte = first.encode('utf-8')
second_to_byte = second.encode('utf-8')
third_to_byte = third.encode('utf-8')
fourth_to_byte = fourth.encode('utf-8')
 print(f'\nfirst_to_byte = {first_to_byte},'
      f'\nsecond_to_byte = {second_to_byte},'
      f'\nthird_to_byte = {third_to_byte},'
      f'\nfourth_to_byte = {fourth_to_byte}')

 '''
 first_to_byte = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
second_to_byte = b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5',
third_to_byte = b'protocol',
fourth_to_byte = b'standard'
'''

print('\nbyte to string:')
first_to_string = first_to_byte.decode('utf-8')
second_to_string = second_to_byte.decode('utf-8')
third_to_string = third_to_byte.decode('utf-8')
fourth_to_string = fourth_to_byte.decode('utf-8')
 print(f'\nfirst_to_string = {first_to_string},'
      f'\nsecond_to_string = {second_to_string},'
      f'\nthird_to_string = {third_to_string},'
      f'\nfourth_to_string = {fourth_to_string}')
 '''

first_to_string = разработка,
second_to_string = администрирование,
third_to_string = protocol,
fourth_to_string = standard
'''

 '''
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
в строковый тип на кириллице.
'''
import subprocess
args = ['ping', 'yandex.ru']
args2 = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
subproc_ping2 = subprocess.Popen(args2, stdout=subprocess.PIPE)
 for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))
 for line in subproc_ping2.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))
 print('\n')

 '''
 Обмен пакетами с yandex.ru [77.88.55.77] с 32 байтами данных:
 Ответ от 77.88.55.77: число байт=32 время=40мс TTL=51
 Ответ от 77.88.55.77: число байт=32 время=47мс TTL=51
 Ответ от 77.88.55.77: число байт=32 время=40мс TTL=51
 Ответ от 77.88.55.77: число байт=32 время=48мс TTL=51
 Статистика Ping для 77.88.55.77:
     Пакетов: отправлено = 4, получено = 4, потеряно = 0
     (0% потерь)
 Приблизительное время приема-передачи в мс:
     Минимальное = 40мсек, Максимальное = 48 мсек, Среднее = 43 мсек
 Обмен пакетами с youtube.com [173.194.122.136] с 32 байтами данных:
 Ответ от 173.194.122.136: число байт=32 время=40мс TTL=112
 Ответ от 173.194.122.136: число байт=32 время=48мс TTL=112
 Ответ от 173.194.122.136: число байт=32 время=40мс TTL=112
 Ответ от 173.194.122.136: число байт=32 время=49мс TTL=112
 Статистика Ping для 173.194.122.136:
     Пакетов: отправлено = 4, получено = 4, потеряно = 0
     (0% потерь)
 Приблизительное время приема-передачи в мс:
     Минимальное = 40мсек, Максимальное = 49 мсек, Среднее = 44 мсек
 '''

 '''
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
«сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате 
Unicode и вывести его содержимое.
'''
 f_n = open('test_file.txt', 'r')
print(f_n)
f_n.close()

 '''
 <_io.TextIOWrapper name='test_file.txt' mode='r' encoding='cp1251'>
 Делаем вывод что кодировка файла - ср1251
 '''
 with open('test_file.txt', encoding='utf-8') as f_n:
    for line in f_n:
        print(line, end='')
 '''
сетевое программирование
сокет
декоратор