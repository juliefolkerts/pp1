def f (subject):
    max_avg = 0
    sub = ''
    for key,value in subject.items():
        if (sum(subject[key]) / len(subject[key])) > (max_avg):
            sub = key
            max_avg = sum(subject[key]) / len(subject[key])
    return sub

if __name__ == '__main__':
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))