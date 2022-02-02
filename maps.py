import subprocess
import shlex
newline = '<br>'

# жалобы
def complaints_func():
    complaints = '**ЖАЛОБЫ**'
    complaintsText = input("Введите жалобы пациента: ")

    file.write(complaints + ' ' + '<u>' + complaintsText + '</u>')
    file.write(newline)

# анамнез
def anamnesis_func():
    anamnesis = '**АНАМНЕЗ** (в т.ч. – эпид., аллерг., гинекол. по показаниям)'
    anamnesisText = input("Введите анамнез: ")

    file.write(anamnesis + ' ' + '<u>' + anamnesisText + '</u>')
    file.write(newline)

# обьективно
def objectively_func():
    objectively = '**ОБЪЕКТИВНО:**'
    objGenState = 'общее состояние'
    print("Общее состояние (удовл.(1), ср. тяжести(2), тяжелое(3), терминальное(4))")
    objGenStateUserInput = input("Выберите общее состояние пациента: ")

    if objGenStateUserInput == '1':
        objGenStateUserChoise = '(<u>удовл.</u>, ср. тяжести, тяжелое, терминальное)'
        file.write(objectively + ' ' + objGenState + objGenStateUserChoise + ' ')
    elif objGenStateUserInput == '2':
        objGenStateUserChoise = '(удовл., <u>ср. тяжести</u>, тяжелое, терминальное)'
        file.write(objectively + ' ' + objGenState + objGenStateUserChoise + ' ')
    elif objGenStateUserInput == '3':
        objGenStateUserChoise = '(удовл., ср. тяжести, <u>тяжелое</u>, терминальное)'
        file.write(objectively + ' ' + objGenState + objGenStateUserChoise + ' ')
    elif objGenStateUserInput == '4':
        objGenStateUserChoise = '(удовл., ср. тяжести, тяжелое, <u>терминальное</u>)'
        file.write(objectively + ' ' + objGenState + objGenStateUserChoise + ' ')

# сознание
def conscience_func():
    conscience = 'Сознание: '
    print('Сознание: ясное(1), оглушение(2), сопор(3), кома(4)')
    conscienceUserInput = input("Выберите уровень сознания пациента: ")

    if conscienceUserInput == '1':
        conscienceUserChoise = '<u>ясное</u>, оглушение, сопор, кома -- глубина по шкале'
        file.write(conscience + ' ' + conscienceUserChoise + ' ')
    elif conscienceUserInput == '2':
        conscienceUserChoise = 'ясное, <u>оглушение</u>, сопор, кома -- глубина по шкале'
        file.write(conscience + ' ' + conscienceUserChoise + ' ')
    elif conscienceUserInput == '3':
        conscienceUserChoise = 'ясное, оглушение, <u>сопор</u>, кома -- глубина по шкале'
        file.write(conscience + ' ' + conscienceUserChoise + ' ')
    elif conscienceUserInput == '4':
        conscienceUserChoise = 'ясное, оглушение, сопор, <u>кома</u> -- глубина по шкале'
        file.write(conscience + ' ' + conscienceUserChoise + ' ')
    file.write(newline)

# Глазго 15 баллов Положение активное, пассивное, вынужденное:
def glasgo_func():
    glasgo = 'Глазго'
    glasgoUserUnput = input("Введите баллы по шкале Глазго ")
    file.write(glasgo + ' ' + '<u>' + glasgoUserUnput + ' баллов ' + '</u>')
    
# положение пациента
def position_func():
    position = 'Положение'
    print('Положение активное(1), пассивное(2), вынужденное(3)')
    positionUserInput = input("Введите положние пациента: ")

    if positionUserInput == '1':
        positionUserChoise = '<u>активное</u>, пассивное, вынужденное'
        file.write(position + ' ' + positionUserChoise)
    elif positionUserInput == '2':
        positionUserChoise = 'активное, <u>пассивное</u>, вынужденное'
        file.write(position + ' ' + positionUserChoise)
    elif positionUserInput == '3':
        positionUserChoise = 'активное, пассивное, <u>вынужденное</u>'
        positionForced = input("Введите описание вынужденного положения пациента: ")
        file.write(position + ' ' + positionUserChoise + ' ' + '<u>' + positionForced + '</u>')
    file.write(newline)

