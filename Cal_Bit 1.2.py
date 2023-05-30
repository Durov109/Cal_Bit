import requests
#Создаем крипто-калькулятор

print("Приветсвтвую, что хотите узнать: курсы валют и криптоактивов - введите 1, включить калькулятор - введите 2")

def price():
    # Запрос к API Центрального Банка России
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

    # Получение данных о курсах валют в формате JSON
    data = response.json()

    # Получение курса рубля к доллару и евро
    usd_rate = data['Valute']['USD']['Value']
    eur_rate = data['Valute']['EUR']['Value']

    # Вывод курсов валют
    print(f'Курс рубля к доллару: {usd_rate:.2f}')
    print(f'Курс рубля к евро: {eur_rate:.2f}')
    
    # Список криптовалют, для которых нужно получить курс
    symbols = ['bitcoin', 'ethereum', 'litecoin']

    # Параметры для запроса к API CoinGecko
    params = {'ids': ','.join(symbols), 'vs_currencies': 'usd'}

    # Запрос к API CoinGecko для получения курсов криптовалют
    response = requests.get('https://api.coingecko.com/api/v3/simple/price', params=params)

    # Получение данных о курсах криптовалют в формате JSON
    data = response.json()

    # Извлечение курсов криптовалют
    btc_rate = data['bitcoin']['usd']
    eth_rate = data['ethereum']['usd']
    ltc_rate = data['litecoin']['usd']

    # Вывод курсов криптовалют
    print(f'Курс биткоина: {btc_rate:.2f}')
    print(f'Курс эфириума: {eth_rate:.2f}')
    print(f'Курс лайткоина: {ltc_rate:.2f}')


def option_1():
    user_reply = 3  #Ставил тройку чтобы выполнялся цикл while
    while user_reply!=1 or user_reply!=2:
        user_reply = int(input()) #спрашиваем у пользователя что хочет
        # если хотел узнать курсы
        if user_reply==1:
            price()
            break
        #если выбрал калькулятор
        elif user_reply==2:
            monetky = float(input('Введите количество монет:'))
            start_sum = float(input('Введите начальную сумму крипты:'))
            final_sum = float(input('Введите финальную продажу крипты:'))
            #kurs = float(input('Введите курс доллара:'))
            
            step_1 = final_sum - start_sum #Получаем сумму прироста
            step_2 = step_1 * monetky #Сумму прироста умножаем на кол-во монет и получаем прибыль в долларах
            step_3 = dollar() * step_2 #Получаем прибыль в рублях
            
            if step_3 > 0: # Если проторговали в плюс
                print()
                print(f"Курс доллара: {dollar()}")
                print(f'Начальная сумма монеты: {start_sum}')
                print(f'Финальная сумма монеты:{final_sum}')
                print(f'Количество монет: {monetky}')
                print()
                print(f'Прирост в рублях: {step_3}')
                print(f'Прирост в долларах: {step_2}')
                print(f'Общая сумма в долларах было: {monetky * start_sum}, стало: {monetky * final_sum}')
                print(f'Общая сумма в рублях было: {monetky * start_sum * dollar()}, стало: {monetky * final_sum * dollar()}')
                break
    
            elif step_3 < 0: # Если проторговали в убыток
                print()
                print(f"Курс доллара: {dollar()}")
                print(f'Начальная сумма монеты: {start_sum}')
                print(f'Финальная сумма монеты:{final_sum}')
                print(f'Количество монет: {monetky}')
                print()
                print(f'Убыток в рублях: {step_3}')
                print(f'Убыток в долларах: {step_2}')
                print(f'Общая сумма в долларах было: {monetky * start_sum}, стало: {monetky * final_sum}')
                print(f'Общая сумма в рублях было: {monetky * start_sum * dollar()}, стало: {monetky * final_sum * dollar()}')
                break
        else:
            print("Надо ввести 1 или 2")
#kurs_1 = float(input('Введите курс доллара по которому покупали:'))
#kurs_2 = float(input('Введите курс доллара по которому продали:'))

def dollar():
    # Запрос к API Центрального Банка России
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    # Получение данных о курсах валют в формате JSON
    data = response.json()
    # Получение курса рубля к доллару и евро
    usd_rate = data['Valute']['USD']['Value']
    return usd_rate

def euro():
    # Запрос к API Центрального Банка России
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    # Получение данных о курсах валют в формате JSON
    data = response.json()
    # Получение курса рубля к доллару и евро
    eur_rate = data['Valute']['EUR']['Value']
    return eur_rate
option_1()