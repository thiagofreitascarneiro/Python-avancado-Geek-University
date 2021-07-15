def data_convert(h, m, s):
    min = m * 60
    horas = h * 60 * 60
    tot = min + horas + s
    return tot


print(f'{data_convert(1, 30, 45)} segundos')

data = lambda h, m, s: (h * 60 * 60) + (m*60) + s
print(data(1, 30, 45))
