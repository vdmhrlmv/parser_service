# import re
#
#
# s = '1   2df .32d   d 656 :;dfdfvdv\n апрпорвов    орор kkkk l 4562'
#
# result = re.findall(r'(\s{,1}\S)', s) #[^\t\n\r]
#
# print(result)
# print(s)
# print(''.join(result))


import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# FILES_DIR = Path(__file__).resolve().parent.joinpath('files')
# print(FILES_DIR)

import re

file = '/home/vdm/Документы/AG/пушкин/Text_v1.txt'
file_res_1 = '/home/vdm/Документы/AG/пушкин/Text_v1_result_1.txt'
file_res_2 = '/home/vdm/Документы/AG/пушкин/Text_v1_result_2.txt'

out_1 = out_2 = ''
count_1 = count_2 = 0
with open(file) as f:
    for line in f:
        match = re.search(r'[A-Z|a-z]|(\[|\])|\d+', line) #<|>|\*  #\W:[^<>]+
        if match:
            out_1 += line
            count_1 += 1
        else:
            out_2 += line
            count_2 += 1


#result = ''.join(re.findall(r'\s{,1}\S' ,text))
#result = ''.join(re.findall(r'\s[а-яА-Я]', text))

with open(file_res_1, 'w') as f:
    f.write(out_1)

with open(file_res_2, 'w') as f:
    f.write(out_2)

print('count_1 =', count_1)
print('count_2 =', count_2)
