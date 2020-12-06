import json

profit = {}
pr = {}
profit_2 = 0
profit_avr = 0
i = 0
with open('firm.txt', 'r') as file:
    for line in file:
        name, firm, earn, losses = line.split()
        profit[name] = int(earn) - int(losses)
        if profit.setdefault(name) >= 0:
            profit_2 = profit_2 + profit.setdefault(name)
            i += 1
    if i != 0:
        profit_avr = profit_2 / i
        print(f'Средняя прибыль - {profit_avr:.2f}')
    else:
        print(f'Компании работают в убыток')
    pr = {'Средняя прибыль': round(profit_avr)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('firm.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
