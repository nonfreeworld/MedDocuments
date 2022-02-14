'''
###
The MIT License (MIT)
Copyright © 2022 <Mikhail Pakharev>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###
'''


# html
def html_begin():
  file.write('<!DOCTYPE html>')
  file.write('<html>')
  file.write('  <head>')
  file.write('    <meta charset="utf-8">')
  file.write('  </head>')
  file.write('  <body style="font-family:free sans; font-size: 13px;">')

def html_exit():
  file.write('  </body>')
  file.write('</html>')

# жалобы
def complaints_func():
    complaints = '<b>Жалобы: </b>'
    complaintsText = input("Введите жалобы пациента: ")

    file.write(complaints + '<u>' + complaintsText + '</u>')
    file.write('<br>')

# анамнез
def anamnesis_func():
  anamnesis = '<b>АНАМНЕЗ</b> (в т.ч. – эпид., аллерг., гинекол. по показаниям)'
  anamnesisText = input("Введите анамнез: ")

  file.write(anamnesis + ' ' + '<u>' + anamnesisText + '</u>')
  file.write('<br>')

# объективно
def objectively_func():
  objectively = '<b>ОБЪЕКТИВНО:</b>'
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
    conscienceUserChoise = '<u>ясное</u>, оглушение, сопор, кома - '
    file.write(conscience + ' ' + conscienceUserChoise + ' ')
  elif conscienceUserInput == '2':
    conscienceUserChoise = 'ясное, <u>оглушение</u>, сопор, кома - '
    file.write(conscience + ' ' + conscienceUserChoise + ' ')
  elif conscienceUserInput == '3':
    conscienceUserChoise = 'ясное, оглушение, <u>сопор</u>, кома - '
    file.write(conscience + ' ' + conscienceUserChoise + ' ')
  elif conscienceUserInput == '4':
    conscienceUserChoise = 'ясное, оглушение, сопор, <u>кома</u> - '
    file.write(conscience + ' ' + conscienceUserChoise + ' ')
  file.write('<br>')

# Глазго 15 баллов Положение активное, пассивное, вынужденное:
def glasgo_func():
  glasgo = 'глубина по шкале Глазго'
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
  file.write('<br>')


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
        file.write(key + ' ')
      else:
        file.write(key + ', ')

  file.write('<br>')

#сыпь зев
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
  file.write('<br>')


# лимфоузлы пролежни отеки температура
def lymph_nodes():
  # раздел лимфоузлы
  lymph = 'Лимфоузлы '
  lymphUserInput = input("Лимфоузлы: 1. Не увеличены 2. Опишите лимфоузлы пациента ")

  if lymphUserInput == '1':
    file.write(lymph + ' ' + '<u>' + 'Не увеличены ' + '</u>' + ' ')
  else:
    userInput = input("Опишите лимфоузлы пациента: ")
    file.write(lymph + ' ' + '<u>' + userInput + '</u>' + ' ')


  # раздел пролежни
def bed_sores():
  bedsores = 'Пролежни '
  bedsoresUserInput = input("Если ли пролежни у пациента: 1. Пролежней нет 2. Опишите пролежни ")

  if bedsoresUserInput == '1':
    bedsoresOutput = file.write(bedsores + ' ' + '<u>' + 'Нет ' + '</u>' + ' ')
    return bedsoresOutput
  else:
    userInput = input("Опишите пролежни: ")
    bedsoresOutput = file.write(bedsores + ' ' + '<u>' + userInput + '</u>' + ' ')
    return bedsoresOutput

# раздел Отеки
def swelling_func():
  swelling = 'Отеки '
  swellingUserInput = input("Есть ли отеки у пациентка: 1. Нет 2. Опишите отеки пациента ")

  if swellingUserInput == '1':
    file.write(swelling + ' ' + '<u>' + 'Нет ' + '</u>' + ' ')
  else:
    userInput = input("Опишите отеки пациента: ")
    file.write(swelling + ' ' + '<u>' + userInput + '</u>' + ' ')

# раздел температура
def temperature_func():
  temperature = 't\u2103'
  temperatureUserInput = input("Введите температуру пациента: ")
  file.write(temperature + ' ' + '<u>' + temperatureUserInput + '</u>')
  file.write('<br>')

# раздел органов дыхания
def respiratory_organs_func():
  respiratoryOrgans = '<b>Органы дыхания: </b>'
  respInMin = 'ЧДД '
  respInMinUserInput = input("Введите частоту дыхательных движений: ")

  respiratoryOrgansOutput = file.write(respiratoryOrgans + respInMin + '<u>' + respInMinUserInput + '</u>' + ' в мин.,' )
  return respiratoryOrgansOutput

