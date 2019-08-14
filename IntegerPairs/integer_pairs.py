def first(arr, sum):
    answer = []
    for x in arr:
        for y in arr:
            if x + y == sum:
                answer.append([x, y])
    return answer

# def second(list, sum):
#     print(sorted(list)
