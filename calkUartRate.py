'''
clk_value = 125.0
clk_uart_array = [0.004800, 0.009600, 0.019200, 0.038400, 0.57600, 0.115200, 0.128000, 0.256000, 0.512000, 0.921600,
                  1.0, 2.0, 3.0, 4.0, 5.0]

for clk_i in clk_uart_array:
    print('#', clk_i*1000000)
    mode_uart_rate = clk_value // (2 * clk_i)
    print('mode_uart_rate =', mode_uart_rate)

    tmp = mode_uart_rate + mode_uart_rate + 1
    real_uart_rate = clk_value / tmp
    print('real_uart_rate =', round(real_uart_rate*1000000, 2))

    delta = (clk_i - real_uart_rate)*1000000
    delta_percants = abs(delta)/(clk_i*10000)
    print('delta =', round(delta,2), '\t', round(delta_percants, 3), '%\n')
'''


'''from math import pi
N = 31232
D = 1000
S = D*pi
print(S)
mm = N/S
print(mm)'''

clk_value = 1_953_125 #125_000_000.0
v_kmph = 160.0
v_mms = v_kmph*1000/3.6
print('частота следования миллиметров:', v_mms) #f_mm
# t_mm = 1000000/v_mms
# print(t_mm)
print('тактов 125М между мм:', clk_value/v_mms)

time = 1/40
freq = 40
ratio = clk_value/freq
print(ratio)

cnt = ratio/(clk_value/v_mms)
print(cnt)
