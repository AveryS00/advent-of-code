
with open('input.txt') as f:
    arr = [int(i.strip()) for i in f.readlines()]
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(j, len(arr)):
                if arr[i] + arr[j] + arr[k] == 2020:
                    print('Found: {} and {} and {}'.format(arr[i], arr[j], arr[k]))
                    print(arr[i] * arr[j] * arr[k])