# кожные покровы
def skin_covers_func():
    skinCovers = 'Кожные покровы:'
    print('Состояние кожных покровов: сухие(1), влажные(2), обычной окраски(3), бледные(4), '
    + 'гиперемия(5), цианоз(6), желтушность(7), описать кожные покровы(8), закончить ввод(9).')
    
    skinCoversDict = dict()
    skinCoversDict['сухие'] = False
    skinCoversDict['влажные'] = False
    skinCoversDict['обычной окраски'] = False
    skinCoversDict['бледные'] = False
    skinCoversDict['гиперемия'] = False
    skinCoversDict['цианоз'] = False
    skinCoversDict['желтушность'] = False
    skinCoversDict['описать кожные покровы'] = False
    skinCoversDict['закончить ввод'] = False
    
    userInput = True
    while userInput:
        skinCoversUserInput = input("Введите состояние кожных покровов пациента:")
        if skinCoversUserInput == '1':
            skinCoversDict['сухие'] = True
        elif skinCoversUserInput == '2':
            skinCoversDict['влажные'] = True
        elif skinCoversUserInput == '3':
            skinCoversDict['обычной окраски'] = True
        elif skinCoversUserInput == '4':
            skinCoversDict['бледные'] = True
        elif skinCoversUserInput == '5':
            skinCoversDict['гиперемия'] = True
        elif skinCoversUserInput == '6':
            skinCoversDict['цианоз'] = True
        elif skinCoversUserInput == '7':
            skinCoversDict['желтушность'] = True
        elif skinCoversUserInput == '8':
            skinCoversDict['описать кожные покровы'] = True
        elif skinCoversUserInput == '9':
            userInput = False
        
    file.write(skinCovers + ' ')
        
    for key, value in skinCoversDict.items():
        if value == True:
            if key == 'закончить ввод':
                file.write(' ')
            elif key == 'описать кожные покровы':
                userTimeInput = input('Опишите кожные покровы: ')
                file.write('<u>' + userTimeInput + '</u>')
            elif key == 'желтушность':
                file.write('<u>' + key + '</u>')   
            else:
                file.write('<u>' + key + '</u>' + ', ')
        elif value == False:
            if key == 'закончить ввод':
                file.write(' ')
            elif key == 'описать кожные покровы':
                file.write(' ')
            elif key == 'желтушность':
                file.write('<u>' + key + '</u>')
            else:
                file.write(key + ', ')
    file.write(newline)

#сыпь
def rash_func():
    # раздел сыпь
    rash = 'Сыпь: '
    rashUserInput = input("Наличие сыпи у пациента: Отсутствует(1), Свое описание(2)" + ' ')

    if rashUserInput == '1':
        file.write(rash + ' ' + '<u>' + 'Отсутствует' + '</u>' + ' ')
    else:
        userInput = input("Опишите сыпь: ")
        file.write(rash + ' ' + '<u>' + userInput + '</u>' + ' ')

    # раздел зев
    zev = 'Зев: '
    zevUserInput = input("Опишите зев пациента: Розовый(1), Свое описание(2)" + ' ')

    if zevUserInput == '1':
        file.write(zev + ' ' + '<u>' + 'Розовый' + '</u>' + ' ')
    else:
        userInput= input("Опишите зев пациента:" + ' ')
        file.write(zev + ' ' + '<u>' + userInput + '</u>' + ' ')

    # раздел миндалины
    tonsils = 'Миндалины: '
    tonsilsUserInput = input("Опишите миндалины пациента: Не увеличены, без налета(1), свое описание(2)" + ' ')

    if tonsilsUserInput == '1':
        file.write(tonsils + ' ' + '<u>' + 'Не увеличены, без налета' + '</u>' + ' ')
    else:
        userInput = input("Опишите миндалины пациента:" + ' ')
        file.write(tonsils + ' ' + '<u>' + userInput + '</u>' + ' ')

# главная программа
file = open('list.md', 'w') # открываем карту на запись
complaints_func() # жалобы
anamnesis_func() # анамнез
objectively_func() # объективное состояние
conscience_func() # уровень сознания
glasgo_func() # шкала комы Глазго
position_func() # позиция пациента
skin_covers_func() # кожные покровы
rash_func() # сыпь, зев, миндалины
file.close() # закрываем файл