def shortness_breath():
  shortnessBreath = 'одышка '
  shortnessBreathUserInput = input("Есть ли у пациента одышка? 1. экспираторная 2. инспираторная 3. смешанная 4. одышки нет ")

  if shortnessBreathUserInput == '1':
    shortnessBreathOutput = file.write(shortnessBreath + '<u>' + 'эксператорная, ' + '</u>' + 'инспираторная, смешанная. ')
    return shortnessBreathOutput
  elif shortnessBreathUserInput == '2':
    shortnessBreathOutput = file.write(shortnessBreath + 'эксператорная, ' + '<u>' + 'инспираторная, ' + '</u>' +  'смешанная. ')
    return shortnessBreathOutput
  elif shortnessBreathUserInput == '3':
    shortnessBreathOutput = file.write(shortnessBreath + 'эксператорная, ' + 'инспираторная, ' + '<u>' + 'смешанная. ' + '</u>')
    return shortnessBreathOutput
  else:
    shortnessBreathOutput = file.write(shortnessBreath + 'эксператорная, ' + 'инспираторная, ' + 'смешанная. ')
    return shortnessBreathOutput

# Патологическое дыхание
def path_breath():
  pathBreath = 'Патологическое дыхание: '
  pathBreathUserInput = input("Есть ли патологическое дыхание? ")

  pathBreathOutput = file.write(pathBreath + '<u>' + pathBreathUserInput + '</u>')
  return pathBreathOutput

def auscultatively_func():
  file.write('<br>')
  auscultatively = 'Аускультативно: '
  print("Дыхание пациента: 1. везикулярное 2. жесткое 3. бронхиальное. 4. пуэрильное 5. ослаблено 6. отсутствует в (укажите где) ")
  auscultativelyUserInput = input("Введите тип дыхания во время аускультации? ")
  
  if auscultativelyUserInput == '1':
    auscultativelyOutput = file.write(auscultatively + '<u>' + 'везикулярное, ' + '</u>' + 'жесткое, ' + 'бронхиальное, ' + \
                                      'пуэрильное, ' + 'ослаблено, ' + 'отсутствует в ' + '<u>' + 'над всеми полями' + '</u>')
    return auscultativelyOutput
  elif auscultativelyUserInput == '2':
    auscultativelyOutput = file.write(auscultatively + 'везикулярное, ' + '<u>' + 'жесткое, ' + '</u>' + 'бронхиальное, ' + \
                                      'пуэрильное, ' + 'ослаблено, ' + 'отсутствует в ')
    return auscultativelyOutput
  elif auscultativelyUserInput == '3':
    auscultativelyOutput = file.write(auscultatively + 'везикулярное, ' + 'жесткое, ' + '<u>' + 'бронхиальное, ' + '</u>' + \
                                      'пуэрильное, ' + 'ослаблено, ' + 'отсутствует в ')
    return auscultativelyOutput
  elif auscultativelyUserInput == '4':
    auscultativelyOutput = file.write(auscultatively + 'везикулярное, ' + 'жесткое, ' + 'бронхиальное, ' + \
                                      '<u>' + 'пуэрильное, ' + '</u>' + 'ослаблено, ' + 'отсутствует в ')
    return auscultativelyOutput
  elif auscultativelyUserInput == '5':
    auscultativelyOutput = file.write(auscultatively + 'везикулярное, ' + 'жесткое, ' + 'бронхиальное, ' + \
                                      'пуэрильное, ' + '<u>' + 'ослаблено, ' + '</u>' + 'отсутствует в ')
    return auscultativelyOutput
  elif auscultativelyUserInput == '6':
    userInput = input("Где отсутствует дыхание? ")
    auscultativelyOutput = file.write(auscultatively + 'везикулярное, ' + 'жесткое, ' + 'бронхиальное, ' + \
                                      'пуэрильное, ' + 'ослаблено, ' + '<u>' + 'отсутствует в ' + userInput + '</u>')
    return auscultativelyOutput

