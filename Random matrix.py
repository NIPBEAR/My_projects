import random
import sys


class RandomMatrix(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        RandomMatrix.__instance = None

    def __init__(self, m_size, kol_el):
        self.m_size = m_size
        self.kol_el = kol_el

    def create_matrix(self):
        lst = [[0] * self.m_size for _ in range(self.m_size)]
        k = 0
        while k < self.kol_el:
            i = random.randint(0, len(lst) - 1)
            j = random.randint(0, len(lst) - 1)
            if lst[i][j] != 1:
                lst[i][j] = 1
                k += 1
        return lst


def check_input(m_size: str, kol_el: str or int) -> tuple[int, int]:
    try:
        m_size = int(m_size)
        kol_el = int(kol_el)
    except ValueError:
        sys.exit('Error_input')
    if m_size <= 0 or kol_el <= 0 or m_size ** 2 < kol_el:
        sys.exit('Error_input')
    return m_size, kol_el


def is_isolate(*args):
    return not sum(args) > 1


def verify(lst: list) -> bool:
    for i in range(len(lst) - 1):
        for j in range(len(lst[i]) - 1):
            res = is_isolate(lst[i + 1][j], lst[i + 1][j + 1],
                             lst[i][j + 1], lst[i][j])
            if not res:
                return False
    return True


def isolate_matrix(m_size: int, kol_el: int) -> list:
    cl_lst = RandomMatrix(m_size, kol_el)
    count = 0
    while True:
        lst = cl_lst.create_matrix()
        if verify(lst):
            break
        count += 1
        if count == 100000:
            sys.exit('Not found')
    return lst


def output(m_size: int, kol_el: int):
    lst = isolate_matrix(m_size, kol_el)
    for i in lst:
        for j in i:
            print(j, end=' ')
        print()


N = input('Enter matrix size N x N, N = ')
M = 1
N, M = check_input(N, M)
output(N, M)
