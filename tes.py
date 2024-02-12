
def is_subarray(subarray, array):
    len_subarray = len(subarray)
    len_array = len(array)

    for i in range(len_array - len_subarray + 1):
        if array[i:i + len_subarray] == subarray:
            return True
    
    return False

#print(is_subarray([1,2,3], []))

def count_subarrays(subarray, array):
    len_subarray = len(subarray)
    len_array = len(array)
    count = 0

    for i in range(len_array - len_subarray + 1):
        if array[i:i + len_subarray] == subarray:
            count += 1

    return count


array1 = [1, 2, 1, 2, 1, 2,1]
subarray1 = [5, 4, 3]
subarray2 = [1, 2, 3]
subarray3 = [1, 2, 1]
subarray4 = [1, 1]

print(count_subarrays(subarray1, array1))  # 0
print(count_subarrays(subarray2, array1))  # 1
print(count_subarrays(subarray3, array1))  # 2
print(count_subarrays(subarray4, array1))  # 3
