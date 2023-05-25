import sys

def zero_to_thousand(n, is_thousand):
    res = str()

    if is_thousand != 'Yes':
        list_simply_number = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    else:
        list_simply_number = ['одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']

    list_decimal_number = ['двадцать', 'тридцать', 'cорок', 'пятьдесят', 'шестьдесят', 'семьдесят',
                           'восемьдесят', 'девяносто']

    list_teen_number = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
                           'семнадцать', 'восемнадцать', 'девятнадцать']

    list_hundred_number = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот',
                           'девятьсот']


    if n >= 100:
        res = list_hundred_number[n//100 - 1] + ' '

    if n%100 > 20:
        res = res + list_decimal_number[((n%100)//10) - 2] + ' '

    if n%100 >= 10 and n%100 < 20:
        return res + list_teen_number[(n%100)%10]

    if n%10 != 0:
        res = res + list_simply_number[n%10 - 1]

    return res

def choice_of_word_endings(n, word):
    if n%10 == 1 and (n%100 < 10 or n%100 > 20):
        return word[0]
    elif (n%10 >= 2 and n%10 <= 4) and (n%100 < 10 or n%100 > 20):
        return word[1]
    else:
        return word[2]

def main(n):
    try:
        n = int(n)
    except ValueError:
        sys.exit('Error input')

    if n < 0 or n > 1000000000:
        sys.exit('Not_support')

    res = str()

    million = ['миллион', 'миллиона', 'миллионов']
    thousand = ['тысяча', 'тысячи', 'тысяч']

    if n >= 1000000:
        res = zero_to_thousand(n//1000000, 'No') + ' ' + choice_of_word_endings(n//1000000, million) + ' '

    if n%1000000 >= 1000:
        res = res + zero_to_thousand(((n%1000000) // 1000), 'Yes') + ' ' + choice_of_word_endings(((n%1000000) // 1000), thousand) + ' '

    if n%1000 != 0:
        res = res + zero_to_thousand((n%1000), 'No')

    return res

print(main(input()))
