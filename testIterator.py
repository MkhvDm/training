
class multifilter: # итерируемый объект

    def judge_half(pos, neg):
        return pos >= neg
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return not neg

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.pos = 0
        self.neg = 0
        self.funcs = funcs
        self.judge = judge

        self.lenth = len(iterable)
        self.i = 0
        self.res = []
        self.resLength = 0
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        for elem in self.iterable:
            self.pos = 0
            self.neg = 0
            for func in self.funcs:
                if func(elem):
                    self.pos += 1
                else:
                    self.neg += 1
            # print('pos =', self.pos, 'neg =', self.neg)
            if self.judge(self.pos, self.neg):
                # print('add:', elem)
                self.res.append(elem)
        self.resLength = len(self.res)
        return

    def __iter__(self):
        return self
        # возвращает итератор по результирующей последовательности

    def __next__(self):
        if self.i < self.resLength:
            self.i += 1
            return self.res[self.i - 1]
        else:
            raise StopIteration





def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]