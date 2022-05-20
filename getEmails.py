import pandas as pd
import re
import os

directory = r'C:\Users\chris\Desktop\SCU_CONTACTS'
df = pd.DataFrame(columns=['emails'])
count = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f, 'r') as h:
            lines = h.readlines()
            for index, line in enumerate(lines):
                if(index < len(lines) -1):
                            combined = str(line + lines[index +1])
                            e = re.findall('\S+@\S+', combined)
                            
                            email = str(e)
                            sb = email.replace('[', "")
                            sb1 = sb.replace(']', "")
                            sb2= sb1.replace("'", "")
                            df = df.append({'emails': sb2}, ignore_index=True)


df1 = df.drop_duplicates()
df1.to_csv('email_list_final.csv', index=False)