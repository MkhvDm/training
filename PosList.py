class NonPositiveError (Exception):
    pass

class PositiveList (list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            super().append(x)


test_lst = PositiveList()
for i in range(5):
    try:
        test_lst.append(int(input()))
        print(test_lst)
    except:
        print('Value is not positive!')

