lista = [32, 54, 78, 86, 90, 120]
f = lambda c: c * (9.0 / 5.0) + 32.0

# convertendo a lista em fahrenheit
print(list(map(f, lista)))
