lst0 = list(map(int, input().split()))


def splitting_lists(lst: list) -> list:
    """
    Разбивка списка на части
    """
    res = []
    if len(lst) >= 3:
        half = len(lst) // 2
        lst = lst[:half]
        lst2 = lst[half:]
        res += [*splitting_lists(lst)]
        res += [*splitting_lists(lst2)]
    else:
        res += [lst]
    return res


def list_comparison(lst1: list, lst2: list) -> list:
    """
    Сортировка 2-х списков и соединение их в один
    """
    res = []
    i = 0
    j = 0
    while True:
        while True:
            if i == len(lst1) and j < len(lst2):
                res.append(lst2[j])
                j += 1
            elif j > len(lst2) - 1:
                break
            elif lst1[i] <= lst2[j]:
                res.append(lst1[i])
                i += 1
            elif lst1[i] > lst2[j]:
                res.append(lst2[j])
                j += 1
        if j > len(lst2) - 1 and i != len(lst1):
            res.append(lst1[i])
            i += 1
        elif i == len(lst1):
            break
    return res


def merge_sort(lst: list) -> list:
    """
    Сортировка слиянием
    """
    res = []
    temp = splitting_lists(lst)
    for i in range(len(temp)):
        if len(temp[i]) > 1:
            for j in range(len(temp[i])):
                if temp[i][0] > temp[i][1]:
                    temp[i][0], temp[i][1] = temp[i][1], temp[i][0]
    while True:
        res.clear()
        if len(temp) % 2 == 0:
            for i in range(0, len(temp) - 1, 2):
                res.append(list_comparison(temp[i], temp[i+1]))
        else:
            for i in range(0, len(temp) - 2, 2):
                res.append(list_comparison(temp[i], temp[i+1]))
            res.append(temp[len(temp)-1])
        temp = res.copy()
        if len(res) == 1:
            break
    return res


def output(lst: list):
    """
    Вывод
    """
    if len(lst) == 1:
        print(*lst)
    elif len(lst) == 2:
        if lst[0] >= lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
        print(*lst)
    elif len(lst) > 2:
        input_list = merge_sort(lst)
        print(' '.join(map(str, *input_list)))


output(lst0)
