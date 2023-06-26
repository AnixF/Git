per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))
deposit = [int(money * per_cent[key] / 100) for key in per_cent]
max_deposit = max(deposit)
print('Депозиты по банкам:', deposit)
print('Максимальная сумма, которую вы можете заработать -', max_deposit)

input("Нажмите Enter для выхода")