def solution1(list):
    count = 0
    reverse = sorted(list, reverse=True)
    for i in reverse:
        if i > 0:
            count += 1
    return count


arr1 = []
arr2 = [0]
arr3 = [0, 1]
arr4 = [1, 0]
arr5 = [1, 0, 0]
arr6 = [0, 1, 0]
arr7 = [0, 0, 1]
arr8 = [1, 2]
arr9 = [1, 2, 0]
arr10 = [0, 1, 2]

print(f"arr1: {solution1(arr1)}")
print(f"arr2: {solution1(arr2)}")
print(f"arr3: {solution1(arr3)}")
print(f"arr4: {solution1(arr4)}")
print(f"arr5: {solution1(arr5)}")
print(f"arr6: {solution1(arr6)}")
print(f"arr7: {solution1(arr7)}")
print(f"arr8: {solution1(arr8)}")
print(f"arr9: {solution1(arr9)}")
print(f"arr10: {solution1(arr10)}")