# хрипы
def dry_wheezing_func():
  # Хрипы сухие (свистящие, жужжащие) в:
  file.write('<br>')
  dryWheezing = 'Хрипы <i>сухие</i>'

  dryWheezingUserInput = input("Есть ли у пациента сухие хрипы? Если есть - указать где (1. свистящие 2. жужжащие 3. нет) ")
  if dryWheezingUserInput == '1':
    dryWheezingInputWhere = input("Локализация хрипов? ")
    dryWheezingOutput = file.write(dryWheezing + '(' + '<u>' + 'свистящие' + '</u>' + ', жужжащие ) ' + '<u>' + dryWheezingInputWhere + '</u>')
    return dryWheezingOutput
  elif dryWheezingUserInput == '2':
    dryWheezingInputWhere = input("Локализация хрипов?")
    dryWheezingOutput = file.write(dryWheezing + '(свистящие, ' + '<u>' + 'жужжащие ' + '</u>' + ') ' + '<u>' + dryWheezingInputWhere + '</u>')
    return dryWheezingOutput
  else:
    dryWheezingOutput = file.write(dryWheezing + '(свистящие, жужжащие) ' + '<u>' + 'отсутствуют во всех отделах' + '</u>')
    return dryWheezingOutput

def wet_wheezing_func():
  # Влажные (мелко-, средне-, крупнопузырчатые) в:
  file.write('<br>')
  wetWheezing = '<i>Влажные </i>'

  wetWheezingUserInput = input("Есть ли у пациента влажные хрипы? Если есть - указать где (1. мелко-, 2. средне-, 3. крупнопузырчатые 4. нет) ")
  if wetWheezingUserInput == '1':
    wetWheezingInputWhere = input("Локализация хрипов? ")
    wetWheezingOutput = file.write(wetWheezing + '(' + '<u>' + 'мелко- ' + '</u>' + ', средне-, крупнопузырчатые) в: ' + '<u>' + wetWheezingInputWhere + '</u>')
    return wetWheezingOutput
  elif wetWheezingUserInput == '2':
    wetWheezingInputWhere = input("Локализация хрипов?")
    wetWheezingOutput = file.write(wetWheezing + '(мелко-, ' + '<u>' + 'средне- ' + '</u>' + ', крупнопузырчатые) в: ' + '<u>' + wetWheezingInputWhere + '</u>')
    return wetWheezingOutput
  elif wetWheezingUserInput == '3':
    wetWheezingInputWhere = input("Локализация хрипов?")
    wetWheezingOutput = file.write(wetWheezing + '(мелко-, ' + 'средне-, ' + '<u>' + 'крупнопузырчатые' + '</u>' + ') в: ' + '<u>' + wetWheezingInputWhere + '</u>')
    return wetWheezingOutput
  else:
    wetWheezingOutput = file.write(wetWheezing + '(мелко-, средне-, крупнопузырчатые) в: ' + '<u>' + 'отсутствуют во всех отделах' + '</u>')
    return wetWheezingOutput
    
    
# Крепитация, шум трения плевры над:
def crepitation_func():
  file.write('<br>')
  crepitationUserInput = input("Есть ли у пациента: 1. крепитация 2. шум трения плевры 3. нет ")
  if crepitationUserInput == '1':
    crepitationInputWhere = input("Локализация крепитации? ")
    crepitationOutput = file.write('<u>' + 'Крепитация' + '</u>' + ', шум трения плевры над: ' + '<u>' + crepitationInputWhere + '</u>')
    return crepitationOutput
  elif crepitationUserInput == '2':
    crepitationInputWhere = input("Локализация шума трения плевры? ")
    crepitationOutput = file.write('Крепитация, ' + '<u>' + 'шум трения плевры над: ' + '</u>' + '<u>' + crepitationInputWhere + '</u>')
    return crepitationOutput
  else:
    crepitationOutput = file.write('Крепитация, шум трения плевры над: ' + '</u>' + '<u>' + 'отсутствуют во всех отделах' + '</u>')
    return crepitationOutput

