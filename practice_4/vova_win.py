from import_this import RACE_DATA

def winer(x):
    for key, value in RACE_DATA.items():
        for key_1, value_1 in value.items():
            if key_1 == 'FinishedPlace' and value_1 == x:
                winer_key = key
    return(winer_key)


def result(x):
    for key, value in RACE_DATA.items():
        if key == winer(x):
            for key_1, value_1 in value.items():
                if key_1 == 'RacerName':
                    print(f'Гонщик на {x} месте:')
                    print(f'\tИмя: {value_1}')
                elif key_1 == 'RacerTeam':
                    print(f'\tКоманда: {value_1}')
                elif key_1 == 'FinishedTimeSeconds':
                    minut = value_1 // 60
                    sec = value_1 % 60
                    hour = minut // 60
                    minut_1 = minut % 60
                    print(f'\t{hour:02}:{minut_1:02}:{sec:02}')
    return ''


for key, value in RACE_DATA.items():
    if key == winer(1):
        for key_1, value_1 in value.items():
            if key_1 == 'RacerName':
                name_win = (f'Выиграл - {value_1}!!! Поздравляем!')
                print(name_win)
                print('_' * len(name_win))
                print('Первые три места:')
                print('Гонщик на 1 месте:')
                print(f'\tИмя: {value_1}')
            elif key_1 == 'RacerTeam':
                print(f'\tКоманда: {value_1}')
            elif key_1 == 'FinishedTimeSeconds':
                minut = value_1 // 60
                sec = value_1 % 60
                hour = minut // 60
                minut_1 = minut % 60
                print(f'\t{hour:02}:{minut_1:02}:{sec:02}') 
                print('')

print(result(2))
print(result(3))    
print(winer(1)) 


# print(winer(3))
    # print(f'ключ: {key} значение: {value}')