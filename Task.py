list1 = ['hello', '2', 'world', ':-)']
list2 = ['1234', '1567', '-2', 'computer science',]
list3 = ['Russia', 'Denmark', 'Kazan']


def func(arr = []):
    result = []
    for i in range(len(arr)):
        if len(str(arr[i])) <= 3:
            result.append(str(arr[i]))
    return result
    

print('', func(list1),'\n', func(list2),'\n', func(list3))