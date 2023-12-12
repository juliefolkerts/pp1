def f(subjects):
    averages = []
    for subject,grades in subjects.items():
        averages.append(sum(grades)/len(grades))
    max_average = max(averages)
    max_subject = ''
    for key, value in subjects.items():
        if (sum(value)/len(value))  == max_average:
            max_subject = key
    return max_subject


subjects = {"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}

print(f(subjects))

