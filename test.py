import re

x = '3456file.csv'

y = re.findall('csv$', x)

if y:
    print(x)
else:
    print('kein xml')

print(y)