def solution(X, Y):
    answer = []

    dic_X = {}
    dic_Y = {}
    for k in range(10):
        dic_X.update({str(k) : 0})
        dic_Y.update({str(k) : 0})

    for k in X:
        dic_X[k] += 1
    
    for k in Y:
        dic_Y[k] += 1
    
    for x, y in zip(dic_X.items(), dic_Y.items()):
        if min(x[1], y[1]) > 0:
            answer.extend(x[0] * min(x[1], y[1]))
    
    if set(answer) == {'0'}:
        return '0'
    return ''.join(answer[::-1]) if len(answer) > 0 else '-1'