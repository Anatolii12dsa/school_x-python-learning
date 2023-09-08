alphabet = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'X',
    10: 'Y',
}

o_letter = alphabet.get('Z', None)
if not bool(o_letter):
    print('No 0')

for key, value in alphabet.items():    #.keys() .values()
    # if value in 'AY':
    print(f'ключ: {key} значение: {value}')