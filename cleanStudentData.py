import pandas as pd
import re
with open('studentData.txt', 'r') as f:
    count = -1
    lines = f.readlines()
    for index, line in enumerate(lines):
        if(index < len(lines) -1):
            combined = str(line + lines[index +1])
            print(combined)
            print('---------------------------------------------------------------')

    # for row in f:
    #     count += 1
    #    # full = row + f[count]
    #     lst = re.findall('\S+@\S+', row)
    #     if(len(lst) > 0):
    #         email = lst[0]
    #     print(f[count])
