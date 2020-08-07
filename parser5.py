import re

if re.compile('^[A-Z]{3,5}$').findall('AB'.strip()):
    print('yes')

for (index, (a, b)) in enumerate(zip(list(range(5)), list(range(5)))):
    print(index, a, b)
