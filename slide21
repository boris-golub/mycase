print()
print('*****************************')
print('*          Привет!          *')
print('*     Это игра в ГОРОДА     *')
print('*****************************')
print()
print('Для выхода из игры нажми "5" в свой ход')
print('Итак, начинаем!!!')
print()

history = []
priority = ('Твой ход:  ', 'Ход друга: ')
i = 0
 
while True:
   
   city = input(priority[i]).lower()  
   
   if city == '5': 
      break
   if len(history) != 0 and city[0] != last_letter:
      print(f'... город должен начинаться на букву "{last_letter}"')
      continue
   if city in history:
      print('... это название уже было')
      continue
   
   history.append(city)
   
   last_letter = city[-1]
   if city[-1] in ['ь','ъ','й','ы']:
      last_letter = city[-2]
   
   i = (i + 1) % 2
