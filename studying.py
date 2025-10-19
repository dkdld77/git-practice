def grade(score):
    if score > 100:
        return 'None in range'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 0 and score < 60:
        return 'F'
    else:
        return 'None in range'

score = list(map(int, input().split()))
average = sum(score) / len(score)
print(average)
for i in range(len(score)):
    a = grade(score[i])
    print(a)
