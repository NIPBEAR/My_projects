def func_show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'Площадь прямоугольника: {res}')
        return res
    return wrapper

@func_show
def get_sq(width, height):
    return width*height

width, height = map(int, input().split())

res = get_sq(width, height)
