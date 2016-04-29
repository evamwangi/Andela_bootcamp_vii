def solution(a):
    max_ = 0 #max value
    current = 0 #current value

    #skip the tailing zero(s)
    while a > 0 and a % 2 == 0:
        a //= 2

    while a > 0:
        remainder = a % 2 
        if remainder == 0:

            current += 1
        else:

            if current != 0:
                max_ = max(current, max_)
                current = 0
        a //= 2

    return max_

print solution(15)
print solution(150)
print solution(20)
print solution(529)