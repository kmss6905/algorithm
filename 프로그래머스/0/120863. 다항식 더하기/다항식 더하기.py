def solution(polynomial):
    answer = []
    elements = polynomial.split(' + ')
    xsum = 0
    nusum = 0
    for element in elements:
        if 'x' in element:
            if element == 'x':
                xsum += 1
            else:
                xsum += int(element[:-1])
        else:
            nusum += int(element)
    
    result = []
    if xsum:
        if xsum == 1:
            answer.append("x")
        else:
            answer.append(f"{xsum}x")
    if nusum:
        answer.append(str(nusum))

    return " + ".join(answer)
    