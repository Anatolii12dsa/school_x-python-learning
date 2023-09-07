import string
# new_name: str = input('type name:')

# greet_massage = 'hello bob'

# greet_massage: str =(greet_massage [:-3] + new_name)

# greet_massage: str = greet_massage.replace('bob', new_name)

# print(greet_massage)



# river: str = 'mmississippi'

# print('m' + river.lstrip('m'))



# words: str = 'dsa das das'

# print(words.split())


# words: str = '<!--dsa das das--!>'

# print(words.strip('<>!-').split())



# num: str = string.digits
# word: str = 'hell123o b23ob'
# for number in num:
#     word = word.replace(number, '')


# print(word)

# _set: set = ([])

# num: str = string.digits
# word: str = 'hell123o b23ob'
# _word: str = ''
# for ch in word:
#     if ch in num:
#         continue
#     else:
#         _word += ch
# word = _word
# del _word

# print(word)

# words: str = 'hello Bob, are you a bob? BOB!'
# words = words.lower().find('bob')

# while True:
#     bob_index = words.lower().find('bob')
#     if bob_index == -1:
#         break
#     else:
#        words = words[:bob_index]
#         print(words)
       
       
# print(words.casefold())
# print(words.capitalize()) - первая заглавная отсальные маленькие
#.upper - верхний регистрб lowe - нижний


_list: list = [1, 2, 3]
_str: str = '123'
_tuple: tuple = (
    [1, 3],
    [2, 3],
    [4, 3],
    [9, 6]

)

_list[-1] = 5
_tuple[1][1] = 5


print(_list, _str, _tuple)