def solution(participant, completion):
    part = participant
    part.sort()
    comp = completion
    comp.sort()
    comp.append('')
    answer = ''
    for i in range(len(part)):
        if part[i] != comp[i]:
            answer = part[i]
            break
    return answer