def enrollment_stats(universities):
    students = []
    tuition = []
    for n in range (len(universities)):
        students.append(universities[n][1])
        tuition.append(universities[n][2])
    return [students, tuition]

def total(list):
    total_students = 0
    total_tuition = 0
    for n in range (len(list)):
        total_students += list[n][1]
        total_tuition += list[n][2]
    return [total_students, total_tuition] 

def mean(list):
    mean = [0,0]
    for n in range(len(list)):
        for i in range(len(list[n])):
            mean[n] = mean[n] + list[n][i]
        mean[n] = mean[n] / len(list[n])
    return mean


universities = [
    ["CIT", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["MIT", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500]
]

print "*****************"
print "Total students: {}".format(total(universities)[0])
print "Total tuition: ${}".format(total(universities)[1])
print "Student mean: {}".format(mean(enrollment_stats(universities))[0])
print "Tuition mean: ${}".format(mean(enrollment_stats(universities))[1])


