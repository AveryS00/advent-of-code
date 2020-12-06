with open('input.txt') as f:
    arr = f.read().split('\n\n')


count = 0
for group in arr:
    occurrences = {}
    persons = group.split('\n')
    for person in persons:
        for question in person:
            if question in occurrences:
                occurrences[question] += 1
            else:
                occurrences[question] = 1
    for key, val in occurrences.items():
        count += len(persons) == val
print(count)


''' Part 1
count = 0
for group in arr:
    occurrences = {}
    persons = group.split('\n')
    for person in persons:
        for question in person:
            occurrences[question] = 1
    count += len(occurrences.items())
print(count)
'''