# Перкуторный звук легочный, тимпанический, коробочный, притупленный, тупой над
def percussive_sound_func():
  file.write('<br>')
  percussiveSound = 'Перкуторный звук '
  percussiveSoundUserUnput = input("Перкуторный звук у пациента: 1. легочный(норма) 2. тимпанический 3. коробочный 4. притупленный 5. тупой ")

  if percussiveSoundUserUnput == '1':
    percussiveSoundOutpute = file.write(percussiveSound + '<u>' + 'легочный' + '</u>' + ', тимпанический, коробочный, притупленный, тупой над:' + \
                                        '<u>' + ' над всеми полями' + '</u>')
    return percussiveSoundOutpute
  elif percussiveSoundUserUnput == '2':
    percussiveSoundWhereInput = input("Локализация перкуторного звука? ")
    percussiveSoundOutpute = file.write(percussiveSound + 'легочный, ' + '<u>' + 'тимпанический' + '</u>' + ', коробочный, притупленный, тупой над:' + \
                                        '<u>' + percussiveSoundWhereInput + '</u>')
    return percussiveSoundOutpute                                    
  elif percussiveSoundUserUnput == '3':
    percussiveSoundWhereInput = input("Локализация перкуторного звука? ")
    percussiveSoundOutpute = file.write(percussiveSound + 'легочный, тимпанический, ' + '<u>' + 'коробочный' + '</u>' + ', притупленный, тупой над:' + \
                                        '<u>' + percussiveSoundWhereInput + '</u>')
    return percussiveSoundOutpute
  elif percussiveSoundUserUnput == '4':
    percussiveSoundWhereInput = input("Локализация перкуторного звука? ")
    percussiveSoundOutpute = file.write(percussiveSound + 'легочный, тимпанический, коробочный,' + '<u>' + 'притупленный' + '</u>' + ', тупой над:' + \
                                        '<u>' + percussiveSoundWhereInput + '</u>')
    return percussiveSoundOutpute
  elif percussiveSoundUserUnput == '5':
    percussiveSoundWhereInput = input("Локализация перкуторного звука? ")
    percussiveSoundOutpute = file.write(percussiveSound + 'легочный, тимпанический, коробочный, притупленный, ' + '<u>' + 'тупой над: ' + '</u>' + \
                                        '<u>' + percussiveSoundWhereInput + '</u>')
    return percussiveSoundOutpute
    
# кашель, мокрота    
def cough_func():
  file.write('<br>')
  cough = 'Кашель '
  sputum = 'Мокрота. '
  сoughUserInput = input("Характер кашля пациента: Кашель 1. сухой, 2. влажный, 3. лающий 4. нет ")

  if сoughUserInput == '1':
    coughWhereInput = input("Характер мокроты при кашле")
    coughOutput = file.write(cough + '<u>' + 'сухой' + '</u>' + ' , влажный, лающий. ' + sputum + '<u>' + coughWhereInput + '</u>')
    return coughOutput
  elif сoughUserInput == '2':
    coughWhereInput = input("Характер мокроты при кашле")
    coughOutput = file.write(cough + 'сухой, ' + '<u>' + 'влажный ' + '</u>' + ' , лающий. ' + sputum + '<u>' + coughWhereInput + '</u>')
    return coughOutput
  elif сoughUserInput == '3':
    coughWhereInput = input("Характер мокроты при кашле")
    coughOutput = file.write(cough + 'сухой, влажный, ' + '<u>' + 'лающий. ' + '</u>' + sputum + '<u>' + coughWhereInput + '</u>')
    return coughOutput
  else:
    coughOutput = file.write(cough + 'сухой, влажный, лающий. ' + sputum + '<u>' + 'нет' + '</u>')
    return coughOutput

def circulatory_organs_func():
  file.write('<br>')
  circulatoryOrgans = '<b>Органы кровообращения: </b>'
  
  pulseRate = input("Введите пульс пациента: ")
  pulseRateOutput = file.write(circulatoryOrgans + '<u>' + pulseRate + '</u>' + ' в мин. ')

  pulseRateChr = input("Характер пульса пациента: 1. ритмичный 2. аритмичный ")
  if pulseRateChr == '1':
    pulseRateChrOutput = file.write('<u>' + 'ритмичный' + '</u>' + ', аритмичный, наполнение ')
  else:
    pulseRateChrOutput = file.write('ритмичный, ' + '<u>' + 'аритмичный' + '</u>' + ', наполнение ')
  
  pulseRateNpl = input("Наполнение пульса пациента: 1. удовлетворительное 2. слабое ")
  if pulseRateNpl == 1:
    pulseRateNpl = file.write('<u>' + 'удовлетворительное' + '</u>')
  else:
    pulseRateNpl = file.write('<u>' + ' слабое' + '</u>')
  
  cssRate = ' ЧСС '
  cssRateInput = input('Введите ЧСС пациента: ')
  cssRateOutput = file.write(cssRate + '<u>' + cssRateInput + '</u>')


# main app
file = open('example.html', 'w') # открываем главный файл
html_begin()
complaints_func()
anamnesis_func()
objectively_func()
conscience_func()
glasgo_func()
position_func()
skin_covers_func()
rash_func()
lymph_nodes()
bed_sores()
swelling_func()
temperature_func()
respiratory_organs_func()
shortness_breath()
path_breath()
auscultatively_func()
dry_wheezing_func()
wet_wheezing_func()
crepitation_func()
percussive_sound_func()
cough_func()
circulatory_organs_func()
html_exit()
file.close()