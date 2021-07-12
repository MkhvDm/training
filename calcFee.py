USDRUB = 76.9
USDRUB_bank = USDRUB - 1.3
value_usd = 10000
broker_fee = 0.0005
exchange_fee = 0.000015
currency_broker_fee = 0.002
value_to_currency_fee_usd = value_usd - 7800

total_fee = value_usd*(broker_fee*2 + exchange_fee*2) + value_to_currency_fee_usd*currency_broker_fee
print('Комиссия при конвертации на бирже:')
# print('total fee, USD =', total_fee)
print('total fee, RUB =', total_fee*USDRUB, '\n')

total_fee_bank = value_usd*(USDRUB - USDRUB_bank)
print('"Комиссия" при конвертации в банке:')
print('total fee, RUB =', total_fee_bank, '\n')



