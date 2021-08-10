array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):  # ex) i=0, j=1
        if array[min_index] > array[j]:  # array[0] > array[1]
            min_index = j  # min_index = 1
    array[i], array[min_index] = array[min_index], array[i]  # 스와프 -> [0], [1] = [1], [0]

print(array)
