# Bad modular code example
# This example called spaghetti code and not something good to be followed

s = [88, 92, 79, 93, 85]  # Student test scores
print(sum(s) / len(s))  # print mean of test scores

s1 = []
for x in s:
    s1.append(x + 5)

print(sum(s1) / len(s1))

s2 = []
for x in s:
    s2.append(x + 10)

print(sum(s2) / len(s2))

s3 = []
for x in s:
    s3.append(x ** 0.5 * 10)

print(sum(s3) / len(s3))
