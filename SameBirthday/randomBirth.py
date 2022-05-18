import random


class Birthday(object):
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def equal(self, birth):
        if self.month == birth.month and self.day == birth.day:
            return True
        else:
            return False


def sort(s):
    return s.month * 100 + s.day


def find_same_birth(birth):
    length = len(birth)
    same = []
    for a in range(length):
        for b in range(a + 1, length):
            if birth[a].equal(birth[b]):
                same.append(birth[a])
    return same


# <editor-fold desc="Test same birthday in 35 students">
def test():
    classMates = []

    for i in range(35):
        stu = Birthday(random.randint(1, 12), random.randint(1, 31))
        classMates.append(stu)

    classMates.sort(key=sort)

    for i in classMates:
        print('Month:' + str(i.month) + ' Day:' + str(i.day))

    sameBirth = find_same_birth(classMates)
    for i in sameBirth:
        print('Same Birthday Month:' + str(i.month) + ' Day:' + str(i.day))


# test()


# </editor-fold>

def class_size(size):
    new_class = []
    for s in range(size):
        birth = Birthday(random.randint(1, 12), random.randint(1, 31))
        new_class.append(birth)

    return find_same_birth(new_class)


def probability(min_class, max_class):
    for i1 in range(min_class, max_class + 1):
        p = 0
        pair = 0
        for i2 in range(10000):
            if len(class_size(i1)) > 0:
                p = p + 1
                pair = pair + len(class_size(i1))
        print('Class size:' + str(i1) + ', At least one pair probability:' + str(
            p / 100) + '%, Happen to you probability:' + str(round(pair * 2 / 100 / i1, 2)) + '%')


Min_Class = 10
Max_Class = 100
probability(Min_Class, Max_Class)
