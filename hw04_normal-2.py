import re

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

#Решение с помощью re
line_2_str = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print('Список с использованием "re": \n',line_2_str)
 
#Решение без re
symbol1 = list(map(lambda x: chr(x), list(range(65, 91)))) # Преобразуем список из кодов ANSI в список букв A-Z
symbol2 = list(map(lambda x: chr(x), list(range(97, 123)))) # Преобразуем список из кодов ANSI в список букв a-z
new_line = list(line_2)
 
new_list = []
i = len(new_line) - 1
# Находим  символ в верхнем регистре, после которого стоят еще два символа в верхнем регистре
while i >= 0:
    if new_line[i] in symbol2:
         new_list.append(new_line[i])
    elif new_line[i] in symbol1 and i <= len(new_line) - 3 and new_line[i+1] in symbol1 and new_line[i+2] in symbol1:
        new_list.append(new_line[i])
    else:
        new_list.append(' ')
    i -= 1
    #Переворачиваем список
new_list.reverse() 
 
i = 0
list_2 = []
 #Начальное условие поиска сортировки символов в верхнем регистре
registr = True 
#Фильтрация списка
while i <= len(new_list)-1:
    if new_list[i] in symbol2:
        registr = True
    if new_list[i] in symbol1 and new_list[i-1] in symbol2 and new_list[i-2] in symbol2:
        list_2.append(new_list[i])
        registr = False
    elif new_list[i] in symbol1 and registr == False:
        list_2.append(new_list[i])
    else:
        list_2.append(' ')
    i += 1
    #Преобразование в строку
stroka=''.join(list_2).split(' ') 
 
line_str_3 = [i for i in stroka if i != '']
print('Список без использования модуля "re": \n',line_str_3)