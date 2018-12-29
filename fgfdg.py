for name in names:
    for warrior in name:
        print(warrior)

print(names[-1])
print()
print()
print()
print(names[0][0])
print(names[2][2])
print(names[-2][-1])

names[-1][-1]="최무선"
print(names)

names.sort()
print(names)
