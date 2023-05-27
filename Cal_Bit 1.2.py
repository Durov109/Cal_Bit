#Создаем калькулятор

monetky = float(input('Введите количество монет:'))
start_sum = float(input('Введите начальную сумму крипты:'))
final_sum = float(input('Введите финальную продажу крипты:'))
kurs = float(input('Введите курс доллара:'))
#kurs_1 = float(input('Введите курс доллара по которому покупали:'))
#kurs_2 = float(input('Введите курс доллара по которому продали:'))

step_1 = final_sum - start_sum #Получаем сумму прироста
step_2 = step_1 * monetky #Сумму прироста умножаем на кол-во монет и получаем прибыль в долларах
step_3 = kurs * step_2 #Получаем прибыль в рублях

print('_______________________________')
print(f"Курс доллара: {kurs}")
print(f'Начальная сумма монеты: {start_sum}')
print(f'Финальная сумма монеты:{final_sum}')
print(f'Количество монет: {monetky}')
print('_______________________________')
if step_3 > 0: # Если проторговали в плюс
    print(f'Прирост в рублях: {step_3}')
    print(f'Прирост в долларах: {step_2}')
    print(f'Общая сумма в долларах было: {monetky * start_sum}, стало: {monetky * final_sum}')
    print(f'Общая сумма в рублях было: {monetky * start_sum * kurs}, стало: {monetky * final_sum * kurs}')
    
elif step_3 < 0: # Если проторговали в убыток
    print(f'Убыток в рублях: {step_3}')
    print(f'Убыток в долларах: {step_2}')
    print(f'Общая сумма в долларах было: {monetky * start_sum}, стало: {monetky * final_sum}')
    print(f'Общая сумма в рублях было: {monetky * start_sum * kurs}, стало: {monetky * final_sum * kurs}')
