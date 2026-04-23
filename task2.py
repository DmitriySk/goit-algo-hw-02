from collections import deque
import re

def check_palindrome_simple(str):
    str_cleaned = re.sub(r'[^A-Za-zА-Яа-я0-9]', '', str).lower()
    return str_cleaned == str_cleaned[::-1]

def check_palindrome_deque(str):
    str_cleaned = re.sub(r'[^A-Za-zА-Яа-я0-9]', '', str).lower()
    print(str_cleaned)
    str_list = deque(str_cleaned.lower())
    while len(str_list):
        if len(str_list) == 1:
            return True
        if str_list.popleft() != str_list.pop():
            return False
    return True

str1 = 'A man, a plan, a canal: Panama'
str2 = 'Was it a car or a cat I saw?'
str3 = '12321'
str4 = 'Я несу гусеня'
str5 = 'Хата на канатах'
str6 = 'Три психи пили Пилипихи спирт'

strings = [str1, str2, str3, str4, str5, str6]

for str in strings:
    print(str)
    print(check_palindrome_simple(str))
    print(check_palindrome_deque(str), end='\n\n')