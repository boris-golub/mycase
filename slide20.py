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
