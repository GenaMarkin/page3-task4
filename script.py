import array as arr

num_storage = arr.array('i', [])
for i in range(5):
    input_b = int(input('type a number: '))
    input_c = int(input('type b number: '))

    pair = (input_b, input_c)

    x = max(pair)
    num_storage.append(x)
y = min(num_storage)
print('min num is:', y, 'index of this num is:', num_storage.index(y) + 1)
