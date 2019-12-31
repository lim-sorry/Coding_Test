def solution(arr):
    answer = arr[0:1]
    i = 1
    while i < len(arr):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
        i += 1
    return answer
