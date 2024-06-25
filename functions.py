def search_linear(arr):
    for elem in arr:
        print(elem)

def count_linear(lists, findWord):
    start_time = time.time()
    print('BEGIN COUNT')

    count = 0

    for word in lists:
        if word == findWord:
            count += 1
    
    print('--- COUNT : --- %s seconds ---' % (time.time() - start_time))

def fibonacci_iteratif(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def search_binary(word, sorted_list):
    if not sorted_list:
        return []
    index_middle = len(sorted_list) // 2
    if word == sorted_list[index_middle]:
        return sorted_list
    elif word > sorted_list[index_middle]:
        return search_binary(word, sorted_list[index_middle+1:])
    else:
        return search_binary(word, sorted_list[:index_middle])

def count_binary(word, sorted_list):
    new_list = search_binary(word, sorted_list)
    if not new_list:
        return 0

    index_middle = len(sorted_list) // 2
    count = 1

    idx1 = index_middle + 1
    while idx1 < len(sorted_list) and sorted_list[idx1] == word:
        count += 1
        idx1 += 1

    idx2 = index_middle - 1
    while idx2 >= 0 and sorted_list[idx2] == word:
        count += 1
        idx2 -= 1

    return count