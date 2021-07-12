# print('Start2:', 'N =', N, 'k =', k, 'm =', m, 'if:', (N//2 + 1))

def primes():
    N, k, m = 1, 2, True
    while True:
        N += 1     # проверяем это число на простоту
        k = 2      # проверяем делитель ли это? ("1" - делитель у всех, начинаем с "2")
        m = True   # текущее состояние простоты
        while k < (N//2 + 1):
            if N % k == 0:
                m = False
                break
            k += 1
        if m: yield N


my_primes_gen = primes()
i = 0
while i < 10:
    print(next(my_primes_gen))
    i += 1
